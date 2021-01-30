# Hidden Gems


![Landing Image](static/UX/Skeleton/files/wireframes/landing_image.png)
### [Live page](https://hidden-gems-cgpalmer91.herokuapp.com/)





___

## Contents
+ <a href="#rationale">Rationale</a>
    - <a href="#inspiration">Inspiration</a>
+ <a href="#UX">UX</a> 
   - <a href="#fivePlanes">5 planes of UX</a>
   - <a href="#userStories">User Stories</a>
+ <a href="#features">Features</a>
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

___

<span id="UX"></span>
## UX - 5 planes
<span id="fivePlanes"></span>
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
Giving a user the option to download digitally or print a photograph covers all scenarios in which a user would like to purchase a photograph. For examples, see user stories. 


Strategy for the business

There will be an admin section which allows admin staff to add, remove, edit products, and read orders to be fulfilled. There is also an admin link to the full Django admin site, which is only accessible to the superuser. I separated the two for a couple of reasons: 
The staff structure at the business may want people to add products but not at able to access customer details. In addition, they may want some staff to see the most recent orders but not have access to them all. Finally, this separation can prevent some staff from editing special offers and other finance related possibilities.
This all allows for full customisation of delegation tasks which allows managers and employees to smoothly work together throughout the day. 
The forms are validated to ensure that all the information that is needed for the website to work is provided when adding or editing products. 

### Scope
<span id="userStories"></span> 
### User Stories

#### First-time user

1. As a first-time user, I want to easily navigate through the website be able to easily access all of its features.
2. As a first-time user, I want to be able to immediately see what the website is about.
3. As a first-time user, I want to be able to create an account.
4. As a first-time user, I want to be able to log in with my new account.
5. As a first-time user, I want to be able to purchase something without having to create and account.

#### Returning user

1. As a returning user, I want to be able to log in easily.
2. As a returning user, I want to be able to modify my delivery details.
3. As a returning user, I want to be able to modify one of my reviews.
4. As a returning user, I want to be able to add a review.
5. As a returning user, I want to be able to delete one of my reviews.
6. As a returning user, I want to be able to upload one of my own images to use.
7. As a returning user, I want to be able to use a previous upload in a purchase.
8. As a returning user, I want to be able to see my order history.
9. As a returning user, I want to be able to see my previous purchases.
10. As a returning user, I want to be able to download my digital purchase.
11. As a returning user, I want to be able to change my password.
12. As a returning user, I want to be able to log out when I am done.
13. As a returning user, I want my personal details to be private.  

#### General user

1. As a user, I want to access to all the appropriate features, regardless of what device I am on. 
2. As a user, I want to be able to explore the products immediately.
3. As a user, I want to be able to gather information about the products.
4. As a user, I want to know when I have added something to my basket.
5. As a user, I want to be able to modify my basket at any point. 
6. As a user, I want to be able to view my basket at any moment.
7. As a user, I want to be able to search for different products.
8. As a user, I want to be able to easily see contact information.
9. As a user, I want to be able to see a summary of my order before I place it.
10. As a user, I want to be able to see full size photographs and the quality of them before purchase. 
11. As a user, I want digitally download my purchase.
12. As a user, I want to print and have a photo delivered. 
13. As a user, I just purchase want an accessory. 
14. As a user, I want to buy the photo and have it in or on an accessory. 
15. As a user, I want my photo printed on a canvas, calendar or in a frame. 


#### Retail assistant

1. As a retail assistant, I want to be able to edit a product.
2. As a retail assistant, I want to be able to add a product.
2. As a retail assistant, I want to be able to delete a product.
3. As a retail assistant, I want to be able to see the latest 5 orders.

#### Store owner (super user)

3. As a store owner, I want to be able to see all of the above.
2. As a store owner, I want to be able to easily control and manipulate all the data associated with the website. 
3. As a store owner, I want to be able to easily naviagte to the Django Admin panel.

___
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

Please see this link for a [Full list of features](static/files/UX/Scope/feature_list.pdf)

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
9. Multi buy will be customisable based on the the amount and discount - for now it is fixed at buy 3 and get x amount off. X can be changed though.
10. A new customer offer to apply on first order that makes the delivery free.
11. Photos must be printed on all available sizes. Customers should be able to choose that size when adding to the basket.
12. Better data integration for storing the linked products. 
13. A modal to provide feedback when an image is uploading.
14. Order history will be sorted by date like in the admin profile.
15. To have an image preview when editing, in the basket, linked products of an accessory.
16. Warn users if they have repeated linked products on their calendars after they edit basket.


