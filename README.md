# Report On Any Discrimination


[Landing Image](static/files/wireframes/landing_image.png)
### [Live page](https://hidden-gems-cgpalmer91.herokuapp.com/)





___

## Contents
+ <a href="#rationale">Rationale</a>
    - <a href="#inspiration">Inspiration</a>
+ <a href="#UX">UX</a> 
   - <a href="#fivePlanes">5 planes of UX</a>
   - <a href="#userStories">User Stories</a>
+ <a href="#features">Features</a>
   - <a href="#existingFeatures">Existing Features</a>
   - <a href="#featuresLeftToImplement">Features left To Implement</a>
+ <a href="#dataIntegration">Data Integration</a>
+ <a href="#defensiveFeatures">Defensive Features</a>
+ <a href="#technologiesUsed">Technologies Used</a>
+ <a href="#testing">Testing</a>
+ <a href="#responsiveDesign">Responsive design</a>
+ <a href="#deployment">Deployment</a>
   - <a href="#deploymentLive">Deployment Live</a>
   - <a href="#deploymentLocal">Deployment Local</a>
+ <a href="#credit">Credit</a>
   - <a href="#tutorials">Tutorials</a>
   - <a href="#media">Media</a>
   - <a href="#acknowledgements">Acknowledgements</a>
+ <a href="#project">Project Evaluation</a>
   - <a href="#improvements">Improvements</a>






___

<span id="rationale"></span>
## Rationale

## Project proposal

This project aims to give users an opportunity to display unique photographs of the world, around their room. 
Users will be able to select from a wide range of my own personal photographs and purchase them on quality paper,
a variety of canvas sizes or frames. In addition, users can use their own unique photographs and have them printed in 
the same way!

There are many sites that offer this but here is where Hidden Gems is different. Each photo will have a blog attached
to it explaining the story behind the photo. This personal touch adds a third dimension to the art and gives users
a starting point to discuss their choices with guests. 

___

<span id="inspiration"></span>

## Inspiration

#### Requesting information


#### Design



___

<span id="UX"></span>
## UX

5 planes of UX

### Strategy


Design
Simple and intuitive site that is easy enough for anyone to use, from mobile or desktop. No special features needed like Bluetooth or Account being made.  

Business
Make it easy for people to to buy photographs digitally or physically, with the option of having the in a frame, or printer to calendars or canvases. 

Having a website interface is the most accessible design to reach the widest net of clients. This means that users of all ages are more likely to be comfortable on the platform. An app may be the more popular choice amongst younger user whereas the older generation are accustomed to websites – which are not subject to such quick change. In addition, whilst the younger generation may prefer an app, they are fully capable of searching for a website. The capabilities of using an app, or a smartphone over a computer, may be beyond the abilities of some demographics.
In general, a website is much more accessible for those with accessibility issues, especially as more tools continue to come out to aid the process. Those with sight or mobility issues can still get the full experience through a website on any device.
The site has been designed as mobile-first, which is particularly important for this project. Photos are becoming increasingly popular on mobile, as the cameras continue to get better. Fewer people have films cameras and it is now common practise to have digital photos printed instead.
With a mobile-first design, the website is easy to use straight from your mobile – the place where most of the user’s excellent photos are stored. This has several benefits:
1. The user does not need to transfer photos between devices to order.
2. The user can store the photos for a later time by uploading them from your mobile. You can then finish the order from any device. 
3. The user can complete a transaction from start to finish on a mobile, means fewer users will be put of by the complexity of device switching and those who are impulse buying are satisfied quickly. 
4. If the user wants to buy a photo have on their social media account, they can download it to their phone – which is the most likely place for them to use social media. 
Unlike shops where users print their photographs, a user does not need to be familiar with Bluetooth or smartphones in order to get your photos. This, again, widens the demographic of clients. 
Giving a user the option to download digitally or print a photograph covers all scenarios in which a user would like to purchase a photograph. For example:
Table – scenario - action
User wants a photo to use on digital products. Downloads digitally.
User wants a photo to put in an existing frame. User have a photo delivered to the door. (Currently restricted to 1 size of 7” x 5”). 
User has a photo but would like a frames. User buys a frame or canvas on the same website. 
User wants to buy the photo and wants it in a container. User buys a frame, canvas or calendar and gets the photos printed on for free. 
User wants to have their photo printer on a canvas, calendar or in a frame. (Photo will be printed to size automatically to match the container.) User uploads their photo and links it to a product. 

