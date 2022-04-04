from io import RawIOBase
import json
from django.core.checks import messages
import recipes
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import AnonymousUser
from django.db import IntegrityError
from django.db.models import query
from django.db.models.fields import AutoField
from django.http import HttpResponse, HttpResponseRedirect, request
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.urls import reverse

from .models import *

# Create your views here.
def index(request):
    recipes = Recipe.objects.all().order_by('title')
    return index_view(request, "Home", recipes)

@login_required
def my_recipes(request):
    user = request.user
    recipes = Recipe.objects.filter(user=user).order_by('title')
    return index_view(request, "My Recipes", recipes)

def show_search(request):
    name = request.GET['q']
    if Recipe.objects.filter(title__iexact=name).exists():
        recipe = Recipe.objects.get(title__iexact=name)
        return recipe_page(request, recipe.id)
    elif Recipe.objects.filter(title__icontains=name).exists():
        recipes = Recipe.objects.filter(title__icontains=name).order_by('title')
        return index_view(request, f'Correlated results for: {name}', recipes)
    else:
        return render(request, "recipes/index.html", {
            "message": f'No results found for: "{name}"'
        })

@login_required
def saved_recipes(request):
    user = request.user
    if Saved.objects.filter(user=user).exists():
        s = Saved.objects.get(user=user)
        recipes = s.recipe.all().order_by('title')
        return index_view(request, "Saved Recipes", recipes)
    else:
        return render(request, "recipes/index.html", {
            "type": "Saved Recipes",
        })
    
def index_view(request, type, recipes):
    categories = []
    for recipe in recipes:
        categories.append(recipe.category.id)
    categories.sort()
    c = Category.objects.filter(id__in=categories)

    return render(request, "recipes/index.html", {
        "type": type,
        "categories": c,
        "recipes": recipes
    })

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "recipes/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "recipes/login.html")

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))

def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "recipes/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "recipes/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "recipes/register.html")

@login_required
def new_recipe(request):
    c = Category.objects.all()
    return render(request, "recipes/new.html", {
        "categories": c,
        "title": "New Recipe"
    })

@login_required
def edit_recipe(request, id):
    c = Category.objects.all()
    r = Recipe.objects.get(id=id)

    user = request.user
    if r.user == user:
        return render(request, "recipes/new.html", {
            "recipe": r,
            "categories": c,
            "title": "Edit Recipe"
        })
    else:
        return HttpResponseRedirect(reverse("index"))

@csrf_exempt
@login_required
def post_recipe(request):
    user = request.user
    if request.method != "POST":
        return JsonResponse({"error": "POST request required."}, status=400)

    data = json.loads(request.body)
    title = data.get("title", "")

    if Recipe.objects.filter(title=title).exists():
        return JsonResponse({"error": "A recipe with this name already exists."}, status=400)
    image = data.get("image", "")
    category_name = data.get("category", "")
    difficulty = data.get("difficulty", "")
    cost = data.get("cost", "")
    time = data.get("time", "")
    ingredients = data.get("ingredients", "")
    description = data.get("description", "")
    preparation = data.get("preparation", "")
    tips = data.get("tips", "")

    category = Category.objects.get(name=category_name)

    r = Recipe(
        user = user,
        category = category,
        image = image,
        title = title,
        description = description,
        ingredients = ingredients,
        preparation = preparation,
        tips = tips,
        difficulty = difficulty,
        time = time,
        cost = cost
    )
    r.save()
    return JsonResponse({"message": "Post added successfully."}, status=201)

@csrf_exempt
@login_required
def save_edits(request, id):
    user = request.user
    if request.method != "POST":
        return JsonResponse({"error": "POST request required."}, status=400)

    data = json.loads(request.body)
    title = data.get("title", "")

    recipe = Recipe.objects.get(id=id)
    
    if recipe.title != title:
        if Recipe.objects.filter(title=title).exists():
            return JsonResponse({"error": "A recipe with this name already exists."}, status=400)
        else:
            recipe.title = title

    image = data.get("image", "")
    category_name = data.get("category", "")
    difficulty = data.get("difficulty", "")
    cost = data.get("cost", "")
    time = data.get("time", "")
    ingredients = data.get("ingredients", "")
    description = data.get("description", "")
    preparation = data.get("preparation", "")
    tips = data.get("tips", "")

    category = Category.objects.get(name=category_name)

    recipe.category = category
    recipe.image = image
    recipe.description = description
    recipe.ingredients = ingredients
    recipe.preparation = preparation
    recipe.tips = tips
    recipe.difficulty = difficulty
    recipe.time = time
    recipe.cost = cost
    recipe.save()
    return JsonResponse({"message": "Recipe successfully edited."}, status=201)

def recipe_page(request, id):
    r = Recipe.objects.get(id=id)
    user = request.user
    status = ""
    if user.is_authenticated:
        if Saved.objects.filter(user=user, recipe=r).exists():
            status = "Unsave"
        else:
            status = "Save"

    rates = 0
    reviews = Rating.objects.filter(recipe=r)
    for review in reviews:
        rates += review.value
    
    if (reviews.count() == 0):
        average = 0
    else:
        average = rates / reviews.count()

    return render(request, "recipes/recipe.html", {
        "recipe": r,
        "status": status,
        "rating": average,
    })

@login_required
@csrf_exempt
def save_recipe(request, action):
    user = request.user
    if request.method != "POST":
        return JsonResponse({"error": "POST request required."}, status=400)

    data = json.loads(request.body)
    title = data.get("title", "")

    r = Recipe.objects.get(title=title)

    if  Saved.objects.filter(user=user).exists():
        s = Saved.objects.get(user=user)
    else:
        s = Saved(user=user)
        s.save()

    if action == "save":
        s.recipe.add(r)
        return JsonResponse({"status": "Unsave"}, status=201)
    else:
        s.recipe.remove(r)
        return JsonResponse({"status": "Save"}, status=201)

@login_required
@csrf_exempt
def rate_recipe(request, recipe):
    user = request.user
    if request.method != "POST":
        return JsonResponse({"error": "POST request required."}, status=400)
    
    data = json.loads(request.body)
    value = data.get("rate", "")
    r = Recipe.objects.get(title=recipe)

    if Rating.objects.filter(user=user, recipe=r).exists():
        rating = Rating.objects.get(user=user, recipe=r)
        rating.value = value
        rating.save()
        return JsonResponse({"message": "Recipe successfully edited"}, status=201)
    else:
        rating = Rating(user=user, recipe=r, value=value)
        rating.save()
        return JsonResponse({"message": "Recipe successfully rated"}, status=201)

@login_required
def get_user_rate(request, recipe):
    user = request.user
    r = Recipe.objects.get(title=recipe)

    if Rating.objects.filter(user=user, recipe=r).exists():
        user_review = Rating.objects.get(user=user, recipe=r)
        return JsonResponse({"value": user_review.value}, status=201)
    else:
        return JsonResponse({"value": 0}, status=201)