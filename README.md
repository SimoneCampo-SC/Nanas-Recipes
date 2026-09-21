# Nana's Recipes

A full-stack recipe-sharing web application built with Django and JavaScript.

Users can create and manage recipes, search published content, rate recipes and save favourites to their personal collection.

## Features

- User registration and authentication
- Create and edit recipes
- Recipe categories and difficulty levels
- Search with case-insensitive matching
- Five-star recipe rating system
- Save recipes to a personal collection
- View recipes published by the current user
- Dynamic page content based on authentication and ownership
- User interface built with HTML, CSS and JavaScript

## Technical overview

The application uses Django for the backend and data layer, with JavaScript used for interactive frontend behaviour.

The data model separates users, recipes, categories and ratings, while shared Django templates are used across multiple application states to reduce duplication.

The project also includes validation around recipe creation and editing, ownership-aware controls, and dynamically generated views for saved and published recipes.

## Technologies

- Python
- Django
- JavaScript
- HTML
- CSS
- SQLite

## Running the project

Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install the project dependencies:

```bash
python3 -m pip install -r requirements.txt
```

Set a local Django secret key:

```bash
export DJANGO_SECRET_KEY="local-development-key"
```

Apply the database migrations:

```bash
python3 manage.py migrate
```

Start the development server:

```bash
python3 manage.py runserver
```

Then open the local development URL provided by Django and navigate to:

```text
/nanarecipes/
```

## Project context

This is an earlier full-stack project preserved as part of my public engineering portfolio. It demonstrates my work with backend development, relational data modelling, frontend interaction and end-to-end web application design.