I am aware that we should offer to print all photos in a variety of sizes and that is a future feature. 
Strategy for the business
There will be an admin section which allows admin staff to add, remove, edit products, and read orders to be fulfilled. There is also an admin link to the full Django admin site, which is only accessible to the superuser. I separated the two for a couple of reasons: 
The staff structure at the business may want people to add products but not at able to access customer details. In addition, they may want some staff to see the most recent orders but not have access to them all. Finally, this separation can prevent some staff from editing special offers and other finance related possibilities.
This all allows for full customisation of delegation tasks which allows managers and employees to smoothly work together throughout the day. 
The forms are validated to ensure that all the information that is needed for the website to work is provided when adding or editing products. 

### Scope
<span id="userStories"></span> 
### User Stories

#### First-time user


#### Returning user



#### User as a charity or researcher (professional user)


Feature set 
Current features
Order photographs or containers – calendar, frames or canvas. Photographs come at a default size of 7” x 5”. 
Be able to upload their own photographs
Download their purchases to their computer. 
Search for products by name, sku, description.
When you purchase a calendar, frame or canvas, the user can choose to have a picture printed to the product. 
To have an account that remembers their details.

Future features
Picture resolution validation to make sure the photo is high enough quality.
A product preview of the photo within the frame or on the canvas/ calendar. 
A blog to explain the story behind each photo as a unique feature.
Users can upload their own photos to be bought and receive a percentage of the profits. 

Business objectives
For people to use us to purchase frames, calendars and canvases.
For people to upload their photos and know that the picture will be delivered to their door at the correct size for the containers.
Content required:
Profile page with details about the user.
Filters, categories and search to refine product search and speed up the user experience. 
Products with extended details
A basket to handle the purchases
A checkout to process purchases and payments.
Reviews about each product available to create, edit, delete and read. 
Interaction design

Navbar	
I have designed the navbar to read top-to-bottom of importance for mobile. On the mobile, I have attempted to space out the important parts so the user associated certain areas of the website with certain functions. 
I have broken the nav down into two sections. Account and its accessories, including the basket, and the product menu. For both mobile and desktop, the account links are on top and the products nav are on the bottom. I have also included a different dropdown on the mobile, with a different icon to differentiate between the menus.
I decided to keep the basket icon visible to users at all times. There is a flashing animation that occurs when a new product is added to the basket and, therefore, it would be redundant if it was hidden on mobile. It also keeps a running total for the basket sub-total so the user is aware of how much they are spending.
Mobile specific:
The account dropdown contains linked to the ‘profile, admin, login/logout and register’ pages depending on your status. The hierarchy is that useful links for profile come first, then login/logout, then register. This is because I believe those are visiting that part of the site are returning customers. Most who will sign up, will do it from the checkout link when making a purchase. 
For the product menu, I have chosen this order: Home, All products, special offers, photograph, frames & canvases. I put the special offers near to the top to entice the users and the frames at the bottom as the main selling point of the website is the photographs. Within each category are the sub-categories, which as this point are random but could change with popularity in orders. 


Desktop specific:
With the desktop, I have the account on the left and the basket on the right as before. I have moved the search bar to be in the middle of the product links as a way of balancing the links. 
It may be argued that the “All products” and “Special offers” should be on the left of the search bar as important reads from left to right. However, I have placed the “Special offers” underneath the basket, so that it is continuously seen every time a use is drawn to the basket’s “added product” animation. 
Equally, I wanted the main products near to the search bar so should a user not find what they want in the search bar, the bulk of the filters are directly next to the search bar. It is my hope that the user will then start to look through “Photographs” and “Frames & Canvases” for the products they would like. 
Finally, when the mouse hovers over any of the categories on the products bar, all of the menu opens. This serves as a reminder that there is lots to choose from and explore. The user can traverse across the sub-categories, without the menu hiding itself, providing a satisfying experience. 
Other interaction design:
All of the actions a user can take to personalise and modify their experience takes place within the profile page. This is separate from the main part of the website. Although, the user can still access their uploaded photos from the products detail pages, which makes a more intuitive experience for the user. 

Full list of features
Breakdown the apps and pages
Footer with email

### Skeleton design
Wireframes

Whilst this isn't an exhaustive document of every page on each device, it showcases that there is responsive design within the site. These particular images focus on three main
breakpoints - small, medium, extra large. Respectively, mobile, tablet, desktop.
[Image a website on different devices](static/files/testing/responsive_design.pdf)



