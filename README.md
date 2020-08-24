# TRAVEL EXPERIENCES

Welcome to TRAVEL EXPERIENCES! Have you ever visited a place you just have to tell everyone about? Or maybe you just want some inspiration on where to travel? Travel Experiences page is just for you. On this page you have the bragging rights and you are welcome to explore others experiences.


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
    * [Left out implementations](#left-out-implementations)
* [Deployment](#deployment)
* [Credits](#credits)
    * [Content](#content)
    * [Media](#media)
    * Acknowledgments and thank you's
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

**There is a chat functionality which is available once user logs in (how difficult is this?) and they can discuss things in real time or as a forum board. **
**optional: creating a tempUser so the visitors can contribute to the travel experiences to test the page and see how it looks without creating a permanent account (difficulty in implementing this?). Plus side is that users can get into the community very quickly. **
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
You can find all the wireframes in the [wireframes](https://github.com/Vlad-404/...) folder.

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
* orange #ff7043 deep-orange lighten-1 - navbar header and footer text
* dark grey #424242 grey darken-3 - navbar header and footer background
* bright green #00e676 green accent-3 - for floating Icons
* green #00e676 green accent-3 - buttons for confirmation, home, add new experience, log in, log out(confirm), update, save, register
* red #f44336 red - for log out(initiate), cancel, delete

### Icons

Icons were used from a FontAwesome page. 

[Backt to top](#travel-experiences)

# Features
As per initial idea, UI has to have uniform and appealing look, be easy to navigate and control your own content. For this reason, multi-page concept was implemented. Thanks to Flask framework, I used templates to cut down on repetitive tasks like header and footer for the page with links to travel agency page. 
* first look at the page needs to invoke intuitiveness. Looking at some examples from #peer-code-review, I found examples of what I want to achieve: 
	- not to overburden the first look with too much information.
	- present the core of the page and when new visitor scrolls down the page, it reveals more features.
	- ease of navigation as more info for each experience has "Read more..." link. 
	- all of the links in the header (navbar) are always accessible (fixed position), user tools are always accessible.
	- search bar is on the home page
*  About page that explains the UI and features
* a choice to show different number of experiences
* search bar
* ability to sort the experiences by country, user and recommendation
* page dedicated to a single experience where people can read about it in more detail
* CRUD functionality: all registered users can Create, Read, Update and Delete content they created
* Google maps API to show the location of the travel
* admin account to remove content that is not suitable for the page and users who are violating the rules acceptable behaviour. Admin will not have the option to modify the users content at any point - only to delete.
* on every page there is a link to a travel agency page so people can get travel arrangements whenever they choose.
* header image is offering different features while slides change and lead to respectable addresses
* floating icon that gives direct access to user tools
* Users can create and delete their account
* Image hosting will be handled by a third-party provider. Users will have to provide the URL to have their pictures displayed as current storage capacities aren't adequate for large number of images. 

## Features left to implement
Due to time constrains, some of the features were left out so the page can be fully functional within the deadline. Afterwards, features can be added:
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

## Frameworks, Libraries and Services
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
## Other tools:
- [Balsamiq](https://balsamiq.com/) 
- [VS Code](https://code.visualstudio.com/) 
- [W3C Markup](https://validator.w3.org/)
- [W3C CSS](https://jigsaw.w3.org/css-validator/)
- [jshint](https://jshint.com/)
- [Google maps API](https://developers.google.com/maps/documentation)
- [Autoprefixer](https://autoprefixer.github.io/)

[Backt to top](#travel-experiences)

# Testing

#### Browser and Device Testing

| **Browser**      | **Device** | **Compatibility**                                            | **Version**            |
| :--------------- | :--------- | :----------------------------------------------------------- | :--------------------- |
| Google Chrome    | PC         |                                                     | Version   |
| Firefox          | PC         |                                                     | Version        |
| Microsoft Edge   | PC         |                                                     | Version    |
| IE 11            | PC         |  | Version  |
| Brave            | PC         |                                                     | Version        |
| Google Chrome | OnePlus 3t  |                                                     |        |
| Opera Touch | OnePlus 3t  |                                                     |        |
| Safari           | iPad   |                                                     | Version           |

- [] Test links to all pages
- [] Test errors by typing in random page redirects
- [] Try to access the user area without signing in
- [] Test filtering dropdowns
- [] Test searching
- [] Test clear search
- [] Tests Read more...
- [] Test account registration
- [] Test create new experience forms
- [] Test add / del experiences
- [] Test add image
- [] Test update experience
- [] Test delete experience 
- [] Test log out 
- [] Test sign in
- [] Test delete profile
- [] Test admin functionalities

[Backt to top](#travel-experiences)

### Bugs during development

How it works:

* This is a description of the bug
    * how I found it
    * what went wrong
    * resolution

List of bugs found:

* wrong country displayed  in home page
    * after submitting a new experience and comming back to the home page, country name was a number instead of full name
    * dropdown menu had ``value`` field which overwrote the country name
    * renamed ``value`` to ``country_id``

* Jinja crashed after clicking on ``Add experience`` button
    * after implementing the filter to show only users experiences in their profile
    * cancel but, which redirected to profile page, didn't had username to refer to
    * added user name for the call in the button

* Odd text appeared on the left side if datamod template was used
    * found it after clicking on ``Read more...``, ``addxp`` and ``editxp``
    * ``if/elif/else`` loop
    * removed if/elif/else loop and set ``block form`` in ``datamod``. This way each form serves the function it's on

* Jinja kept crashing because there was no ``cloud_name``
    * after clicking on New experience
    * ``cloudinary.config`` wasn't set properly
    * found a solution from another student

* Jinja kept crashing after clicking on submit button after experience was edited
    * after submitting changes to experience
    * in ``app.py`` update request had parameter of ``update_one`` instead of ``update``
    * removed ``_one`` from request

* When testing image upload, browser kept notifying about form resubmission. This resulted in repeated image uploads
    * when working on the image upload function
    * browser kept uploading the image each time confirm form resubmission displayed
    * added ``upload_result = None`` to ``imageupload`` function before ``post`` method
...

[Backt to top](#travel-experiences)

## User stories Testing

For users:
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

For business:
1. As a company who owns the travel agency, I want to find places where people want to travel the most so I can make more popular travel arrangements
	* There isn't yet a filter that can sort the countries by most visited, but one of the future implementations is 	a voting system. Subsequently, there will be a feature to sort the experiences by how much votes they have.
2. As a Hotel owner, I want to know if my Hotel was mentioned, so I can improve on my services or add new ones.
	* Using the search tool, anyone can search through the data base and find the term they are looking for.
3.  As a tourist information centre of the city of Zadar, I want to know if anyone has mentioned the city of Zadar, so we can improve on our event offers and advertising.
	* With the search engine, anyone can filter out a desired keyword and read through the experiences that contain this keyword

[Backt to top](#travel-experiences)

# Deployment
The repository for this project is hosted on [GitHub](https://github.com/) and uses Heroku](https://www.heroku.com/) to serve the site to the world wide web. If you would like to contribute to this project you would need to first have some sort of online code editor like [Gitpod](https://www.gitpod.io/) or local such as [VS Code](https://code.visualstudio.com/)] and also some version control software like [Git](https://git-scm.com/), you will also need a GitHub account.

#### Prerequisites

In order to contribute to this repository, you will need to have the following installed:

- Python 3.8.3 or higher
- Git version control
- Code editor - [Gitpod](https://www.gitpod.io/) or [VS Code](https://code.visualstudio.com/) are recommended

#### Development

There are a number of steps required to deploy a local version of this project. 

##### Local copy

- At the top of the repository click on the "Clone or download button"
- Copy the path to the repo "https://github.com/Vlad-404/..."
- Navigate to the folder where you would like to make a copy of this repository -"c:\My Documents\MyRepo\..." and save.
- Start VS Code and click on "File -> Open Folder..."
- Navigate to the downloaded files "c:\My Documents\MyRepo\..." and click on "Select Folder"
- If you don't have your environment set up, please refer to the VS Code documentation
- Install all the dependencies by typing in the terminal: "pip3 install -r requirements.txt"
- If you add or update any new packages to the project use "pip freeze --local > requirements.txt" to update the [requirements.txt](requirements.txt) file with the new dependencies.

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

[Back to top](# Travel-Experiences)
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

## Media 

## Acknowledgments and thank you's

- Huge thank you to [Tim Nelson (tim_ci)](https://github.com/TravelTimN) from Code Institute for redoing flask mini project videos. I used his ``validateMaterializeSelect();`` function to make country field mandatory. You can find it in script.js.
- CI student by the name of [Frozenaught](https://github.com/Frozenaught/homechopped) whose site Homechopped served as an inspiration to my project.
- ...

[Backt to top](#travel-experiences)

# Disclaimer

This page was built for educational purposes and all resources were used under fair usage and/or under free licence! If you find any content that violates the copyrights, please contact me on vmijat21@gmail.com

Thank you for visiting my page and I hope you'll have fun sharing your Travel Experiences.

[Backt to top](#travel-experiences)
