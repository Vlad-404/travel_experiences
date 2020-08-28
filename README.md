# TRAVEL EXPERIENCES

Welcome to **TRAVEL EXPERIENCES!** Have you ever visited a place you just have to tell everyone about? Or maybe you just want some inspiration on where to travel? Travel Experiences page is just for you. On this page you have the bragging rights and you are welcome to explore others experiences.


Contents:
* UX (user experience)
  * [Idea](#idea)
  * [Research and preparations](#research-and-preparations)
  * [Wireframes](#wireframes)
  * [User stories](#user-stories)
  * [Design choices](#design-choices)
    * [Fonts](#fonts)
    * [Colours](#colours)
    * [Icons](#icons)
* [Features](#features)
* [Features left to implement](#features-left-to-implement)
* [Technologies used](#technologies-used)
* [Testing](#testing)
    * [Bugs during development](#bugs-during-development)
    * [User stories Testing](#user-stories-testing)
* [Deployment](#deployment)
* [Credits](#credits)
    * [Content](#content)
    * [Acknowledgments and thank you's](#acknowledgments-and-thank-you's)
* [Disclaimer](#disclaimer)

# UX 

## Idea
Idea behind this project was to create a page where people can exchange their travel experiences. From grand adventures to little tips and tricks on where to dine or a hidden spot that's not so crowded and yet a must visit. 
Scope of this project is to introduce the visitors to the new locations for travel, and let registered users to contribute to the ever-growing base of reviews. 

Purpose of this page is to be as an extension of a future project called Portals to Paradise, which is a page for a travel agency. On Travel experiences, any person can post a review of a place they visited as long as they are registered on the page. This way, visitors and registered users can get an inside view of a place they want to visit. Benefits of this page are:
•	visitors and users can get hands on  recommendations from people who already visited the place.
•	by separating the two pages, it doesn't look like an ad; people are more drawn to social networks than a company trying to push their product. Even as a link, relation to the Portals to Paradise is perfectly placed.
•	travel agency can sort through the user input and decide which travel arrangements to set up and advertise.
Thanks to a modern looking and inviting page which uses Materialize, users are drawn to contribute to the growing base of user experiences.

The first view on the page reveals experiences from random users to showcase the page and give the users idea how the page works. From there on, page is intuitive and simple to use. Even if a visitor has trouble with the page, an about link is accessible from the always visible header.
There's a floating icon where visitors can login, and if they are already logged in, it expands on click and gives them option to log out, access their own profile or add a new experience in 2 clicks.

I chose to make this project because of the following:
* I like to travel.
* By separating this page from travel agency page, people are more comfortable sharing their experiences than on some private company page.
* It creates a feeling of a social network seeing other people and exchanging experiences.
* sense of satisfaction when contributing to the community and having control over your content.
* Making an advertising page that isn't an advert and is actually giving to the users and visitors.
* Useful data for the agency so they can have info on which arrangements to work on.

After visiting this page, users will be encouraged to join the community, have a better idea about the place they want to visit or maybe they would like to contribute.

[Backt to top](#travel-experiences)

## Research and preparations

Before starting this project, some research and these steps were taken:
* looking for a topic and inspiration on the internet, starting with Code Institute's peer-code-review on Slack
* Pages I came across on the internet were sites of companies that payed a professional to write them an article. There's nothing wrong with that, but they give me an impression of an advert which I'm trying to avoid. Ads are becoming more and more intrusive and aggressive. Another reason is, if something's "ad shaped", it was payed to present information in a certain way so there's a bit of scepticism for me. However, these sites gave me some ideas how to structure my own.
* Other sites were either a blog from individuals or a group within a bigger social media page.
* Blogs - as they are sites of individuals, small number of people have a decent exposure while others have to fight for it. Not to mention variety of styles found on different pages. On Travel experiences, everyone is a part of the community and it's easier to find info as everything is uniformed. Users have the liberty to create and modify their own content.
* Social media pages - they have uniform look, nice UI, sense of community but their UI is suited for general purpose. On my page, all the information is about traveling and the UI is tailored for it.
* from this, I decided for the following:
	- page has to have a sense of community
	- the UI needs to serve the purpose of traveling
	- uniform and appealing look
	- ease of navigation and control of your own content
* next, mockups were generated to have an idea how the page will look like on different platforms. You can find them in folder [Wireframes](https://github.com/Vlad-404/...)

### Wireframes

After the initial idea, I decided to make a couple of sketches and make wireframes for different platforms to have an idea how will the page look like on different platforms. Software used for generating mockups was [Balsamiq](https://balsamiq.com/?gclid=EAIaIQobChMIzK-ozrWk6QIVF-vtCh1l-woMEAAYASAAEgJ_vvD_BwE). 
You can find all the wireframes in the [wireframes](https://github.com/Vlad-404/travel_experiences/tree/master/wireframes) folder.

After finishing the project, some of the design and features were changed:
* *show x entries* dropdown with *pagination* for card container has been removed. The center part was imagined as a scroll container where only 6 experiences was supposed to be shown. Due to time constrains, I decided to leave it as a feature left to implement.
* from experiences, map container was removed as it would take too long to implement it. It was also left for future features.


[Backt to top](#travel-experiences)

## User stories

For users:
1. As a new visitor to the page, I want to be able to find an inspiration for my next holiday.
2. As a person who wants to travel to Spain in the Summer, I want to find more information on Barcelona so I can plan with what kind of clothes to wear (going to the beach and to the fancy restaurant is not the same).
3 As a person who is interested in traveling to Mumbai, I want to read more from someone who has already been there.
4. As a user of this page, I want to be able to add and modify my own content so I can present it to the others.
5. As a special needs person, I want to be able to contact the user who has been to Mt. Rushmore so I can find out how wheelchair accessible the place is.

For business:
1. As a company who owns the travel agency, I want to find places where people want to travel the most so I can make more popular travel arrangements
2. As a Hotel owner, I want to know if my Hotel was mentioned, so I can improve on my services or add new ones.
3.  As a tourist information centre of the city of Zadar, I want to know if anyone has mentioned the city of Zadar, so we can improve on our event offers and advertising.

[Backt to top](#travel-experiences)

## Design choices

As I haven't found many examples of what I'm trying to accomplish, I decided to go with subtle colours with small touches of intense ones for certain focus areas. These focus areas are usually navigational elements. For inspirations, I used milestone projects from Code Institutes Slack channel #peer-code-review.

### Fonts

The following fonts were chosen:

- [Permanent Marker](https://fonts.google.com/specimen/Permanent+Marker) - this font is used for titles only (h1). I wanted to use a smooth, curvy, italic font that associated with the feeling of being relaxed as this page is about relaxation and having a good time. It may look a bit rough around the edges, but it's supposed to be leisurely and like it's had enough of rules - at least for a duration of holidays.
- [Oxygen](https://fonts.google.com/specimen/Oxygen) - this font was used for everything else. It's lightness, as name suggests, should give a light note to the whole page. Combining bold and regular styles with different sizes, I can differentiate accents from plain text.
- [Traveling Typewriter](https://www.1001fonts.com/traveling-typewriter-font.html#styles) - used only as names for form entries (Location, Travel arrangements,...) to associate with writing a diary. For credits, see [credits](#credits)
- Calibri - a backup font if others fail to load.

### Colours
I decided to go with minimalism and few colours. Only thing that will have accents in colour is text in navbars, floating icons  and icons at the bottom of the page. Also, pictures posted by users will add some colour.

| Colours       | Hex           | Materialize value  | Used in         |
| :------------- |:-------------:| :-----:| :-----:|
| orange      | #ff7043 | deep-orange lighten-1 | titles, neutral buttons|
| dark grey      | #424242 | grey darken-3 |navbar, header and footer background|
| bright green      | #00e676 | green accent-3 |for floating Icon and some buttons|
| green      | #00e676 | green |buttons|
| red      | #f44336 | red |buttons|
| blue      | #42a5f5 | blue lighten-1 |ad for Portals to Paradise|


### Icons

Icons were used from a [FontAwesome page](https://fontawesome.com/). 

[Backt to top](#travel-experiences)

# Features
As per initial idea, UI has to have uniform and appealing look, be easy to navigate and control your own content. For this reason, multi-page concept was implemented. Thanks to Flask framework, I used templates to cut down on repetitive tasks like header and footer for the page with links to travel agency page. 
* first look at the page needs to invoke intuitiveness. Looking at some examples, I found some features I want to achieve: 
	- not to overburden the first look with too much information.
	- present the core of the page and when new visitor scrolls down the page, it reveals more features.
	- ease of navigation as more info for each experience has "Read more..." link. 
	- all of the links in the header (navbar) are always accessible (fixed position), user tools are always accessible.
	- search bar is on the home page
*  *About page* that explains the UI and features
* search bar
* ability to sort the experiences by country, user and recommendation
* page dedicated to a single experience where people can read about it in more detail
* CRUD functionality: all registered users can Create, Read, Update and Delete content they created
* admin account to remove content that is not suitable for the page and users who are violating the rules acceptable behaviour. Admin will not have the option to modify the users content at any point - only to delete.
* on every page there is a link to a travel agency page so people can get travel arrangements whenever they choose.
* header image is offering different features while slides change and lead to respectable addresses
* floating icon that gives direct access to user tools
* Users can create and delete their account
* Image hosting will be handled by a third-party provider. Users will have option to upload pictures to that service as current storage capacities aren't adequate for large number of images. 

## Features left to implement
Due to time constrains, some of the features were left out so the page can be fully functional within the deadline. Afterwards, features can be added:
* More in-depth user profile page: email, date of birth, location,... This was left out as GDPR requires to inform the users how the data is handled. Incorporating GDPR compliance would take more time, so the users are defined only by user name and password.
* A container that displays the location of the experience.
* Voting system - registered users will be able to add their vote to the experience they find motivating, inspiring, well written, ... This can be used for users to filter out best and worst experiences other people had and either look for a travel arrangement for ones they like, or change their plans. Travel company can use this system to make travel arrangements based on the highest voted experiences.
* Communication between users - On each experience description there will be an option to contact the user who created the experience. Only registered users will have this option. Also, this will also be used if admin has to delete some content and let the user know what they did wrong. 

[Backt to top](#travel-experiences)

# Technologies used

## Languages

* HTML5
* CSS3
* JavaScript
* JSON
* Python

## Others
- [JQuerry](https://jquery.com/)
- [Flask 1.1.2](https://palletsprojects.com/p/flask/)
- [Pymongo 3.10.1](https://docs.mongodb.com/drivers/pymongo)
- [Jinja2 2.11.2](https://pypi.org/project/Jinja2/)
- [Cloudinary 1.21.0](https://cloudinary.com/)
- [Git](https://git-scm.com/)
- [Materialize](https://materializecss.com/)
- [Google fonts](https://fonts.google.com/)
- [Font Awesome](https://fontawesome.com/)
- [Heroku](https://www.heroku.com/)
- [GitHub](https://github.com/)
- [MongoDB](https://www.mongodb.com/cloud/atlas)
- [Balsamiq](https://balsamiq.com/) 
- [VS Code](https://code.visualstudio.com/) 
- [W3C Markup](https://validator.w3.org/)
- [W3C CSS](https://jigsaw.w3.org/css-validator/)
- [jshint](https://jshint.com/)

[Backt to top](#travel-experiences)

# Testing

#### Browser and Device Testing

| **Browser**      | **Device** | **Compatibility**                                            | **Version**            |
| :--------------- | :---------: | :-----------------------------------------------------------: | :--------------------- |
| Google Chrome    | PC         |         Excellent                                             | Version |
| Firefox          | PC         |          Excellent                                           | Version        |
| Opera            | PC         | Excellent | Version  70|
| Brave            | PC         |                                                     | Version        |
| Google Chrome | OnePlus 3t  |                                                     |        |
| Opera Touch | OnePlus 3t  |                                                     |        |
| Safari           | iPad   |                                                     | Version           |

- [x] Test links to all pages
- [x] Test errors by typing in random page redirects
- [x] Try to access the user area without signing in
- [x] Test filtering dropdowns
- [x] Test searching
- [x] Tests Read more...
- [x] Test account registration
- [x] Test create new experience forms
- [x] Test add / del experiences
- [x] Test add image
- [x] Test update experience
- [x] Test delete experience 
- [x] Test log out 
- [x] Test sign in
- [] Test delete profile
- [] Test admin functionalities

[Backt to top](#travel-experiences)

### Bugs during development

**List of bugs found:**

* **Description:** wrong country displayed  in home page
    * **How I found it:** after submitting a new experience and comming back to the home page, country name was a number instead of full name
    * **What went wrong:** dropdown menu had ``value`` field which overwrote the country name
    * **Resolution:** renamed ``value`` to ``country_id`` later replaced the country dropdown menu with Country selector with flags (see [credits](#credits) below)

* **Description:** Jinja crashed after clicking on ``Add experience`` button
    * **How I found it:** after implementing the filter to show only users experiences in their profile
    * **What went wrong:** cancel button which redirected to profile page, didn't had username to refer to
    * **Resolution:** added user name for the call in the button

* **Description:** Odd text appeared on the left side if datamod template was used
    * **How I found it:** found it after clicking on ``Read more...``, ``addxp`` and ``editxp``
    * **What went wrong:** ``if/elif/else`` loop
    * **Resolution:** removed if/elif/else loop and set ``block form`` in ``datamod``. This way each page that has to add, edit and show experiences has it's own form

* **Description:** Jinja kept crashing because there was no ``cloud_name``
    * **How I found it:** after clicking on New experience
    * **What went wrong:** ``cloudinary.config`` wasn't set properly
    * **Resolution:** added ``clodinary.config`` to ``app.py``

* **Description:** Jinja kept crashing after clicking on submit button after experience was edited
    * **How I found it:** after submitting changes to experience
    * **What went wrong:** in ``app.py`` update request had parameter of ``update_one`` instead of ``update``
    * **Resolution:** removed ``_one`` from request

* **Description:** When testing image upload, browser kept notifying about form resubmission. This resulted in repeated image uploads
    * **How I found it:** when working on the image upload function
    * **What went wrong:** browser kept uploading the image each time confirm form resubmission displayed
    * **Resolution:** added ``upload_result = None`` to function``imageupload`` function before ``post`` method

* **Description:** Button for ``New`` didn't work on homepage
    * **How I found it:** After editing image processing pages
    * **What went wrong:** element of type ``button`` had an anchor link which didn't work
    * **Resolution:** converted button element into anchor element with class of ``btn``

* **Description:** Error after updating the experience image
    * **How I found it:** After editing image for experience
    * **What went wrong:** image ``public_id`` wasn't handled correctly
    * **Resolution:** added ``public_id`` variable to ``imgedit``, and to requests

...

[Backt to top](#travel-experiences)

## User stories Testing

**For users:**
1. As a new visitor to the page, I want to be able to find an inspiration for my next holiday.
	* This is fulfilled with just arriving on this page as there are experiences from people presented right on the 	home page. If this isn't enough, there is a search bar right below the banner image.
2. As a person who wants to travel to Spain in the Summer, I want to find more information on Barcelona so I can plan with what kind of clothes to wear (going to the beach and to the fancy restaurant is not the same).
	* User entries cover their own experiences and even if it's not guaranteed a visitor will find something they 	are looking for, they can register and send a message with a direct question.
3 As a person who is interested in traveling to India, I want to read more from someone who has already been there.
	* If a solution from previous user story doesn't work, it is highly likely that someone has already been to 	India and they can use the search feature to read through the experiences or even filter them by country
4. As a user of this page, I want to be able to add and modify my own content so I can present it to the others.
	* this is possible due to MongoDB as all entries are saved there so they can be shared with others and details 	edited afterwards. Some entries cannot be left empty even when editing.
5. As a special needs person, I want to be able to contact the user who has been to Mt. Rushmore so I can find out how wheelchair accessible the place is.
	* User story 2 answer applies here too: after registering/ logging in, user can contact another user and ask a 	direct question.

**For business:**
1. As a company who owns the travel agency, I want to find places where people want to travel the most so I can make more popular travel arrangements
	* There isn't yet a filter that can sort the countries by most visited, but one of the future implementations is a voting system. Subsequently, there will be a feature to sort the experiences by how much votes they have.
2. As a Hotel owner, I want to know if my Hotel was mentioned, so I can improve on my services or add new ones.
	* Using the search tool, anyone can search through the data base and find the term they are looking for.
3.  As a tourist information centre of the city of Zadar, I want to know if anyone has mentioned the city of Zadar, so we can improve on our event offers and advertising.
	* With the search engine, anyone can filter out a desired keyword and read through the experiences that contain this keyword

[Backt to top](#travel-experiences)

# Deployment
The repository for this project is hosted on [GitHub](https://github.com/) and uses [Heroku](https://www.heroku.com/) to serve the site to the world wide web. If you would like to contribute to this project you would need to first have some sort of online code editor like [Gitpod](https://www.gitpod.io/) or local such as [VS Code](https://code.visualstudio.com/). Also you will some version control software like [Git](https://git-scm.com/). For Git, you will also need a GitHub account.

#### Prerequisites

In order to contribute to this repository, you will need to have the following installed:

- Python 3.8.3 or higher
- Git version control
- Code editor - [Gitpod](https://www.gitpod.io/) or [VS Code](https://code.visualstudio.com/) are recommended

#### Development

There are a number of steps required to deploy a local version of this project. 

##### Local copy

- At the top of the repository click on the **Code** button and select *Download zip*
- Copy the path to the repo "https://github.com/Vlad-404/travel_experiences"
- Navigate to the folder where you would like to make a copy of this repository - *"c:\My Documents\MyRepo\..."* and save.
- Start VS Code and click on *"File -> Open Folder..."*
- Navigate to the downloaded files *"c:\My Documents\MyRepo\..."* and click on "Select Folder"
- If you don't have your environment set up, please refer to the VS Code documentation
- Install all the dependencies by typing in the terminal: ``pip3 install -r requirements.txt``
- If you add or update any new packages to the project use ``pip freeze --local > requirements.txt`` to update the [requirements.txt](requirements.txt) file with the new dependencies.

##### Environment Variables

You will need to setup the following environment variables on your system.

| Variable name         | Used for                 | Notes                                                        |
| --------------------- | ------------------------ | ------------------------------------------------------------ |
| CLOUDINARY_CLOUD_NAME | Cloudinary Image package | Found in your Cloudinary account dashboard                    |
| CLOUDINARY_API_KEY    | Cloudinary Image package | Found in your Clouinary account dashboard                    |
| CLOUDINARY_API_SECRET | Cloudinary Image package | Found in your Clouinary account dashboard                    |
| MONGO_DBNAME       | Mongo DB                 | This is the name of your database collection e.g.: "travel_experiences" |
| MONGO_URI          | Mongo DB                 | Found in the connect button on the database cluster          |
| SECRET_KEY        | Session Variables        | This is a unique secret used for cookie encryption,  you can use any random string for this |
| IP                    | Flask                    | You can use `0.0.0.0` here to indicate a local IP address    |
| PORT                  | Flask                    | You can use the default port `5000`                          |



> Note: you will need to add these environment variable to your GitHub repo in "env.py" and Heroku  in "settings -> config vars"

[Backt to top](#travel-experiences)

##### Deployment

The easiest way to deploy the project to Heroku is to set your connect method to GitHub and link the repository master branch. If you set the project up for automatic deploys it will deploy once the master branch is updated.

[Back to top](#travel-Experiences)

Travel Experiences site was developed on GitPod and VS code, using GitHub and Heroku to host the repository. As GitHub pages cannot host dynamic pages, for this purpose I used Heroku.

When deploying Travel Experiences using Heroku, the following steps were made:

Linking the Heroku and GitHub:
* Log in to [Heroku](https://www.heroku.com/) and [GitHub](github.com)
* Make sure you have admin privileges on GitHub
* Go to Heroku and select Travel Experiences app
* Click on Deploy and in Deployment method, select GitHub(Connect to GitHub)
* Select repository to connect to
* Enter repo name in the empty field and click on search. Be sure your repo exists on GitHub and that you typed it in correctly.
* When repo shows click on "Connect"
* Your Heroku app will be synchronised each time you "git push"
* Travel Experiences are now live on Heroku. To run the site, click on "Open App" at the top

[Backt to top](#travel-experiences)

# Credits

Traveling Typewritter font made by [Carl Krull](https://www.onlinewebfonts.com/author/Carl_Krull) from http://www.onlinewebfonts.com oNline Web Fonts is licensed by CC BY 3.0.

## Content
 During development, you will notice users of name test01,test02,... These were my test accounts with which I tested the functionality of the site. Images in these experiences belong to me. Images from other users belong to their respective owners.

## Acknowledgments and thank you's

- Huge thank you to [Tim Nelson (tim_ci)](https://github.com/TravelTimN) from Code Institute for redoing flask mini project videos. I used his ``validateMaterializeSelect();`` function to make country field mandatory. You can find it in ``script.js``.
- CI student by the name of [Frozenaught](https://github.com/Frozenaught/homechopped) whose site Homechopped served as an inspiration to my project.
- Code for coutry selector dropdown in ``addxp.html`` and ``editxp.html`` used from mrmarkfrench and his Country selector project. More info [here](https://github.com/mrmarkfrench/country-select-js).
- code for dynamic image preview for image upload taken from [Webtrickshome](https://www.webtrickshome.com/faq/how-to-display-uploaded-image-in-html-using-javascript)

[Backt to top](#travel-experiences)

# Disclaimer

This page was built for educational purposes and all resources were used under fair usage and/or under free licence! If you find any content that violates the copyrights, please contact me on vmijat21@gmail.com

Thank you for visiting my page and I hope you'll have fun sharing your Travel Experiences.

[Backt to top](#travel-experiences)
