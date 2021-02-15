<h1>Best Bars 2021</h1>

[The live project can be viewed here.](https://best-bars.herokuapp.com/)

Best Bars 2021 is a web application designed for those that love the nightlife! Bars, cocktails, service, decor, 
music and vibes is all important and at Best Bars 2021 and we want users to contribute reviews detailing the impressive Bars that we should know about.
The website is responsive and available on desktop, laptops, tablets and mobile devices.

<h2 align="center"><img src="https://github.com/chardma3/SummerMemories/blob/master/assets/images/Mockup.jpg"></h2>


## User Experience (UX)
This web application is designed for those who wish to learn about bars in their current area as well as share reviews 
themselves about their experiences at bars they have visited

The application is aimed at:

-people who like visting bars for an experience
-people who work in the industry

Users of the application are able to create an account and submit reviews of bars that they think deserve attention. They are also able to edita nd delete their reviews as they see fit.

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

      
-   ### Design
    -   #### Colour Scheme
        -   The main colors are black and white with bold and exciting colors of yellow/orange and purple/pink. I found these just from experimenting. I'm a fan of bold and exciting.
    -   #### Typography
        -   The font I used for the header is Anton from Google Fonts as I felt it was a minimal, yet strong and stiking font that feels very magazine-ish. For the other text I used Raleway from Google fonts with a back up of Sans Serif.
    -   #### Imagery
        -   The images featured on the site are cocktails with exciting garnishing, elegant glasswear are well styled and lit, with vibrant colors and elegant content. Credits can be found below
        
*   ### Wireframe
    -Wireframes were done in photoshop. As I focus very much on images, fonts and colors I find that photoshop is more useful for me when wireframing. The wireframes evolved and served as a testing ground for new layouts and features. 
    The main template layout consists of a header, navbar and the footer, and is used across the site.
    The link to the pdf file with wireframes for desktop, tablet and mobile devices can be viewed here - [View](https://github.com/chardma3/SummerMemories/tree/master/assets/wireframes)

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

## Features

-   Responsive on different device sizes
-   an easy to use navigation bar located at the top of the page, available on all pages and collapses to an icon on mobile devices
-   A home page with a desciption that explains the purpose of the site
-   A reviews page
-   Add, Edit and Delete review functionality
-   Login, Log Out and register functionality
-   A footer located on every page with links to social media accounts and an email link

**Features Left to Implement**  
*In the future I would like to implement a recipe form for users to add recipes of cocktails


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
1. [EmailJS](https://www.emailjs.com/)
    - EmailJS was used to add an email service to the form in the contact template
1. [Flask](https://flask.palletsprojects.com/en/1.1.x/)
   - Flask was the microframework use to build the application
1. [Font Awesome](https://fontawesome.com/)
   - Font Awesome was used to add various icons throughout the site
1. [MongoDB](https://www.mongodb.com/)
   - MongoDB Atlas is a cloud database service used to create and store the database collections for the application
1. [VS Code](https://code.visualstudio.com/)
   - Visual Studio Code was the IDE used to code the project

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

## Testing

The W3C Markup Validator and W3C CSS Validator Services were used to validate every page of the project to ensure there were no syntax errors in the project.

-   [W3C Markup Validator](https://validator.w3.org/) - To test for errors in html
-   [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) - To test for errors in css
-   [GTmetrix](https://gtmetrix.com/) - To test website loading times
-   [JSHint](https://jshint.com/) - To test website for JS errors

### Bugs Found
-   ...

    
### Automated testing
-   Automated testing has been done and it conforms to screen readers and is error free

### Testing User Stories from User Experience (UX) Section

The site was tested manually and fulfills its goals by providing an easy and straightforward way for users to achieve their goals.

1 Buttons 
-  The buttons provided allow the user to tailor the game to suit their needs. These are: a sound button to toggle the sound on and off, an instructions button which acts as an accordian and shows the instructions for the game, and a restart button so that the user can retsart if they got off to a bad start and would like to start again rather than waiting for the timer to run out.

2 Game Info Section 
-  The game info section provides the time ticking down from 80 seconds and a flips tally which shows how many times you have flipped a card.

The website is responsive and diplays the four by four grid on desktop screen and tablet sized devices and displays two cards wide in mobile view.

### Further Testing

-   The Website was tested on Google Chrome, Internet Explorer, Microsoft Edge and Safari browsers.
-   The website was viewed on a variety of devices such as Desktop, Laptop, iPhone7, iPhone 8 & iPhoneX via Google Chrome developer Tools.
-   All buttons, cards and other functions were tested to ensure they work.
-   Friends and family were asked to look at the site and give feedback on their user experience with the site in regard to color, sizes, and font styles.

## Deployment

### GitHub Pages

The site is hosted on Github pages.

This project has been deployed to Github by doing the following:
1. Login to GitHub and locate the required [GitHub Repository](https://github.com/chardma3/SummerMemories)
2. At the top of the Repository locate the "Settings" Button on the menu.
3. Scroll down the Settings page until you locate the "GitHub Pages" Section.
4. Under "Source", click the dropdown called "None" and select "Master Branch".
5. The page will automatically refresh.
6. Scroll back down through the page to locate the now published site [link](https://chardma3.github.io/SummerMemories/) in the "GitHub Pages" section.

There are no differences between the deployed version and the developement version.

In order to run the code for the project locally use the link provided to navigate to the project repository and the clone the project. 


## Credits

### Media

Images used on the site have been sourced from liquor.com and delicious.com

### Content

-   Concept, design, coding and text has been created by myself. Wikipedia has also been used for extra research 

### Acknowledgements

-  Thanks to my mentor for advising me and helping me make the project better as well as the CI tutors who have helped me with many a problem