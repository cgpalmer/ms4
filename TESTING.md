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
As a first-time user, I want to easily navigate through the website be able to easily access all of its features. | I expect all of the links to be working and in an intuitive position| All the links take me to their destination and none are broken.
As a first-time user, I want to be able to immediately see what the website is about.                             | I expect information about the website to be ready available on the landing page without needed to click a button | The purpose is very close to the top and the home page gives me all the information I need 
As a first-time user, I want to be able to create an account.                                                     | I expect to be able to fill in the signup form and successfully create and account | I can fill out the form and submit it. I receive feedback if I make a mistake and when I am successful I am taken to my dashboard area. I know it has worked because on the dashboard I can see 'Welcome, (my name)'.
As a first-time user, I want to be able to log in with my new account.                                            | I expect to be able to login to my new account immediately. | After I sign up, I am taken to the dashboard. If I log out I can immediately log in again.
As a first time user, I want to be able to explore the dashboard immediately.                                     | I expect that when I signup, I am taken to the user area (dashboard) immediately. | The result is as expected. I can explore my reports and get into my settings.
As a first time user, I want to be able to add a report regardless of whether I have created an account or not.   | I expect to be able to add a report even if I don't have an account by filling out the add report form. | If I add a report without creating an account, I am still successful. I receive feedback thanking me for my report and I am taken back to the 'add report' screen.
As a first-time user, I want to be able to search reports.                                                        | I expect to click on the search report link and fill in the form to find reports.| I can get to the search page regardless of being a user or not. I can search by location, discrimination or reported reports and it will display my results in a pagination collapsible.
As a first-time user, I want to be able to log out when I am done.                                                | I can click the logout link and no longer be logged in | After clicking the log out link, I am taking to the home page and the options to login or signup reappears on the nav.
As a first-time user, I want my personal details to be private and kept away from the reports.                    | When I search the database for a report, I do expect there to be any of my login details on display | This is as expected - none of my details are on display.
 
User Stories - returning users | Expected outcome | Actual outcome 
--------- | --------------- | ---
As a returning user, I want to be able to log in easily.                                                     | I expect to find the login button easily and be able to fill in the form to login.| I could find the login button easily in the nav bar and the form is very quick to fill in. Once I have logged in I am taken to the dashboard.
As a returning user, I want to search through my own reports.                                                 | I expect to be able to search through my own reports. | I can intuitively search through my own reports in the dashboard over. The collapsible is already open to draw my attention. I filled out the form and I receive the results in the same style as searching the whole database.
As a returning user, I want to be able to add a report and it go into my collection.                          | I expect to add a report and then find it in my results| I clicked the link to add a report in the dashboard and it took me to the same add report link as a new user. Once I had added the report, I could then find it by searching ym reports in the dashboard.
As a returning user, I want to be able to modify one of my reports.                                          | I expect to be able to pick a report and update any of the elements | I could edit any of the reports after doing a search in the dashboard. I can then update any of the elements and, if untouched, the rest stay the same.
As a returning user, I want to be able to delete one of my reports.                                          | I expect to pick a report, click delete and then confirm my delete | I can select any of my reports, click delete, view the report and confirm delete. I am then taken back to the dashboard and receive feedback that my report has been successfully deleted.
As a returning user, I want to be able to change my preferred name.                                          | I expect to be able to changed my preferred name and receive feedback| I can change my preferred name in the settings page, which I can access intuitively from the dashboard. I am informed of my current preferred name before I change the name and then receive feedback once I have changed it to let me know I was successful.
As a returning user, I want to be able to change my email.                                                   | I expect to be able to change the email address associate with my account | Like the password, I can change my email in the settings. When I change the email address, I get feedback to say I was successful. Also, all of my reports have been swapped over to my new email.
As a returning user, I want to be able to change my password.                                                | I expect to be able to change my password securely | I can change my password int he settings page. If I input my old password correctly, I can change my password. I received feedback to let me know I was successful.
As a returning user, I want to be able to delete my account.                                                  | I expect to be able to delete my account and have all my reports deleted with it| My account is deleted and if I search the database none of my reports are there.

General User | Expected outcome | Actual outcome 
--------- | --------------- | ---

As a user, I want to access to all the appropriate features, regardless of what device I am on. 
As a user, I want to be able to explore the products immediately.
As a user, I want to be able to gather information about the products.
As a user, I want to know when I have added something to my basket.
As a user, I want to be able to modify my basket at any point. 
As a user, I want to be able to view my basket at any moment.
As a user, I want to be able to search for different products.
As a user, I want to be able to easily see contact information.
As a user, I want to be able to see a summary of my order before I place it.
As a user, I want to be able to see full size photographs and the quality of them before purchase. 

Retail assistant | Expected outcome | Actual outcome 
--------- | --------------- | ---
As a retail assistant, I want to be able to edit a product.
As a retail assistant, I want to be able to add a product.
As a retail assistant, I want to be able to see the latest 5 orders.

Store Owner | Expected outcome | Actual outcome 
--------- | --------------- | ---
As a store owner, I want to be able to see all of the above.
As a store owner, I want to be able to easily control and manipulate all the data associated with the website. 
As a store owner, I want to be able to easily naviagte to the Django Admin panel.


## Code validation

### Python
To check my python code validation, I have used a combination of 'cornflakes-linter 0.4.0' and http://pep8online.com/
I have configured the cornflakes to accept a line length of 120 characters.
Therefore, the only code issue that comes up on http://pep8online.com/ is that the lines are too long as it is set to 79 characters.

### CSS
CSS has been checked by this online validator: [Jigsaw](https://jigsaw.w3.org/css-validator/ )
When inputted by URL, the only issues are relating to bootstrap.min.
When inputted by direct input, no issues are found but there are some warnings about using the same colour for background and borders. 
These are by design though and intenional.

### HTML
My HTML has been checked on this website: https://validator.w3.org/

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
[Cross Browser Testing]()
