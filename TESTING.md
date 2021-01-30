# Testing

## General testing

### Basic test

1. Nav has been fully tested
2. I have checked that the collapsibles open and close appropriately
3. I have checked buttons enable and disable appropriately

### Feedback from other users

On the whole, I received more feedback than this but they consisted of generic, this margin is too big etc. The following are
mistakes that I had missed.

User 1

* "The search bar is a random length on the mobile view. It doesn't seem like it's lined up with anything?"

Since this, I have changed the nav to a grid so it has more of a purposeful size.

User 2

* "I searched for a really long name and it has caused white space around the margins."

I added the class "word-wrap" to deal with any potential long searches.

User 3

* "The menu items on iOS disappear when I hover over them."

The active class for this item turned the color the same as the background, making it "disappear". I corrected the classes. 

## User stories tests

User Stories - first time users | Expected outcome | Actual outcome 
--------- | --------------- | ---
As a first-time user, I want to easily navigate through the website be able to easily access all of its features. | I expect all of the links to be working and in an intuitive position| All the links take me to their destination and none are broken. Both desktop and mobile screens have the same functionality.
As a first-time user, I want to be able to immediately see what the website is about.                             | I expect information about the website to be ready available on the landing page without needed to click a button | The purpose is very clear in the middle of the jumbotron. There is a 'shop' now button to immediately get started.
As a first-time user, I want to be able to create an account.                                                     | I expect to be able to fill in the signup form and successfully create and account |  I can fill out the form and submit it. I receive feedback if I make a mistake and when I am successful I sent a verification email, which allows me to verify the account.
As a first-time user, I want to be able to log in with my new account.                                            | I expect to be able to login to my new account immediately. | Once my email is verified, I can log in using those details immediately.
As a first-time user, I want to be able to purchase something without having to create and account. | I expect to be able to process a purchase without needing log in. | When I am not logged in, I can still see all of the products. The basket and checkout work and I told I will tell an emailed summary of my transaction.

 
User Stories - returning users | Expected outcome | Actual outcome 
--------- | --------------- | ---
As a returning user, I want to be able to log in easily. | I can find the log in page and it is easy to log in. | The log in page is easily found in the account dropdown and the form is simple, with prompts if I get my details wrong.
As a returning user, I want to be able to modify my delivery details.| There is a convenient place to change my details. | The profile page has a section labelled 'delivery information' and is a simple form to update. 
As a returning user, I want to be able to modify one of my reviews.| There is a convenient place to edit my reviews. | On my profile page, there is a section for editing reviews. I can see all my reviews and choose which to edit, before being taken to a simple 'edit review' form.
As a returning user, I want to be able to add a review.| There is an intuitive method of adding a review. | Below the product summary on the product details, there is a clear link to add a review. It takes me to a very simple form that is easy to use.
As a returning user, I want to be able to delete one of my reviews.| There is a convenient place to edit my reviews. | On my profile page, there is a section for editing reviews. I can see all my reviews and choose which to delete. I receive a warning in case I have pressed delete by accident.
As a returning user, I want to be able to upload one of my own images to use.| There is a convenient place to upload my own images. | I can do this when viewing an accessory product or on my profile page. 
As a returning user, I want to be able to use a previous upload in a purchase.| I can easily choose my photos to be a linked product. | In the linked product select options, when buying an accessory, I can see my own photos above the store's.
As a returning user, I want to be able to see my order history.| There is a convenient place to see my order history. |On my profile page, there is a section for editing reviews. I can see all my older orders. A link on each order will take me to a full summary.
As a returning user, I want to be able to see my previous digital purchases.| There is a convenient place to see my previous digital purchases. |On my profile page, there is a section for purchased products, with a dropdown. There I can see the name of my previous digital downloads and the time they were downloaded.
As a returning user, I want to be able to download my digital purchase.| There is a convenient place to see my digital purchases. |On my profile page, there is a section for purchased products. There I can click to download any of my purchased products. It takes me to a page which has very clear and easy instructions.
As a returning user, I want to be able to change my password.| I can request to change my password. | On the log in page, there is a clear link to reset my password. I fill in my email details, receive a link, where I can simply reset the password. I get a message saying it is successful and I log in again.
As a returning user, I want to be able to log out when I am done.| There is a quick and easy way for me to log out. | Whenever I am logged in, I can click the logout button in the account menu. This takes me to a confirmation page, where I just click "signout". 
As a returning user, I want my personal details to be private. | I do not see any of my personal details after logging out. | All personal details such as basket items, photo lists, profile pages aren't available to me as soon as I log out.

