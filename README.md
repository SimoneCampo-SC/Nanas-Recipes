# Nanas-Recipes
## Project Background
One of the cultural pillars of every State is their cuisine and, in a world that promotes diversity and inclusion, I decided to present a website called “Nana’s Recipes”, where users can publish, rate, and save recipes. 
Functionalities
In this paragraph, the website functionalities are listed in a form of bullet point list:
1.	Registration Page
Users can register to the website by inserting their username, email and password.

2.	Add Recipe: authenticated users can publish a new recipe. Each recipe has the following data fields:
o	Name: Compulsory field,
o	URL image: Non-Compulsory field, 
o	Category: Compulsory field – [Sides, Main Course and Desserts] hardcoded in the database,
o	Difficulty: Compulsory field – how difficult is to prepare the recipe [Easy, Medium, Difficult],
o	Cost: Non-Compulsory field – How expensive the recipe is [Low, Medium, High],
o	Prep. Time: Compulsory Field – How long it takes to prepare the recipe in minutes, 
o	Ingredients: Compulsory Field,
o	Description: Compulsory Field,
o	Preparation: Compulsory Field,
o	Tips: Non-Compulsory Field.

3.	Recipe Page: Can be viewed by both authenticated and non-authenticated users and it shows all the information inserted by the users. Additionally, it shows:
o	Edit Button: If the user is the one who published the recipe.
o	Rating: Accessed by both authenticated and non-authenticated users and it shows the average rating that the recipe received [up to five].
o	Stars: Accessible to authenticated users who have not published that recipe.
o	Save: Accessible to all the authenticated users, allow them to save the recipes inside a section called “Saved Recipes”.

4.	Edit Page: Accessed by the edit button and it allows the user to edit its own recipe. It has an important behaviour:
o	An error is thrown if user replace the name with another one that already exists into the database.
o	The fields are filled with the existing information.

5.	Rating System: Authenticated users can rate a recipe with the stars: 1 to 5.


6.	Save Recipes: Accessed by authenticated users and it displays all the recipes saved by the user. It follows these guidelines:
o	Each recipe is recognised by its name and image,
o	Recipes are sorted in alphabetical order,
o	Recipes are grouped by their category, starting from Sides to Desserts,
o	The category is not displayed if there are no recipes,
o	Recipes can be scrolled, and their page is loaded when selected.

7.	My Recipes: Accessed by authenticated users and it displays all the recipes published by the user. It follows the same guidelines as the Save Recipe page.

8.	Home Page: Accessed by both authenticated and non-authenticated users and it displays all the published recipes. It follows the same guidelines as the Save Recipe page.

9.	Search Bar: Can be used by both authenticate and non-authenticated users who wants to search for a specific recipe. It has the following behaviour: 
o	Search button does not work when the text bar is empty,
o	If the user’s string matches with a recipe’s name, it uploads that recipe page.
o	If the user’s string does not match with a recipe’s name but it is contained in the title of the recipe, the correlated results are displayed.
o	If the user’s string is neither a recipe’s name, nor contained within one of them, an error message is displayed.
o	To improve the results, the user’s string is processed without considering capital letter. Thus, the research is not case sensitive.
o	The results produced follow the same guidelines as the Save Recipe page.

Distinctiveness and Complexity 
I strongly believe that this project fully satisfies the distinctiveness and complexity requirements. Indeed, the database is composed by four different models: one for the user, one for the recipe, one for the category and the last one for the ratings. Additionally, the website features have been thought and designed following the topics and the knowledge acquired during the entire course. In this respect, the project makes use of HTML/CSS, JavaScript and Python, the pages are created dynamically and their content changes according to the user that is using the website. 
Regarding the structure, all the HTML pages are extended by a layout HTML page and the application has been designed in a such way that a single HTML is used in multiple scenarios. For example, the index.html file is used to display the home, saved recipes and my recipes page and the new.html file is used to both publish and to edit a recipe. As far as Python concerned, repetitive actions have been collected in a single function, which is called by other requested functions. E.g. index_view function.
Hard work has been made on the styling and on the CSS. In this respect, the user conducted a thorough research finalised at producing a qualitative aesthetic to the web page. UX/UI principles have been applied to make all the interaction easy to understand and to perform – an example is the star rating system. 
The project has been created using Django and the App is called ‘recipes’. In addition to all the files that come with the Django app, the following project has 6 HTML, 1 CSS and 2 JS files.
How to run the Django Application.
1.	Go inside the terminal
2.	Navigate into the Capstone directory
3.	Run the command ‘python3 manage.py runserver’.
4.	Open the produced link 
5.	Add the /nanarecipes to the URL – e.g. ‘http://127.0.0.1:8000/nanarecipes/’