### Skeleton design
Wireframes

Whilst this isn't an exhaustive document of every page on each device, it showcases that there is responsive design within the site. These particular images focus on three main
breakpoints - small, medium, extra large. Respectively, mobile, tablet, desktop.
[Image a website on different devices.](static/files/Skeleton/wireframes/wireframes_finished.pdf)



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

Image Presentation

Image presentation was tricky for this project and I feel I got the balance just right. As anyone knows, the larger the images on website, the slower the page will load.*
However, for a website that is selling products that have images printed onto products, printed out or digitally downloaded, I needed to make sure images looked good on the page.
To achieve my balance, I restricted the image sizes to the largest sized image container on the website (300px height). This greatly reduce the amount of memory each photo was taking
up. 

However, I want the user to still be able to see the full image and explore it's quality. So images across the website are links (where appropriate) to the full size image, hosted on 
Image Shack. This way, I do not need to load the photo, just the link but the user can still zoom in and appreciate the real quality. 

I also left the width as unrestricted and object fit is set to contain. This has caused some images to sit differently in their containers but where possible they have all been aligned either at the bottom or top,
depending on which suited the purpose better. My reasons for not controlling the width meant that some of the images became distorted or no longer had the main part of the picture visible.
Again, I feel the images have the best compromise of responsive design, performance and quality. 

*Please see my efforts to improve my websites performance on the [Testing page](TESTING.md) under the "performance section".

___
<span id="dataIntegration"></span>
## Data Integration

Throughout this project, I have Postgres and JSON files to store data. I have also used Whitenoise to hold my static file, 
as Heroku doesn't support file uploads. I chose Whitenoise as an option for my project but I am aware that in production,
you would normally pay for a cloud service such as AWS to allow for scaling. 

Please find my [database table schema](static/files/data_integration/database_schema_tables.pdf) and my [database schema diagram](static/files/data_integration/database_schema_diagram.png)
at their respective links.

#### Postgres

With Postgres, in conjunction with Django, I have created several models within each app. I have ensured that each model
only contains data that is relevant to the app. If I felt information was better suited, I created a separate model.

I have chosen Postgres as it is a relational database and allows for the collaboration between models. I have made use of 
the foreign keys in order to control my cross-app logic. For instance, I store a product in each of the reviews as a 
foreign key. By storing the instance of a product, I am able to extract whatever data is appropriate
for the review. 

I have used a combination of entries for my models, including the following: Character fields, dates, decimals,
integer, boolean, text fields and urls. Each of these has been specifically chosen as the best tool to store the data. 

Further examples of data integration logic:

In the products app, I have three models: Special, Category, Product. Instead of storing the category within the 
product, I stored it as it's own model. This allowed me to loop through the categories for forms or other select options.
In addition, having both categories and special offers allow for an update in either, without having to change each individual
product. Eg - swapping an offer from 'clearance' to 'Multi-buy' would only require the changing of the category. Each product
with that foreign key would then change in turn.

When a user uploads their own images, I have stored their profile in the database as well. This allows me to loop through
the user's photos and display them in the "linked products" option when purchasing an accessory. By storing their
profile, I can ensure they do not have access to anyone else's photographs. Likewise, I have done the same to the 
ContentDownload model which means the user can only download, what they have purchased.

The most unique model is the linked_product model, in the checkout app. It was important that the customer had a record
of the linked_products that they chose for their order - in case it was wrong. The model only has three fields: order.id,
product, linked_product. The product refers to the original item being purchased (calendar etc) and the linked products
refer to the photographs associated with the product. The idea is that on the order summary, I can list the product and every linked product associated with it.

However, whilst this works, it is not the elegent or efficient of designs. For every calendar ordered, 12 entries go 
into this model. That means that the database will fill up quickly. Moreover, looping through each item looking for the
right order.id with continue to get slower, the more orders placed. 

Therefore, whilst this works for the website on a small scale, it will need to be altered ready for upscaling.

#### JSON

The most complex part of my data storage came from storing items in the basket. This was complicated by the fact that some
products, such as a photo frames, could be associated with another product - or 12 others, in the case of calendars.
I had to ensure there was enough data in the session to be able to pull images, SKUs and delivery details in order to provide
customer information and, more importantly, to query.