General User | Expected outcome | Actual outcome 
--------- | --------------- | ---

As a user, I want to access to all the appropriate features, regardless of what device I am on. | All the above actions can be done on mobile or desktop. | I can still access all the features on every screen. The most noticable is that the search bar and basket are always visible regardless of the screen size.
As a user, I want to be able to explore the products immediately. | There is an easy way to see the products. | A 'shop now' button and a dedicated nav to the products, makes it very easy for me to find the products immediately.
As a user, I want to be able to gather information about the products. |There is information ready avaiable for each product. | I found that each product has a summary of the information below the picture. When clicked on, each photo also had a breakdown of the reviews as well as all the previous information.
As a user, I want to know when I have added something to my basket. | It is clear that I have successfully added something to my basket. | The basket icon turns flashes blue when an item is added and there is a message at the top of the screen showing success.
As a user, I want to be able to modify my basket at any point. | I can reach my basket easily from anywhere and start editing. | The basket is always on show at the top of the screen. Once I click the icon, I am taken to the basket page where I can click one more button and start editing my order.
As a user, I want to be able to view my basket at any moment. | I can reach my basket easily from anywhere and start editing. | The basket is always on show at the top of the screen. It has a summary of my sub-total. Once I click the icon, I am taken to the basket page.
As a user, I want to be able to search for different products. | The search bar produces different results. | I can search at any time as the search bar is always visible. It tells me how many products it has returned, even if 0.
As a user, I want to be able to easily see contact information. | There is an easy to find place with contact information on. | The footer is included in every page and has all the contact information on.
As a user, I want to be able to see a summary of my order before I place it. | I can see all my items and how much it will cost. | On the checkout page, I can see a full order summary and cost, before getting to the payment section.
As a user, I want to be able to see full size photographs and the quality of them before purchase. | I am able to access the full pictures that I am purchasing. | Nearly every image is clickable and takes me to another window where I can see a high quality image. There are sometimes prompts to remind me of this.

Retail assistant | Expected outcome | Actual outcome 
--------- | --------------- | ---
As a retail assistant, I want to be able to edit a product. | There is a convenient place to edit a product. | The admin page has a select where I choose a product by category. I can the click to edit individual products and fill out an easy form. 
As a retail assistant, I want to be able to add a product. | There is a convenient place to add a product. | The admin page has a link to add a product. I can the click to and fill out an easy form. 
As a retail assistant, I want to be able to see the latest 5 orders. | There is a convenient place to see the latest orders. | The admin page has a select where it shows the last 5 orders. There is a link to the order summary. 
As a retail assistant, I want to be able to delete a product. | There is a convenient place to delete a product. | The admin page has a select where I choose a product by category. I can the click to delete individual products and receive a warning to ensure I want to delete. 

Store Owner | Expected outcome | Actual outcome 
--------- | --------------- | ---
As a store owner, I want to be able to see all of the above. | I have access to all of the web pages. | I do have access to the admin profile page.
As a store owner, I want to be able to easily control and manipulate all the data associated with the website. | I have the ability to edit the way my site works from one page. | Django's CMS covers everything and I have access to it as a Store Owner. 
As a store owner, I want to be able to easily naviagte to the Django Admin panel. | There is an easy way to get to the Django CMS. | On the admin page there is a link to Django's CMS.


## Code validation

