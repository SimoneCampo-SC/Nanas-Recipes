from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [ 
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("new", views.new_recipe, name="new-recipe"),
    path("edit/<int:id>", views.edit_recipe, name="edit-recipe"),
    path("myrecipe", views.my_recipes, name="my-recipes"),
    path("<int:id>", views.recipe_page, name="recipe-page"),
    path("saved", views.saved_recipes, name="saved-recipes"),
    path("search/", views.show_search, name="search"),

    #API 
    path("postRecipe", views.post_recipe, name="post-recipe"),
    path("edit/editRecipe/<int:id>", views.save_edits, name="save-edits"),
    path("saveRecipe/<str:action>", views.save_recipe, name="save-recipe"),
    path("raterecipe/<str:recipe>", views.rate_recipe, name="rate-recipe"),
    path("personalrate/<str:recipe>", views.get_user_rate, name="personal-rate")
]