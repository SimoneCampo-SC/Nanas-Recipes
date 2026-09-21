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
- Responsive user interface built with HTML, CSS and JavaScript

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

From the repository root:

```bash
python3 manage.py runserver
