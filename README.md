# CS50x_project
#### Video Demo: https://www.youtube.com/watch?v=zxea0cXaqDA
#### Description:

Hi my final project is about a site to create and manage passwords. Sometimes it happens to all of us that we forget the password of our accounts on sites or social networks, etc., or our access to them is cut off. The project I defined largely avoids these problems.
Now let's go to the explanation of the parts of the project:
Most of the project files were created by Django and I only edited a few of them.

Most of the project files were created by Django and I only edited a few of them.
Let's start with the "password_generator" directory.
The file "__init__.py" indicates that this is a Python directory.
The files "asgi.py" and "wsgi.py" were created by Django and I have not made any changes to them.
In the "settings.py" file on line 41, I added the "generator" app to the Django settings. I have also added lines 122 to line 125 to load static files.
In the "urls.py" file, I have defined lines of 24 to 30 URLs required by the site.

After checking the "password_generator" directory, we go to the "generator" directory.
The "migrations" directory was created by Django and is related to database work.
And the "__init__.py" file, as mentioned, indicates that this directory is related to Python.
The "admin.py", "apps.py" and "tests.py" files were created by Django and I have not made any changes to them.
In the "models.py" file, in lines 5 to 8, I defined the password models for storage in the database.
In the "views.py" file, I have defined the necessary views of the project, which I will discuss below.
I have imported the required functions in the first 10 lines. Lines 13 to 17 first indicate whether the user has registered or not and then render the "index.html" template.
In lines 20 to 37, I have defined the user login form.
I have also defined the registration form in lines 40 to 49.
In lines 52 to 69, I wrote the registration so that if the request method is mail, it will save the user in the database and then log in with it and be redirected to the home page. And if the request method is get, render the "signup.html" template with the registration form.
In lines 73 to 135, I wrote the main part of the site, ie generating the password, which first generates the password with the appropriate algorithm, then if the user has registered, stores the password for him in the database, and finally the "password.html" template. Renders with the generated password.
In lines 141 to 144, I have written the password view, which the user must have registered for this section. First we read the password code from the database, then the "mypass.html" template renders the passwords.
Finally, in lines 147 to 150, I have written the possibility of deleting passwords by the user. Which first receives the desired password ID and then clears the password from the database and reloads the page.

In the last part of this section, we take a look at the "templates" directory, where I put the "generator" directory.
And in this directory I have put all the templates of the site.
I wrote the templates using Bootstrap and it is almost responsive. At the head of the templates, I entered the required titles and links, and in the first part, I put the navigation body, and then I put the content, which I coded separately for the phone and laptop.

Going back and going to the "static" directory. This directory contains three directories: "css", "js" and "pictures", which contain CSS and JavaScript files and images, respectively, which are used to better display the templates.

Then we go back and see the file "db.sqlite3" which was created by Django and is the database of this project.
Next we have the file "manage.py" which was created by Django and I have not changed it.
Finally, we have the "requirements.txt" file, which shows the packages that must be installed for this project.


This project is not perfect and thank you for helping me improve it :)