### Surface design
Buttons
Action buttons also have a chevron pointing right, which is the logical symbol for “next”. All of the navigation buttons or cancel buttons have a chevron pointing left. This give the illusion that there is a certain way to navigate around the website, that discourages the users from click the browser “back” button. 

Typography
The same font is used across the website. The font-weight has been adjusted accordingly for the elements that need to stand out more or need to be more readable. For example: Where necessary, on the small “special offer” badge the font-weight is slightly less so it is more readable at a smaller font. 
I deliberately picked a clean, plain text font to maximise accessibility for the user. It does not use any cursive devices, nor is it italic. 

Colour Scheme
For my project, I knew which picture I wanted for my landing page. I decided that I would use a colour from the picture in order to replicate the feel of “nature” in colour scheme. As the majority of photographs on the site are animals or nature, I felt this fitted the website well. 
Once I had my base green colour, I used Canva https://www.canva.com/colors/color-wheel/ as a tool for developing secondary colours. Using the “Complementary” section, I chose to pick the secondary as the dark blue you see on the screen. I used the chromatic and found it suggested slightly lighter colours. However, the base green I chose, I decided to keep as it was darker and the “white” text had a better contrast ratio and was much easier to read.
Therefore, I made the hover functions, a slightly darker version of the two main “green” and “blue” colour.
I did experiment with the the other colours on the tetradict pdf. However, they broke they didn’t seem to properly fit with my design. Any fourth colour looked out of place and complex. Therefore, I stuck with a 3-colour system of white, green and blue.
Possibly the most important use of my colour scheme, aside from readability, is that I used it to reinforce the intuitive navigation and action around the website. All action buttons are blue. Whereas all cancel, navigation, delete buttons are green. As a general rule, the user will look for a blue button when they want to complete an action and will see a green button when they wish to return to a page. 
In addition, I use the colour scheme to have alert the user to the status of certain features. For example, when an item is added to the basket, the basket icon in the nav glows blue. This is so the user knows it has been added successfully and is drawn to their current total so far.
Another feature is the “profile” icon, which turns blue when a user is logged in. This is just visual feedback for the user, should they run into any issues. 

Balance in the design
I have made a significant effort to keep a balance on each webpage. Each has access to the header and foot, which are consistent in their sizes across the pages. Each page has a clear “section” in the middle that has an individual purpose. 
Cards
Each product has been placed on a card, with a photo at the top and text at the bottom. As these are white cards on a white background, I have added shadow to create a subtle 3D look.  The cards are consistent, with the images being of the same height and the text formatted in the same way below.
On the product details, cards are also used to keep the design consistent.

Horizontal rules
Horizontal rules have been used across the website to highlight headers and to separate items. For instance, they are used to separate reviews from each other or items in the basket.
I found these to be subtle and more flexible to use that a table. 











### Wireframes

Wireframes have been made using Balsamiq. 

[Wireframes](static/files/wireframes/ms3-wireframes-with-notes.pdf)

As there were not initial wireframes of the all the screen, I have added responsive images of all the pages in their final form.
[- responsive images of actual site.](static/files/wireframes/responsive-images-instead-of-WF.pdf)
___
<span id="features"></span>
## Features

<span id="existingFeatures"></span>
### Existing Features

<ins>Navbar</ins>

1. The navbar is responsive and had a traditional 'hamburger' icon on devices smaller than a laptop.
2. Each link will take the user to the designated pages.
3. There are links for the home page, login page, signup page, add report, search report - initially.
4. When logged in the links change to the following: - home page, dashboard, logout, add report, search report.
5. The logo will take the user back to the home page.

<ins>Footer</ins>

1. An email address which the user can contact the team by.
2. A telephone which the users can contact the team by.

<ins>Home </ins>

1. There is an update on how many reports have been collected altogether.
2. User can see the purpose of the website clearly.
3. There is information about the team behind the website.
4. There is a disclaimer giving advice on how to use the website. 

<ins>Dashboard </ins>

1. Has a welcome message with the users name.
2. A collapsible gives the user the three options:- Manage their own reports, search the database or add a report.
3. The search our database and add report links will take the user to the designated pages for adding reports and 
   searching the database.
4. The managing reports part of the collapsible is open.
5. The user can search their own reports by searching all, by location or by discrimination.
6. Button is disabled until the right amount of information is given.
7. There is a settings button which will take the user to the settings.