### Python
To check my python code validation, I have used a combination of 'cornflakes-linter 0.4.0' and http://pep8online.com/
I have configured the cornflakes to accept a line length of 120 characters.
I had have some warning or 'avoid using null' but each issue that is left is by design. 

### CSS
CSS has been checked by this online validator: [Jigsaw](https://jigsaw.w3.org/css-validator/ )
When inputted by URL, the only issues are relating to bootstrap.min.
When inputted by direct input, no issues are found but there are some warnings about using the same colour for background and borders. 
These are by design though and intenional.

### HTML
My HTML has been checked on this website: https://validator.w3.org/
I checked the HTML by inputting the address. Here is a photo of the [result](static/files/validation/html_validation.jpg)

### Javascript
My javascript has been checked at https://jshint.com/
There are a couple of unused variables which are actually functions but if you remove that from JSHint configure, there are no errors.


## Interesting bugs

Here is a list of interesting bugs that I came across during the project.

1. [Adding a float and a decimal](static/files/testing/interesting_bugs/Adding_float_and_decimal.pdf)
2. [Adding a foreign key value to another model.](static/files/testing/interesting_bugs/Adding_foreign_key_values_to_a_blog_instance.pdf) Please note that this code has since been removed
   but provided a basic understanding that I used for future foreign keys.
3. [Category filter not working.](static/files/testing/interesting_bugs/category_filter_not_working.pdf)
4. [Non unique ID](static/files/testing/interesting_bugs/non_unique_ID.pdf)
5. [Querying the database](static/files/testing/interesting_bugs/querying_the_db.pdf)
6. [Rating not divisible by 0](static/files/testing/interesting_bugs/Rating_not_divisible_by_0.pdf)
7. [Repeated digital download not functioning.](static/files/testing/interesting_bugs/Repeated_digital_download.pdf)
8. [Subtotal error in basket](static/files/testing/interesting_bugs/subtotal_error_in_basket.pdf)



## Cross browser test

I have test my site on Microsoft Edge, Firefox and Chrome web browsers.
I specifically test the following things:
   + Do the collapsibles and their animations open?
   + Does the checkbox still work?
I also tested my website across the different browsers to ensure the CSS and JS held up, which it does. 
[Cross Browser Testing](static/files/testing/performance_testing/cross_browser_testing.pdf)


## Performance Testing

I used Lighthouse on Google Chrome to test the performance of my website. There are clearly areas to improve upon
and most of the seem around loading up the correct scripts as an when needed or image sizes.

Originally, I used PageSpeed insights and received these scores:
[Page speed initial mobile](PageSpeed_initial_mobile.pdf)
[Page speed initial desktop](PageSpeed_initial_desktop.pdf)

I then reduced the size of the images to fit the largest container (see also Image Presentation). I also made sure only
the mobile sized images were loaded on the website and the larger images were available through "href".

I also created different base.html templates, some of which has more specific requirements such as the Stripe JS. By only including
the JS where necessary, I greatly sped up my mobile website and improved my desktop performance. 

For comparison and future development, I also used Lighthouse in Chrome to test the performance of my site. I have included the [mobile test](PageSpeed_latest_mobile.pdf)
and [desktop test](PageSpeed_latest_desktop.pdf)

Clearly the numbers are not green yet and there is still work to be done to make the experience optimal for users for the landing page. I tried to
reduc the image size for the jumbotron but the lack of quality distorted the image and mde little difference in speed.

However, whilst the landing page still has some improvements, the actual loading of the products page is excellent. My efforts to reduce the
image sizes and remove unnecessary cdn's has brought the products and product detail pages to a very high score. I also used lazy_loading() to really
push the experience for the mobile user. The reports are available here:

[Mobile products](Lighthouse_latest_mobile_products.pdf)
[Mobile product details](Lighthouse_latest_mobile_product_detail.pdf)
[Desktop products](Lighthouse_latest_desktop_product.pdf)
[Desktop product details](Lighthouse_latest_desktop_product_detail.pdf)