I am most proud of the condensing_basket view in checkout. It takes the items stored in the basket and checks if there
are any duplicates, usually from editing the basket. It then identifies duplicates, updates the quantity of one and deletes
the other. This was only possible because I was able to store so much meta-data in the basket['items']. It provides
a much cleaner summary for the user.  
___
<span id="defensiveFeatures"></span>
## Defensive Features

General

+ Form validation is present on each form.
+ There is a modal that asks for confirmation whenever something is being deleted.
+ A custom 404 page has been made in the case of broken links.
+ Visual feedback messages at the top of each appropriate screen for successful and failed actions.

Authentication

+ User can only access the links to members area if they are logged in. 
+ Only super users are able to access the full Django admin site.
+ Retail users and super users are able to access the websites custom Content Management System in the Admin Profile Page.


Products

+ Only users can add a review so that poor reviews can be address by contacting the user. Users are redirected to the login
  page.
+ Only photographs can be downloaded digitally - the option is hidden for accessories and set as delivery by default.
+ The 'add to basket' button disables if you click a quantity of 0.
+ Digital products are auto-changed to a quantity of 1.
+ The quantity input is also disabled and cannot be altered when the item is digital download.
+ When an item is not linked to an extra product, the preview picture disappears. This is to avoid the user clicking on
  the photograph and receiving a broken link.
+ There is an image of a white square, should any work out how to unhide the image or the JS fails. 


Basket 
+ Items are delete from basket if the quantity is changed to 0.
+ A warning tells the user if their accessories (calendar etc) does not have photographs associated with them and what will happen. 
+ A warning tells the user if there are repeated photographs in their purchase. Eg, calendar has two of the same photos.
+ User is limited to a quantity of 1 of a specific item, if they are digitally downloading that item. 
  This is because you only need to download one digital copy.
+ At this stage, users cannot be sent their purchase through email - therefore they cannot digitally download items unless they
  are logged in. The option is hidden in the edit basket model and the product detail model.
+ An empty basket will show a message and a button to redirect the user.



Checkout

+ Including a modal that will show when the user places an order. This is typically a slow processes.
  This is to stop the user clicking any other buttons because they think nothing is happening.
+ There are live validators to give clues to the user if the payment hasn't been successful.
+ The modal with disappear if the payment or delivery information is not valid. 
+ The user is directed as soon as the payment and order is successfully placed. 
+ If someone clicks back after processing a payment (during the modal loading), the basket will inform them that there aren't 
  items.

Reviews

+ There are live validators that will cap the rating score at 0 or 5 using JS.
+ The model also has 'Max' and 'Min' validators on the review_rating.
+ JS also stops the user using the large buttons to go above 5 or below 0.

Profiles

+ When downloading a purchase, there is a back button on the screen to encourage the user to use. This will refresh the
  screen and register that the item has been downloaded.


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
8. Lazy Loading

Other dependencies include:
+ Pillow
+ White Noise
+ Heroku for deployment

Of course, a full list can be found at [requirements.](requirements.txt)