<ins>Login </ins>

1. A form to input user details which will allow them to log in.
2. A button which will submit the form.
3. If the user inputs an incorrect email or password, then a message will flash underneath the heading giving 
   the user feedback.
4. There is advice on how a user can reset their password.
5. There is a link to the signup page in case the user doesn't yet have an account. 

<ins>Signup</ins>

1. A form to fill in in order to register an account.
2. A lightbulb will give the users information for the password requirements. 
3. There is an eye-icon which users can press to see the password they have inputted.
4. When the user enters a password that meets the criteria a tick will be displayed next to the eye-icon.
5. There is a check button the user must click to confirm they have checked the password.
6. Once signed up, the user is redirected to another page where they can enter their preferred name.

<ins>Add report</ins>

1. There is a reminder to not use person's name in the report.
2. There are initial options to start the report.
3. There is a disabled button which will become enabled when all the options have been chosen.
4. Upon pushing the add report button, the user is taken to a new screen where they can add a loction or skip 
   and then add a date.  

<ins>Search report</ins>

1. There collapsible from materialize that has four options: Search by discrimination, location, whether it has been reported or all.
2. If the user clicks on a header, then that part of the collapsible stands out to draw focus. 
3. In all search options except 'search all', there is an option to choose a date frame within which to search.
4. For the discrimination option, you can choose from the pre-selected discrimination categories. 
5. For the location option, you can choose any of the pre-set location options.
6. Should you choose to search by buildings, you may choose a second location in order to compare. 
7. Like in the add report, the button stays disabled until the user has given enough information for a viable report.
8. Starred inputs are there to show the user which information is needed.
9. For searching by reported to authorities, there is a choice between whether the report has or hasn't been reported.

<ins>Settings</ins>

1. There is a collapsible on the settings page where the user can change name, password, email or delete account.
2. Each of the options above are in their own collapsible body.
3. The current name, password, email have the original values displayed underneath.
4. When deleting the account, the user must put in their correct password.  

<ins>Search Result</ins>

1. All results are within a card and display all of the report information.
2. The pagination works by splitting up the reports ten at a time and putting them in separate collapsibles.
3. At the top of the page, the user will get three statistics: How many reports, what percentage they make up of 
   the database they make, and how many have been reported to authorities. 
4. There are two choices with each report: to either edit or delete the report.


<ins>User Modify</ins>

1. The user modify page has a form with all previous values form the report.
2. The user can modify any of the values and resubmit the form.

<ins>User Delete</ins>

1. The user delete page will show a single report with a delete button.

<span id="featuresLeftToImplement"></span>
### Features Left to Implement

MS4
- Multi buy will be customisable based on the the amount and discount - for now it is fixed at buy 3 and get x amount off. X can be changed though.




- The date will present itself the correct way round.
- Automatic email will be sent to the website managers when a report is updated/added
- Public can recommend categorise when adding a report rather than having to email separately.
- A google api will allow the locations of the features to be displayed as clusters across a map. 
- People can filter incidents just by a date frame. 
- Export data as a CSV to be used on excel.
- Councils/ other professional bodies will be able to upload reports of discrimination via their own CSV.
___
<span id="dataIntegration"></span>
## Data Integration

