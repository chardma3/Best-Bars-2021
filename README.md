<h1>Best Bars 2021</h1>

<span id="Bestbars"></span>

![Multi Device Website Mockup Generator](readme_img/mockup.png)

Best Bars 2021 is a web application designed for those that love the nightlife! Bars, cocktails, service, decor, 
music and vibes is all important and at Best Bars 2021 and we want users to contribute reviews detailing the impressive Bars that we should know about.

Everyone is welcome to create an account and add their reviews. If the user has an account, they can add, edit and delete their reviews.

The website is responsive and available on desktop, laptops, tablets and mobile devices.

**[The live project can be viewed here.](https://best-bars.herokuapp.com/)**

---

## Index 

- <a href="#ux">1. User experience (UX)</a>
  - <a href="#ux-goals">1.1. Project goals</a>
  - <a href="#ux-stories">1.2 User stories</a>
  - <a href="#ux-design">1.3 Design</a>
  - <a href="#ux-wireframes">1.4 Wireframes</a>
- <a href="#db-schema">2. Database Schema</a>
- <a href="#features">3. Features</a>
- <a href="#technologies">4. Technologies used</a>
- <a href="#testing">5. Testing</a>
- <a href="#deployment">6. Deployment</a>
- <a href="#credits">7. Credits</a>

<span id="ux"></span>

## User Experience (UX)

<span id="ux-goals"></span>

### Project goals 

- Making a full-stack site that allows users to manage a common dataset about a particular domain. 
- Making a full-stack site that uses HTML, CSS, JavaScript, Python+Flask and MongoDB. 
- Creating a website that is simple to understand and easy to navigate.
- The users of the website can make use of CRUD (create, read, update and delete) for the reviews. 
This web application is designed for those who wish to learn about bars in their current area as well as share reviews about their experiences at bars they have visited.

The application is aimed at:

- people who like visting bars for an experience
- people who work in the industry

Users of the application are able to create an account and submit reviews of bars that they think deserve attention. They are also able to edit and delete their reviews as they see fit.

<span id="ux-stories"></span>

### User Stories

#### First Time Visitor Goals

- As a **first time visitor**, I want to understand the main purpose of the site
- As a **first time visitor**, I want to be able to easily navigate through the site
- As a **first time visitor**, I want to be able to find bars in my current area
- As a **first time visitor**, I want to be able to sign up for an account to add my own reviews
- As a **first time visitor**, I want to be able to contact the site owner

#### Registered User Goals

- As a **registered user**, I want to be able to easily login and logout of my account
- As a **registered user**, I want to be able to add reviews to the site
- As a **registered user**, I want to be able to edit any reviews that I have written
- As a **registered user**, I want to be able to delete any reviews that I have written

#### Site Owner Goals

- As a **site owner**, I want to provide the user with a description about the purpose of the site
- As a **site owner**, I want to include a navigation bar to allow users to easily and intuitively navigate to other pages on the site
- As a **site owner**, I want to provide the user with access to reviews without having to create an account
- As a **site owner**, I want to allow the user to easily sign up for an account to allow them to write their own reviews
- As a **site owner**, I want to allow the user to easily edit and delete any reviews thay've added to the site
- As a **site owner**, I want all visitors and registered users to be able to easily contact me through email or social media platforms

<span id="ux-design"></span>
      
-   ### Design
    -   #### Colour Scheme
        -   The main colors are black and white with bold and exciting colors of yellow/orange and purple/pink. I found these just from experimenting. I'm a fan of bold and exciting.
    -   #### Typography
        -   The font I used for the header is Anton from Google Fonts as I felt it was a minimal, yet strong and stiking font that feels very magazine-ish. For the other text I used Raleway from Google fonts with a back up of Sans Serif.
    -   #### Imagery
        -   The images featured on the site are cocktails with exciting garnishing, elegant glasswear are well styled and lit, with vibrant colors and elegant content. Credits can be found below

    -   #### Icons
        -   In the project, icons are used that are provided by [Font Awesome](https://fontawesome.com/). The Icons that are used have functional purposes such as the hamburger menu and social media icons. 
        
<span id="ux-wireframes"></span>

*   ### Wireframes
    -Wireframes were done in photoshop. As I focus very much on images, fonts and colors I find that photoshop is more useful for me when wireframing. The wireframes evolved and served as a testing ground for new layouts and features. 
    The main template layout consists of a header, navbar and the footer, and is used across the site.
    Wireframes for this project may be viewed in a seperate file [here](wireframes.md).
   
<span id="db-schema"></span>

## Database Schema

MongoDB Atlas was the cloud database service used to create and store the database collections for this project:

### Dictionary Collection

| Key | Value |
| :---: | :---: |
| _id: | ObjectId("unique_id") |
| bar-name: | "string" |
| review: | "string" |
| fav_drink: | "string" |
| location: | "string" |
| added_by: | "string" |

### User Profile Collection

| Key | Value |
| :---: | :---: |
| _id: | ObjectId("unique_id") |
| username: | "string" |
| email: | "string" |
| password: | "string" |

<span id="features"></span>

## Features

-   Responsive on different device sizes
-   an easy to use navigation bar located at the top of the page, available on all pages and collapses to an icon on mobile devices
-   A home page with a desciption that explains the purpose of the site
-   A reviews page
-   Add, Edit and Delete review functionality
-   Login, Log Out and register functionality
-   A footer located on every page with links to social media accounts and an email link

**Features Left to Implement**  
* In the future I would like to implement a recipe form for users to add recipes of cocktails
* An admin page could be advantageous so that one can administate via the application rather than go into Mongo DB

<span id="technologies"></span>

## Technologies Used

### Languages Used

-   [HTML5](https://en.wikipedia.org/wiki/HTML5)
-   [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
-   [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
-   [Python](https://www.python.org/)

### Frameworks, Libraries & Programs Used

1. [Bootstrap 5.0:](https://getbootstrap.com/)
    - Bootstrap was used to assist with the responsiveness and styling of the website.
1. [Google Fonts:](https://fonts.google.com/)
    - Google fonts were used to import the heading font of Pacifico cursive and Trebuchet.
1. [jQuery:](https://jquery.com/)
    - To make Bootstrap work and to write Javascript more quickly.
1. [Git](https://git-scm.com/)
    - Git was used for version control by using the Gitpod terminal to commit to Git and Push to GitHub.
1. [GitHub:](https://github.com/)
    - GitHub is used to store the projects code after being pushed from Git.
1. [Photoshop:](https://www.adobe.com/ie/products/photoshop.html)
    - Photoshop was used for manipulating images, creating favicon and creating the wireframes during the design process.
1. [Heroku](https://www.heroku.com/)
   - Heroku is a cloud platform that was used to deploy and run the application from the GitHub repository
1. [Flask](https://flask.palletsprojects.com/en/1.1.x/)
   - Flask was the microframework use to build the application
1. [Font Awesome](https://fontawesome.com/)
   - Font Awesome was used to add various icons throughout the site
1. [MongoDB](https://www.mongodb.com/)
   - MongoDB Atlas is a cloud database service used to create and store the database collections for the application

   ### Dependencies

1. [autopep8](https://pypi.org/project/autopep8/)
   - A tool that automatically formats Python code to conform to the PEP 8 style guide
1. [click](https://palletsprojects.com/p/click/)
   - Composable command line interface toolkit
1. [dnspython](https://www.dnspython.org/)
   - A DNS toolkit for Python
1. [Flask-PyMongo](https://flask-pymongo.readthedocs.io/en/latest/)
   - PyMongo support for Flask applications
1. [itsdangerous](https://palletsprojects.com/p/itsdangerous/)
   - Various helpers to pass data to untrusted environments and back
1. [Jinja2](https://palletsprojects.com/p/jinja/)
   - Templating language for Python
1. [MarkupSafe](https://palletsprojects.com/p/markupsafe/)
   - Safely add untrusted strings to HTML/XML markup
1. [pymongo](https://pypi.org/project/pymongo/)
   - Python driver for MongoDB
1. [Werkzeug](https://werkzeug.palletsprojects.com/en/1.0.x/)
   - A comprehensive WSGI web applications library

<span id="deployment"></span>

## Deployment

### Heroku

This project is hosted on Heroku - A cloud platform service that enables developers to build, run and operate applications entirely in the cloud:

- Before creating a Heroku app, open the repository in Github and create a requirements file that lists all the applications and dependencies required to run the application: ```pip3 freeze --local > requirements.txt```
- Create a Heroku specific file called a Procfile - this is what Heroku looks for to know which file runs the app and how to run it: ```echo web: python run.py > Procfile```
- Open [Heroku](www.heroku.com) and login to your account or sign up for an account if you don't already have one
- Open the dashboard and select **"New"** to create a new app
- Name the app and set the region to Europe
- Open the settings tab and open **"Reveal Config Vars"**
- Add the environment variables from the **env.py** file:
  - **KEY:** IP | **VALUE:** 0.0.0.0
  - **KEY:** PORT | **VALUE:** 5000
  - **KEY:** SECRET_KEY | **VALUE:** YOUR_SECRET_KEY
  - **KEY:** MONGO_URI | **VALUE:** YOUR_MONGO_URI
  - **KEY:** MONGO_DBNAME | **VALUE:** YOUR_MONGO_DBNAME
- To deploy the app from GitHub, open the deploy tab and change the deployment method to GitHub
- Connect to your GitHub account and search for the name of the repository to connect to
- Once connected, **"Enable Automatic Deployments"** and select the **"Master"** or **"Main"** branch to deploy
- Click the **"Deploy Branch"** button to deploy the app to Heroku

There are no differences between the deployed version and the developement version.

## Local Deployment

1. Navigate to the GitHub Repository.
2. Click the Code drop down menu.
3. Either Download the ZIP file, unpackage locally and open with IDE (This route ends here) OR Copy Git URL from the HTTPS dialogue box.
4. Open your developement editor of choice and open a terminal window in a directory of your choice.
5. Use the git clone command in terminal followed by the copied git URL.
6. A clone of the project will be created locally on your machine.

Once the project has been loaded into an IDE of choice, run the following command in the shell to install all the required packages: pip install -r requirements.txt

### Cloning the Repository

To clone the repository on GitHub and make a local copy on your computer, follow these steps:

- Open GitHub and locate the GitHub repository: [https://chardma3.github.io/Best-Bars-2021](https://chardma3.github.io/Best-Bars-2021)
- Under the repository name, click "Code" and copy the link to clone the repository using "HTTPS"
- After copying the link, open terminal on your computer - this step can also be done in the terminal in your preferred IDE
- Change the current working directory to the location where you want the cloned directory to be saved
- Type ```git clone```, and then paste the URL: [https://github.com/chardma3/Best-Bars-2021.git](https://github.com/chardma3/Best-Bars-2021.git)
- Press Enter to create a local clone
- To then run the repository locally, install the required dependencies from the **requirements.txt** file: ```pip3 install requirements.txt```
- Run the app from your local IDE using the following command: ```python3 app.py```

<span id="testing"></span>

# Testing
The testing process can be found [here](TESTING.md).

### Testing tools Used

* HTML
code is validated through [W3 validator](https://validator.w3.org/).

* CSS
code is validated through [W3 Jigsaw](https://jigsaw.w3.org/css-validator/).

* JavaScript
code is validated through [JS Hint](https://jshint.com/).

* Python
code is validated through [PEP8](http://pep8online.com/).

* Chrome Devtools
is used to detect problems and test responsiveness  [CHROME DEVTOOLS](https://developers.google.com/web/tools/chrome-devtools/open).

<span id="credits"></span>

## Credits

### Media

Images used on the site have been sourced from liquor.com and delicious.com.

### Content

-   Concept, design, coding and text has been created by myself. Wikipedia has also been used for extra research. 

## Coding Sources

* Videos from Code Institute

## Acknowledgments

* Huge thanks to the gang at Code Institute Tutor Support and student Care for all their guidance, patience and support.

<a href="#bestbars">Back to top!</a>