Other
+ [Image Shack](https://imageshack.com/)
+ [Quick Database Diagrams](https://www.quickdatabasediagrams.com/)


___
<span id="testing"></span>

## Testing

For all testing, please click [Testing](TESTING.md)

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

Please find examples of the sites responsive design [here.](static/files/testing/performance_testing/responsive_design.pdf)


There are a few major resposive choices, detailed below.
1. The majority of the decision were based on how many objects could fit accross the screen. For mobile, I stuck to a rule 
   of one. For iPad and medium screens, I used two and for large, I used 3. However, I kept the forms in a single column
   as it seemed to flow better that way when I was using them. 

2. The bigget decision was how to handle all of the navigation links, account links and basket links. I used Topshop and
   Asos as market research for how they handled their navigation. I quickly understood that the basket and search bar,
   should always be visible. I also settled on separating the accounts from the products by having two navbars, which allowed
   a use to choose which section they needed to explore. 

3. The last major choice I had to make was which images to use on which screens. I thought about using the 'src set' option
   in the html, when I realised that all of my images were limited to around 300px height maximum. By pre-formatting the pictures
   to this size, I was able to really cut down on the memory and therefore, the loading time. I decided I would keep the large
   images as a link, so users could click and see the full-quality image.

___
<span id="deployment"></span>
## Deployment

<span id="deploymentLive"></span>

### To run the app on Heroku. 

Create a Heroku account. Click to start a new app. Pick your location based on the closest free version (or paid version) to your actual location. For this project it was Europe. Choose an appropriate name for the app and click to create.
Before you start to configure the app for deployment, go to the ‘resources’ tab and select Postgres. The free plan will suffice for this project. 
Then move to the ‘deploy’ tab. You can connect to GitHub through one of the tabs. I, however, have used the CLI. You can link to an existing repository by using the following command in your IDE:
```
$ heroku git:remote -a "enter-your-heroku-app-name"
```

Heroku actually have excellent documentation on this and the full documentation can be found [here]( https://dashboard.heroku.com/) under the ‘deploy’ tab in your Heroku account. There are several ways to connect your project to Heroku.
You can also set up automatic deployment to Heroku whenever you push to Github. You should be wary of this, however. If you are using Whitenoise, like I have for this project, then there is not a limited on your static files. 
If, however, you pay for a cloud service, such as AWS, then automatic deployments will wear down you request allowance.

Then, head over to the ‘settings’ tab and click on the ‘reveal config vars’ button. Configure the following:
- SECRET_KEY
- DATABASE_URL* 
- EMAIL_HOST_PASSWORD
- EMAIL_HOST_USER
- STRIPE_PUBLIC_KEY 
- STRIPE_SECRET_KEY 
- STRIPE_WH_SECRET
Stripe keys can be found in your stripe account, which you will need to set up at [Stripe.](https://stripe.com/gb)

EMAIL_HOST_PASSWORD Can be found in the security settings of your email host.
The EMAIL_HOST_USER is simply the email address from which you want your emails to be sent from. 

DATABASE_URL can refer to whichever database system you have set up for your project. For this project, I used Postgres as it is the relational database I wanted and Heroku has a convenient package for it. Before you select the Postgres, you will need to install a couple of things on Github.
You will need dj_database_url and psycopg2. Run the following commands to get them:
```
pip3 install dj_database_url
```

```
pip3 install psycopg2-binary
```

At this point, you will need re-record all of your requirements by using the following command.
pip3 freeze --local > requirements.txt

Please note that you need to re-run the requirements command if you add any dependencies mid-project. Otherwise, Heroku will not deploy the app correctly.

Finally, you can retrieve the URL for your Postgres in the the config vars part of the Heroku settings. 
Go to your main app settings.py and 

```
import dj_database_url
```

Then find the database settings and remove the default settings. Instead, run the default as:
```
‘default’: dj_database_url.parse(‘URL from Postgres – found in Heroku config var’)
```

Now that you have a connection with the database, you will need to re-migrate all of your models. Run the following code:

```
python3 manage.py migrate --plan
```

That will create all your databases. You will now need to “fill” the databases with products. You can do this by running the next command for every fixture in the project.

```
python3 manage.py loaddata <fixturename.json>
```

With those set up, you can now push your project to Heroku directly from your IDE.
First, you will need a ‘procfile’ which will tell Heroku what kind of application it is and how it should be run.
The command for ‘procfile’ is:
```
echo web: python run.py > Procfile
```

Log in to Heroku from the command line using:

```
$ heroku login -i
```

Enter your username and password. Push your commits to Heroku using this command:
```
$ git push -u Heroku master
```




<span id="deploymentLocal"></span>

### To run the app locally

To run this project locally, please ensure you have an IDE installed on your computer. Popular ones are gitpod, Visual Studio or PyCharm (for python projects specifically).
Regardless of which IDE you choose, you will also need the following installed.

•	PIP – to install packages such as django
•	Python3 – the project uses Python3 for the backend language – specially Python 3.8
•	Git – for easy version control

The next step is to access your github repository. Option 1 is to download a zip file.
1.	On the GitHub project page, there is a ‘code’ tab which will dropdown to allow you to download a zip file.
2.	Once downloaded, extract the files to a desired folder on the desktop.

Option 2 is to clone the repository.
1.	Under the same code tab, click to copy the url for your repository.
2.	Open Git Bash on your local computer or open the command line on your IDE and ensure you are in the right directory. Then run the following command:
```
git clone https://github.com/cgpalmer/ms4.git
```

You can then select a file destination for the directory.
First check you have pip installed on the machine:
```
py -3 -m pip --version
```

It is recommended to use a virtual environment for the Python interpreter. Python's own built in environment can utilised by this code:
```
python -m .venv <path for venv>
```


Please note: Different IDE and operating systems, your python command may be slightly different. You may also use the graphical interface to search and select an interpreter. 

Once you have your virtual environment, you can activate it with:
```
.venv\Scripts\activate
```

I have attached a link to the documentation on setting up a virtual environment, in case the commands are different: [Python interpreter.](https://docs.python.org/3/library/venv.html)
Next, you will need to download all of your requirements for the project. You can do this manually or you can run this code:
```
pip -r requirements.txt
```

Next you need to set up your environment variables in an env.py file.
You will need the following for your code to run:

- SECRET_KEY
- DATABASE_URL* 
- EMAIL_HOST_PASSWORD
- EMAIL_HOST_USER
- STRIPE_PUBLIC_KEY 
- STRIPE_SECRET_KEY 
- STRIPE_WH_SECRET

The database URL is so you can run the postgres server than I am running. If you remove the DATABASE_URL from the env, the settings.py will default to a sqlite3 database. Regardless of which database you run, will need to create the databases using the following commands.
Stripe keys can be found in your stripe account, which you will need to set up at [Stripe.](https://stripe.com/gb)

EMAIL_HOST_PASSWORD Can be found in the security settings of your email host.
The EMAIL_HOST_USER is simply the email address from which you want your emails to be sent from. 


Before you can start the local server, you will need to make sure your models have been created in the database. Follow these commands: 
```
python3 manage.py makemigrations --dry-run
```

This is to see the migrations before they occur.
```
python3 manage.py makemigrations 
```

Make the migrations.
```
python3 manage.py migrate --plan
```

This is to see the migrate before it occurs
```
python3 manage.py migrate
```
Migrate the databases.

This will create a database of all of your models.
You will then need to run the following code for each fixture in the project, in order to “fill” the databases.
```
python3 manage.py loaddata <fixturename.json>
```

Once the data is loaded you can then run your server locally. 

```
python3 manage.py runserver 
```

This will open a port (which may be different depending on your IDE) and gives you the open to see your app.


___
<span id="credit"></span>
## Credit

I'd like to thank Code Institute for a lot of what I have achieved with my project. The 'Boutique Ado' project gave me excellent example of
best practise when it came to things like Stripe, User Profiles, setting up forms from a model. I have copied and used a lot of the code for 
these sections as it was clearly best practice. 

I felt it more pertinent that I build on those practices and personalise them to my website. I felt I did an excellent job at editing the
code to suit my purpose. Furthermore, I felt I did an even better job of integrating my personal touches into the excellent code base.
I have ensured I have left a comment on the models or views etc, if I have taken code from the project.

I also used the documentation for the following:
- Bootstrap
- jQuery
- W3schools
- Font Awesome
- Django
- Python 3
- Whitenoise
- Stripe
- AWS
- Heroku

<span id="tutorials"></span>
<ins>Tutorials</ins>

For all of the following tutorials, I have edited the code necessary for my project. 

1. [Email address link](https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_address)
2. [Allow groups different access - django](https://stackoverflow.com/questions/46132857/allow-certain-group-and-admin-to-view-part-of-html-in-django)
3. [Registration of custom tags](https://stackoverflow.com/questions/44265564/django-registration-of-tag-library-not-working)
4. [Pulling data manually from a form](http://www.learningaboutelectronics.com/Articles/How-to-retrieve-data-from-a-Django-form-Python.php#:~:text=Basically%20to%20extract%20data%20from,this%20function%20as%20a%20parameter.)
5. [Uploading images with django](https://djangocentral.com/uploading-images-with-django/?fbclid=IwAR3mB4I-krN5zkLP9fqCiiCro8N3JgtrOy_KWGEoV_KilRhJO3FxGn6vaR4#:~:text=The%20image%20column%20is%20an,as%20read%20and%20write%20them.&text=Setting%20dynamic%20paths%20for%20the%20pictures%20is%20also%20possible.&text=Now%2C%20Install%20Pillow%20by%20running%20the%20following%20command%20in%20your%20shell)
6. [Downloading files](https://www.youtube.com/watch?v=qKAf5xF6nOE&t=112s)
7. [Dealing with cyclic imports](https://stackoverflow.com/questions/62100550/django-importerror-cannot-import-name-reporterprofile-from-partially-initiali)
8. [How to display a backup image](https://gist.github.com/oscarmorrison/52f9d4b3dfce386c7b11b3fcbdd74dd4)
9. [Help with foreign key issues](https://stackoverflow.com/questions/51380780/django-foreign-key-cannot-assign-must-be-a-instance)
10. [Help updating a blog - this is no longer in the code but I still learnt from it.](https://stackoverflow.com/questions/3681627/how-to-update-fields-in-a-model-without-creating-a-new-record-in-django)
11. [Max value on integer fields](https://stackoverflow.com/questions/30849862/django-max-length-for-integerfield/30850101#30850101)
12. [For loop counter](https://stackoverflow.com/questions/11481499/django-iterate-number-in-for-loop-of-a-template)
13. [Creating empty list in python](https://www.freecodecamp.org/news/python-empty-list-tutorial-how-to-create-an-empty-list-in-python/)
14. [Printing duplicate elements of an array](javatpoint.com/python-program-to-print-the-duplicate-elements-of-an-array)
15. [Filtering null or empty values from a db query](https://chartio.com/resources/tutorials/how-to-filter-for-empty-or-null-values-in-a-django-queryset/)
16. [Limiting a results from a db query](https://stackoverflow.com/questions/13422689/django-how-to-limit-number-of-objects-returned-from-a-model)
17. [Catching a 404 in Django](https://stackoverflow.com/questions/51084909/how-can-i-use-a-catch-all-route-using-path-or-re-path-so-that-django-passes)
18. [Creating a 404 page in Django](https://stackoverflow.com/questions/35156134/how-to-properly-setup-custom-handler404-in-django)
19. [Badge on top of an image](https://stackoverflow.com/questions/34685233/css-badge-over-image-with-bootstrap)
20. [Using session storage](https://developer.mozilla.org/en-US/docs/Web/API/Window/sessionStorage)
21. [Querying a database to find everything except an certain attribute](https://stackoverflow.com/questions/687295/how-do-i-do-a-not-equal-in-django-queryset-filtering#:~:text=While%20you%20can%20filter%20Models,filtering%20using%20the%20Q%20object.)
22. [Whitenoise 500 error](https://stackoverflow.com/questions/53859972/django-whitenoise-500-server-error-in-non-debug-mode)
23. [Catching broken images - jquery](https://stackoverflow.com/questions/92720/jquery-javascript-to-replace-broken-images)
24. [Catching function is not define](https://stackoverflow.com/questions/58088946/getting-uncaught-referenceerror-function-is-not-defined)
25. [Remove colour from navbar toggler](https://stackoverflow.com/questions/50668594/remove-border-color-for-navbar-toggler-hamburger-icon-bootstrap-4)
26. [Adding a decimal to a float](https://stackoverflow.com/questions/16080952/django-cannot-convert-float-to-decimal-first-convert-the-float-to-a-string)
27. This site helped me know which [Frames](https://www.frames.co.uk/picture-frames/popular-sizes) were the right size.
28. This site helped me know which [Canvases](https://blog.365canvas.com/canvas-sizes/) were the right size.

<span id="media"></span>
<ins>Media</ins>

To generate my favicon, I used this website: 

https://favicon.io/emoji-favicons/gem-stone

Below are linked to the images I used for accessory products:
1. [Link to where I got my calendar pictures from](https://www.anchorprint.co.uk/printing-products/calendar-printing/)
2. [Link to the A3 calendar link](http://www.carouselcalendars.co.uk/product/landscapes-of-britain-a4-calendar1)
3. [Link to the website where I got the canvas pictures from](https://www.pngitem.com/so/landscape-canvas-blank/)
4. [Link to the website where I got the photo frame picture from](https://frame-company.co.uk/black-20x16-frame-with-white-mount-cut-for-image-size-a3-165x1175_16.html?gclid=Cj0KCQjw5eX7BRDQARIsAMhYLP-B6_kFkSbISrgxkqcT4Gt0Jw3nnxoGkkXB5xVpLBntA_ngVFYX39caAvm_EALw_wcB)

The photographs all belong to myself or my partner. 

I got my colour scheme from [Canvas](https://www.canva.com/colors/color-wheel/).

<span id="acknowledgements"></span>
<ins>Acknowledgements</ins>  

I'd also like to give credit to Asos and Topshop - as their mobile designs gave me plenty of ideas and helped me to work through some of the more
difficult navigation decisions.


___
<span id="project"></span>
## Project Evaluation





<span id="improvements"></span>
### Improvements