I used the following repository for converting excel spreadsheets to JSON files. This is my repository and I was able to 
build it by using the following article:
[Article to upload excel to JSON](https://www.journaldev.com/33335/python-excel-to-json-conversion)


___
<span id="defensiveFeatures"></span>
## Defensive Features

+ Incuding a modal that will show when the user either uploads their own photo or place an order. This is to stop the user clicking
  any other buttons because they think nothing is happening.
+ User is limited to a quantity of 1 of a specific item, if they are digitally downloading that item. This is because you only need to download one digital copy.
+ User can only access the links to members area if they are logged in. 
+ Only super users are able to access django admin and my own custom admin. 

___
<span id="technologiesUsed"></span>
### Technologies Used

Languages used

Front-end

1. HTML
2. CSS
3. Javascript

Back-end 

1. Python 
2. MongoDB Atlas

Frameworks

1. Materialize 1.0.0
2. Flask 
3. Jinja 
4. jQuery


___
<span id="testing"></span>

## Testing
I also tested my website across the different browsers to ensure the CSS and JS held up, which it does. 
[Cross Browser Testing](static/files/testing/cross_browser_testing.pdf)
 
### User stories

User Stories - first time users | Expected outcome | Actual outcome 
--------- | --------------- | ---
As a first-time user, I want to easily navigate through the website be able to easily access all of its features. | I expect all of the links to be working and in an intuitive position| All the links take me to their destination and none are broken.
 
User Stories - returning users | Expected outcome | Actual outcome 
--------- | --------------- | ---
As a returning user, I want to be able to log in easily.                                                     | I expect to find the login button easily and be able to fill in the form to login.| I could find the login button easily in the nav bar and the form is very quick to fill in. Once I have logged in I am taken to the dashboard.


User as a charity or researcher (professional user)| Expected outcome | Actual outcome 
--------- | --------------- | ---
As a profession user, I want to be able to see some statistics about my search so I can compare them to other searches. | I expect to see some statistics when I search the database | At the top of the search results, I can see how many reports have been returned, what percentage of the database they are and how many have been reported to authorities.

### General testing

#### Basic test

1. Nav has been fully tested
2. I have checked that the collapsibles open and close appropriately
3. I have checked buttons enable and disable appropriately
4. I have checked that the correct form options are unhidden based on the users previous inputs

#### Feedback from other users
User 1

* "When i click search by location, it does not populate any cities after choosing that location type. If there are none in the database maybe include a little message saying sorry there are none as it currently looks like a bug" 

Regarding this comment, I have since filled out several reports so that the website has something to pull from the database. 
It is unnecessary for me put in a comment about there not being any available as the database will always have reports in.

* "The search bar is a random length on the mobile view. It doesn't seem like it's lined up with anything?"

Since this, I have changed the nav to a grid so it has more of a purposeful size.




### Responsive design

As in the wireframes section, the website is responsive across mobile, iPad, iPad Pro and Laptops - both MDi and HDMi.
[Here is the list for the responsive images.](static/files/wireframes/responsive-design.jpg)

### Cross browser test

I have test my site on Microsoft Edge, Firefox and Chrome web browsers.
I specifically test the following things:
   + Do the collapsibles and their animations open?
   + Does the checkbox still work?
   + Does the tooltip work on the signup page?
   + Do the select options work? 

On the browsers Firefox, Edge and Chrome, all of th elements above are working properly.
I have attached a pdf of the results of the tests. They are only for Firefox and Edge as Chrome was my main developer and is
covered by my other testing.

[Firefox cross browser testing.](static/files/testing/crossBrowserTesting/crossBrowserFirefoxTest.pdf) 

[Edge cross browser testing.](static/files/testing/crossBrowserTesting/crossBrowserEdgeTest.pdf) 



### Code validation

#### Python
To check my python code validation, I have used a combination of 'cornflakes-linter 0.4.0' and http://pep8online.com/
I have configured the cornflakes to accept a line length of 120 characters.
Therefore, the only code issue that comes up on http://pep8online.com/ is that the lines are too long as it is set to 79 characters.

#### CSS
CSS has been checked by this online validator: https://jigsaw.w3.org/css-validator/#validate_by_input
My css only has warnings about webkits being 'unknown vendor extensions'.
There are no issues with my css. 

#### HTML
My HTML has been checked on this website: https://validator.w3.org/

#### Javascript
My javascript has been checked at https://jshint.com/
There are no issues with my JS. 

### Interesting bugs

1. [Dividing by 0](static/files/testing/interesting-bugs-documentation/bug-for-dividing-by-0.pdf) 
2. [Logging in issues](static/files/testing/interesting-bugs-documentation/Issue-with-logging-in.pdf) 
3. [Console error breaking the JS flow](static/files/testing/interesting-bugs-documentation/js-console-error-interrupting-the-other-js.pdf) 
4. [Problems reading if the email address exists, live](static/files/testing/interesting-bugs-documentation/Live-reading-if-the-username-exists.pdf) 
5. [Only certain elements are being searched in the array](static/files/testing/interesting-bugs-documentation/Not-match-against-all-array-elements.pdf) 
6. [Problems with validating the password](static/files/testing/interesting-bugs-documentation/password-validation-issue.pdf) 





___
<span id="responsiveDesign"></span>
## Responsive Design

This project has been optimised to the common devices on Google Chrome's Dev Tools.
It has been specifically designed for the following:
   + Moto G4
   + iPhone 6/7/8
   + iPad
   + iPad Pro
   + Laptop with MDPI screen
   + Laptop with HiDPI screen


The majority of the website stays consistent to an easy user experience. There are minor changes to font-sizes etc. Some 
of these can be seen in the [responsive image](static/files/wireframes/responsive-design.jpg). This has been taken from the website:
http://ami.responsivedesign.is/#

There are a few major resposive choices, detailed below.

1. When viewing on a laptop the search results present their information in a different way. The incident description,
date and whether it had been reported are shown in their own colour on the right of the card.

2. The pictures of staff and descriptions shift to being alongside each other once on the laptop/ landscape iPad Pro 
screen.
___
<span id="deployment"></span>
## Deployment

<span id="deploymentLive"></span>

### To run the app on Heroku. 

Create a Heroku account.
Click to start a new app.
Pick your location based on the closest free version (or paid version) to your actual location. For this project it was Europe.
Choose an appropriate name for the app and click to create.

Once your app has been created, then move to the ‘deploy’ tab. You can connect to GitHub through one of the tabs. 
I, however, have used the CLI.
You can link to an existing repository by using the following command in your IDE:
```
$ heroku git:remote -a "enter-your-heroku-app-name"
```
Heroku actually have excellent documentation on this and the full documentation can be found here under the ‘deploy’ tab in your Heroku account. There are several ways to connect your project to Heroku. 

Then, head over to the ‘settings’ tab and click on the ‘reveal config vars’ button. 
Configure the following:

Key: value

IP: 0.0.0.0 

PORT: 8080 

MONGO_URI: "link to your MongoDB" 

You can find your MongoDB link by going into your MongoDB Atlas account and clicking the ‘connect’ button. From there you have the option to choose to connect to your application and can select the correct language and version. 

With the Heroku settings sorted, you can head back to your IDE.
There a few things you now need to set up:
1. A ‘procfile’ which will tell Heroku what kind of application it is and how it should be run.
2. A ‘requirements.txt’ which will tell Heroku which dependencies it needs to install in order for the app to run. 
The command for ‘procfile’ is: 
```
echo web: python run.py > Procfile
```
The command for requirements is:  
```
pip3 freeze --local > requirements.txt
```
Please note that you need to re-run the requirements command if you add any dependencies mid-project. Otherwise, Heroku will not deploy the app correctly. 

With those set up, you can now push your project to Heroku directly from your IDE.
```
$ heroku login -i
```
Enter your username and password.
Push your commits to Heroku using this command:
```
$ git push -u Heroku master
```


<span id="deploymentLocal"></span>

### To run the app locally

To run this project locally, please ensure you have an IDE installed on your computer. Popular ones are gitpod, Visual Studio or PyCharm (for python projects specifically).

Regardless of which IDE you choose, you will also need the following installed. 
+	This project uses MongoDB as a database, and therefore you will need either a MongoDB Atlas account or have MongoDB running locally on your machine.
    +  	To set up MongoDB Atlas please see the documentation 
        [MongoDB Atlas](https://www.mongodb.com/cloud/atlas)
+	[PIP](https://pip.pypa.io/en/stable/) – to install packages such as pyMongo    
+	[Python3](https://www.python.org/doc/) – the project uses Python3 for the backend language – specially Python 3.8
+	[Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) – for easy version control

The next step is to access your github repository.
Option 1 is to download a zip file. 
1. On the GitHub project page, there is a ‘code’ tab which will dropdown to allow you to download a zip file.
2. Once downloaded, extract the files to a desired folder on the desktop.

Option 2 is to clone the repository.
1. Under the same code tab, click to copy the url for your repository.
2. Open Git Bash on your local computer and ensure you are in the right directory. Then run the following command:

```
git clone https://github.com/cgpalmer/ms3-project-2.git
```

It is recommended to use a virtual environment for the Python interpreter. Python's own built in environment can utilised by this code:
```
python -m .venv venv
```

Please note: Different IDE and operating systems, your python command may be slightly different.
Once you have your virtual environment, you can activate it with:
```
.venv\Scripts\activate 
```

I have attached a link to the documentation on setting up a virtual environment, in case the commands are different. 
[Python interpreter](https://docs.python.org/3/library/venv.html)

Next, you will need to download all of your requirements for the project. You can do this manually or you can run this code: 
```
pip -r requirements.txt.
```

All that is left to set up now is your SECRET_KEY and a MONGO_URI. You can store these in a file:- .flaskenv. 
You must ensure your database name is the same as the one in MongoDB so it connects properly. For this project it is “projectDB”.

There are three collections to interact with: report, categories, user_credentials. 
Now, you are ready to run the app in browser.
The command is: 
```
python3 app.py
```

This will open a port (which may be different depending on your IDE) and gives you the open to see your app.

___
<span id="credit"></span>
## Credit

<span id="tutorials"></span>
<ins>Tutorials</ins>

For all of the following tutorials, I have edited the code necessary for my project. 

This tutorial helped me to make sure my urls were clearer.
https://restfulapi.net/resource-naming/

This tutorial helped me to alphabetise some areas of results.
https://stackoverflow.com/questions/1959386/how-do-you-sort-a-list-in-jinja2

This tutorial helped me to use the date-time function in python
https://www.dataquest.io/blog/python-datetime-tutorial/

This tutorial helped me to save the date from the input into the mongoDB.
https://stackoverflow.com/questions/58160212/how-to-save-date-from-datepicker-into-database-in-sqlalchemy-flask-application

This tutorial helped me to validate a password live for when users are deciding their first password.
https://www.w3resource.com/javascript/form/password-validation.php


This link helped to set up Flash-messages.
https://www.youtube.com/watch?v=DFCKWhoiHZ4

This tutorial helped me to store things to the Flask session.
https://pythonise.com/series/learning-flask/flask-session-object

This tutorial helped me to set up a back-end validation check which matched the live JS version.
https://www.geeksforgeeks.org/python-program-check-validity-password/


This tutorial helped me to check if there was a value in the array that matched the criteria.
https://stackoverflow.com/questions/55957237/checking-if-input-value-matches-the-array-items

This tutorial helped me to check the email live to see if there was already a user with that account.
https://stackoverflow.com/questions/14411235/while-typing-in-a-text-input-field-printing-the-content-typed-in-a-div

This link helped me to process a list of emails in python and access them in JS.
https://groups.google.com/forum/#!topic/web2py/OmwTo1ZsFN4

This link helped me to process a list from python into a json file.
https://stackoverflow.com/questions/23038710/accessing-python-list-in-javascript-as-an-array

This helped me to understand how I could get the value from a select option.
http://jsfiddle.net/YPsqQ/

Tutorial on how to hash a password
https://nitratine.net/blog/post/how-to-hash-passwords-in-python/

Tutorial helped me to pull certain keys and values from mongodb queries
https://realpython.com/iterate-through-dictionary-python/

I also use the documentation for Flask, Jinja, Materialize, jQuery and Python.
I used W3Schools for any basics that I needed to brush up on.
A special thank you to Stack Overflow, as even though I didn't always use the help they provided in the end, I still learnt a lot from trial and error.


<span id="media"></span>
<ins>Media</ins>

To generate my favicon, I used this website: 

https://www.favicon.cc/



<span id="acknowledgements"></span>
<ins>Acknowledgements</ins>  

I used the Government's own website when choosing which categorise would be available. There are a few names I have
changed on the grounds that there are more colloquial terms available. Eg. 'Sex' has been changed to 'sexism'.
Please find the link attached below:
https://www.gov.uk/discrimination-your-rights


___
<span id="project"></span>
## Project Evaluation

I believe this website handles its purpose with maturity and simplicity. There is no unnecessary data collected and indeed
there is the option to skip it. The clean UX, complete with a responsive navbar, makes the site very easy to navigate.
All of the links to the user areas are in the same place and easy to access in the navbar. 
This is also complemented by a simple and complimentary colour scheme. They colours are calm and neutral which 
sets the correct tone for the purpose of the website.

There are a variety of way in which you can search through the reports. All of search options are on one webpage
which cuts down on screen loading time. In addition, elements of a form that aren't needed are hidden. Again, this
creates a clean user experience where the user is not over loaded with information.

Giving the user complete control over their own reports helps to promote trust in the website. Users can edit and
even delete their reports at any time. If a user is logged in they will be associated with that report in their dashboard
but no where else on the website. This allows flexibility and anonymity. 

Overall, I think the website has a clear purpose, clean UX and defensive features to ensure the user gets the most
out of the experience.



<span id="improvements"></span>
### Improvements

+ There could be a few instructions on where to find what - especially things like searching your own reports in the dashboard. However, the dashboard is hidden and you are taken straight there when you log in and the manage reports is open ready. 
+ I tried to move my secret_key to the env.py but for some reason it didn't work. I'd need to hide it to make it more secure in the future.
+ I would like to refactor the code that chooses whether you can search by a date.
+ The menu could have icons on it as a visual reminder.
+ There could be a dashboard button like the settings button on the pages as a shortcut.
+ I need to use an ajax to live check the email addresses when signing up as the regex will become slow and cumbersome 
  as the users grow.
+ The code for counting the reports has recently become depreciated - in the future I would like to upgrade the code to the new version.
+ Some of my flash messages aren't clear enough to standout to the user. It would be better if they had a border or different css to help them stand out. 



https://stackoverflow.com/questions/16080952/django-cannot-convert-float-to-decimal-first-convert-the-float-to-a-string
https://www.frames.co.uk/picture-frames/popular-sizes
https://blog.365canvas.com/canvas-sizes/
___




https://djangocentral.com/uploading-images-with-django/?fbclid=IwAR3mB4I-krN5zkLP9fqCiiCro8N3JgtrOy_KWGEoV_KilRhJO3FxGn6vaR4#:~:text=The%20image%20column%20is%20an,as%20read%20and%20write%20them.&text=Setting%20dynamic%20paths%20for%20the%20pictures%20is%20also%20possible.&text=Now%2C%20Install%20Pillow%20by%20running%20the%20following%20command%20in%20your%20shell
https://www.anchorprint.co.uk/printing-products/calendar-printing/
https://www.pngitem.com/so/landscape-canvas-blank/
https://frame-company.co.uk/black-20x16-frame-with-white-mount-cut-for-image-size-a3-165x1175_16.html?gclid=Cj0KCQjw5eX7BRDQARIsAMhYLP-B6_kFkSbISrgxkqcT4Gt0Jw3nnxoGkkXB5xVpLBntA_ngVFYX39caAvm_EALw_wcB
http://www.carouselcalendars.co.uk/product/landscapes-of-britain-a4-calendar1


downloading files
https://www.youtube.com/watch?v=qKAf5xF6nOE&t=112s

pdf
https://codeburst.io/django-render-html-to-pdf-41a2b9c41d16

Cyclic imports
https://stackoverflow.com/questions/62100550/django-importerror-cannot-import-name-reporterprofile-from-partially-initiali

How to display a backup image
https://gist.github.com/oscarmorrison/52f9d4b3dfce386c7b11b3fcbdd74dd4

Help with a bug
https://stackoverflow.com/questions/51380780/django-foreign-key-cannot-assign-must-be-a-instance
Help updating a blog
https://stackoverflow.com/questions/3681627/how-to-update-fields-in-a-model-without-creating-a-new-record-in-django

Max value on integer fields
https://stackoverflow.com/questions/30849862/django-max-length-for-integerfield/30850101#30850101

For loop counter
https://stackoverflow.com/questions/11481499/django-iterate-number-in-for-loop-of-a-template

https://www.freecodecamp.org/news/python-empty-list-tutorial-how-to-create-an-empty-list-in-python/

javatpoint.com/python-program-to-print-the-duplicate-elements-of-an-array

https://chartio.com/resources/tutorials/how-to-filter-for-empty-or-null-values-in-a-django-queryset/

https://stackoverflow.com/questions/13422689/django-how-to-limit-number-of-objects-returned-from-a-model

https://bootsnipp.com/snippets/e3q3a

https://stackoverflow.com/questions/51084909/how-can-i-use-a-catch-all-route-using-path-or-re-path-so-that-django-passes
https://stackoverflow.com/questions/35156134/how-to-properly-setup-custom-handler404-in-django
https://stackoverflow.com/questions/34685233/css-badge-over-image-with-bootstrap

https://www.canva.com/colors/color-wheel/ - color scheme

https://developer.mozilla.org/en-US/docs/Web/API/Window/sessionStorage

https://stackoverflow.com/questions/687295/how-do-i-do-a-not-equal-in-django-queryset-filtering#:~:text=While%20you%20can%20filter%20Models,filtering%20using%20the%20Q%20object.

https://stackoverflow.com/questions/53859972/django-whitenoise-500-server-error-in-non-debug-mode

Catching broken images
https://stackoverflow.com/questions/92720/jquery-javascript-to-replace-broken-images
https://stackoverflow.com/questions/58088946/getting-uncaught-referenceerror-function-is-not-defined

Remove colour from navbar toggler
https://stackoverflow.com/questions/50668594/remove-border-color-for-navbar-toggler-hamburger-icon-bootstrap-4
