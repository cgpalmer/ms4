# Report On Any Discrimination


![Landing Image](static/files/wireframes/landing_image.png)
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
a variety of canvas sizes, frames or calendars. In addition, users can use their own unique photographs and have them printed in 
the same way!

With no need for bluetooth or fancy smart phones, Hidden Gems is a one-stop shop for all of the users needs! 

Photos can be digitally downloaded, delivered or put in a frame, calendar or on a canvas.


___

<span id="inspiration"></span>

## Inspiration

My inspiration from this project came from a need to connect with an e-commerce website. I did not feel particularly excited about the prospect of making an online shop, 
so I needed to pick something that would intrinsically motivate me. 

So I decided to build a website where I could show-case my photographs from travelling. I have used my favourite photos from the small parts of the world that I have
been lucky enough to visit.

I decided it would be nice if people wanted these photos in a frame or on a canvas. However, I was sure people would much prefer their own photographs on a canvas, which led me to 
my project idea. 

In the past, I have used the bluetooth machines in shops to print my pictures and found them to be a complex and confusing. I thought that a website where you could directly
upload from your phone would go a long way. It would have the look and feel of uploading normal files to your computer, email etc. This made me feel like I could design a site
where it was accessible to a wide range of people.



#### Requesting information


#### Design



___

<span id="UX"></span>
## UX - 5 planes

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



#### Business objectives

1. For people to use us to purchase frames, calendars and canvases.
2. For people to upload their photos and know that the picture will be delivered to their door at the correct size for the containers.

#### Content required:

1. Profile page with details about the user.
2. Filters, categories and search to refine product search and speed up the user experience. 
3. Products with extended details.
4. A basket to handle the purchases.
5. A checkout to process purchases and payments.
6. Reviews about each product available to create, edit, delete and read. 

#### Interaction design


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

<span id="features"></span>
### Features

Please see this link for a [Full list of features](static/files/UX/scope/feature_list.pdf)

<span id="featuresLeftToImplement"></span>
### Features Left to Implement

1. Picture resolution validation to make sure the photo is high enough quality.
2. A product preview of the photo within the frame or on the canvas/ calendar. 
3. A blog to explain the story behind each photo as a unique feature.
4. Users can upload their own photos to be bought and receive a percentage of the profits. 
5. User to attach the purchased image to an email when the user isn’t logged in. This would allow non-logged in users the option to buy digitally. 
6. The user would not need to put in their delivery details if only purchasing digital photos.
7. Emails will actually be sent with an email receipt.
8. User to retain their basket in session, despite logging out and then in again.
9. - Multi buy will be customisable based on the the amount and discount - for now it is fixed at buy 3 and get x amount off. X can be changed though.
10. A new customer offer to apply on first order that makes the delivery free.


### Skeleton design
Wireframes

Whilst this isn't an exhaustive document of every page on each device, it showcases that there is responsive design within the site. These particular images focus on three main
breakpoints - small, medium, extra large. Respectively, mobile, tablet, desktop.
[Image a website on different devices.]()



### Surface design
Buttons
Action buttons also have a chevron pointing right, which is the logical symbol for “next”. All of the navigation buttons or cancel buttons have a chevron pointing left. This give the illusion that there is a certain way to navigate around the website, that discourages the users from click the browser “back” button. 

Typography
The same font is used across the website. The font-weight has been adjusted accordingly for the elements that need to stand out more or need to be more readable. For example: Where necessary, on the small “special offer” badge the font-weight is slightly less so it is more readable at a smaller font. 
I deliberately picked a clean, plain text font to maximise accessibility for the user. It does not use any cursive devices, nor is it italic. 

Colour Scheme
For my project, I knew which picture I wanted for my landing page. I decided that I would use a colour from the picture in order to replicate the feel of “nature” in colour scheme. As the majority of photographs on the site are animals or nature, I felt this fitted the website well. 
Once I had my base green colour, I used [Canva](https://www.canva.com/colors/color-wheel/) as a tool for developing secondary colours. Using the “Complementary” section, I chose to pick the secondary as the dark blue you see on the screen. I used the chromatic and found it suggested slightly lighter colours. However, the base green I chose, I decided to keep as it was darker and the “white” text had a better contrast ratio and was much easier to read.
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
+ Only super users are able to access django admin and the content management system admin. THIS MAY CHANGE

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
2. Sqlite 3 in development
3. Postgres in deployment

Frameworks

1. Bootstrap 4
2. Django 
3. jQuery
4. Sqlite 3 in development
5. Postgres in deployment
6. Font Awesome
7. Google Fonts

Other dependencies include:
+ Pillow
+ White Noise

Of course, a full list can be found at [requirements.](requirements.txt)


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

#### Feedback from other users
User 1

* "The search bar is a random length on the mobile view. It doesn't seem like it's lined up with anything?"

Since this, I have changed the nav to a grid so it has more of a purposeful size.




### Responsive design

As in the wireframes section, the website is responsive across mobile, iPad, iPad Pro and Laptops - both MDi and HDMi.
[Here is the list for the responsive images.](static/files/wireframes/responsive-design.jpg)

### Cross browser test





### Code validation

#### Python
To check my python code validation, I have used a combination of 'cornflakes-linter 0.4.0' and http://pep8online.com/
I have configured the cornflakes to accept a line length of 120 characters.
Therefore, the only code issue that comes up on http://pep8online.com/ is that the lines are too long as it is set to 79 characters.

#### CSS
CSS has been checked by this online validator: 
My css only has warnings about webkits being 'unknown vendor extensions'.
There are no issues with my css. 

#### HTML
My HTML has been checked on this website: https://validator.w3.org/

#### Javascript
My javascript has been checked at https://jshint.com/
There are no issues with my JS. 

### Interesting bugs

1. [Dividing by 0](static/files/testing/interesting-bugs-documentation/bug-for-dividing-by-0.pdf) 

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


There are a few major resposive choices, detailed below.


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

https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_address
___

https://stackoverflow.com/questions/46132857/allow-certain-group-and-admin-to-view-part-of-html-in-django
https://stackoverflow.com/questions/44265564/django-registration-of-tag-library-not-working



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

https://stackoverflow.com/questions/16080952/django-cannot-convert-float-to-decimal-first-convert-the-float-to-a-string



<span id="media"></span>
<ins>Media</ins>

To generate my favicon, I used this website: 

https://favicon.io/emoji-favicons/gem-stone

These ima 

This site helped me know which [Frames](https://www.frames.co.uk/picture-frames/popular-sizes) were the right size.
This site helped me know which [Canvases](https://blog.365canvas.com/canvas-sizes/) were the right size.

<span id="acknowledgements"></span>
<ins>Acknowledgements</ins>  

Thank you to Asos and Topshop for providing different mobile experiences, which I used to help inform my own decisions. 


___
<span id="project"></span>
## Project Evaluation





<span id="improvements"></span>
### Improvements




