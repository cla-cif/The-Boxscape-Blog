<h1 align="center" id="top">THE BOXSCAPE BLOG</h1>

__You can find the live link here: [BOXSCAPE](https://the-boxscape-blog.herokuapp.com/)__

The Boxscape is a blog for people whose ideas break out of the box (escape), it's a place for independent thinkers who analyses situations, rather than conforming to public opinion. At Boxscape, we believe in freedom of expression and in respecting the opinions, identities, preferences, religions and cultures of others. We like people who contribute to making this a safe space.

The blog has a simple interface, it's intuitive and easy to use. Normal visitors can enjoy the blog in Read-Only mode but logged-in members can post, comment, like or dislike post. We all change our mind at times and so do our members which can edit and delete their posts and comments.  

__Note__: New Posts and Comments won't appear immediately as they are subjected to admin review before being pubblished. Edited Posts and Comments will disappear from the page until reviewed. 

The Bosxcape blog hears its members and visitors wich can send an email to the staff by filling up the form reachable from the Contact Us link at the bottom of the page. 

 __Our promise__
In August 2022, the blog appeared in its first version. It offers the essential functions that every blog should have. We decided not to go overboard because we want to grow with our community and tailor the Boxcape to the needs of our members.

![Landing page](https://github.com/cla-cif/The-Boxscape-Blog/blob/main/screenshots/landing_page.png)

## Content
- [Features](#Features)
- [User Experience](#User-Experience-(UX))
- [User Interface](#User-Interface-(UI))
- [Developer Experience](#Developer-Experience)
- [Technologies used](#Technologies-used)
- [Testing](#Testing)
- [Bugs and future developments](#Bugs-and-future-developments)
- [Deployment](#Deployment)
- [Credits](#Credits)
- [Extra](#Extra)

## Features 
A coincise description of the functionalities featured in each page and a comprehensive list of common features (UI/UX, navigability, services from PaaS)

### Existing Features - Home page

- __Header__

  - The Header contains the logo with a caption (Boxscape - a blog for independent thinkers), and links to the about page, home page (also reachable by clicking on the logo image). If the user is not authenticated, links to login and register page will be displayed, otherwise the log out link will be shown. The header's text is Pantone [very- peri](https://www.pantone.com/articles/press-releases/introducing-pantone-17-3938-very-peri-pantone-color-of-the-year-2022) colour of the year 2022 on a light lilac background. 
 
  The header sticks to the top and resizes on medium and small screens to accomodate the useful links. 
 
![Header](https://github.com/cla-cif/The-Boxscape-Blog/blob/main/screenshots/header.png)

- __Main section__

  - A list of posts paginated by 9 in a 3x3 layout. 
    - Each post is presented as a card showing an image, tags, author, pubishing date, title and an excerpt of the article. The post will be shown in detail by clicking on the image, title or excerpt. 

    __Note__: In case the user decides not to submit an image, a default placeholder will be shown instead consisting on the blog's logo against an orange background.
    
    - Any tag is a clickable link that will show other posts under the same tag.
   - A Sidebar section containing 5 boxes:
        - A welcome message and a brief reminder of the blog's essential code of conduct with a bright orange button inviting user to post. The button lands to a form for submitting a post.
        - Link to a Feed RSS.   
        - A list of the most relevant (aka most commented) posts. 
        - A list of the most recent posts. 
        - Some numbers (which we would like to see grow) counting the number of posts, members, comments and authors. 

     The sidebar collapses on medium and small screens and a 'hamburger' animated button is showed instead. The sidebar can be opened and closed from there.

![Sidebar](###)

- __The Footer__ 

  - The 'Footer' shows a list of white links ona very-peri background to:
    - About us page written by the Boxscape founder. 
    - Links to Twitch and Twitter (a Boxscape account will be hopefully opened soon) and to the RSS feed. 
    - Link to the contact us form (we promise no email will be unanswered)

   The footer sticks to the bottom.
   
    __Note__: Header and Footer are consistent on every page. The sidebar is accessible from the main page only. 
  
![Footer](https://github.com/cla-cif/The-Boxscape-Blog/blob/main/screenshots/footer.png)

### Existing Features - Post Detail page

- __Post section__

  - The section contains:
    - the header area with the title, the blog logo, the author and the publishing date. 
    - The article enclosed in quotation mark
    - The reaction buttons:
        - a clickable heart to like the post (a second click will undo) and its counter.
        - a clickable broken heart to dislike the post with the same functionality.
        - a comment counter.

      if the user is authenticated and owns the post:
        - a delete button which will open a popup message asking for confirmation to delete the post.
        - an edit button which will get a form with the editable elements of the post.

- __Comment Section__
    - if comments are present a large title and a counter will show how many of them there are.
    - if comments are not present the counter will display 0 and some text will invite the user to be the first one to comment.
    - the list of comments (edit and delete options will be present for the authenticated user who owns the comment). 
    - the comment box a large text field and a bright orange submit button. 

- __Suggested Posts__
    - a list of posts labelled with the same tag presented as small cards with the post image, title and author. Similar to the post list in the main/homepage but simpler. 

    All the above elements are presented in a white box against a pale lilac background. Header and footer mantain the same proprtions as in the main page. The elements are consistent with the blog's colours and style. 

![Post Detail](https://github.com/cla-cif/The-Boxscape-Blog/blob/main/screenshots/post_detail_crop.png)

### Existing Features - Create a post and Edit a post pages
- The two pages have a similar layout, a centered well organized, minimalistic form that allowes authenticated users to create or edit a post they own. At the bottom a large orange Submit button.  
- The field forms include Title, tags, image, excerpt, body (the actual content of the post). 
__Note__: Pending the implementation of a cloud based service where to store the images, the members are allowed to submit a web link to an image. 
    - The link will be validated, a message reminds the user to upload link to images in .jpg, .png, .gif format. 
    - A feedback warns the user in case of unsupported link and prevents submission. 
    - The image will be shown as the featured image in the post list. 
- The form to create a post is accessible from the home page. All registered and logged in members can post. If the visitor is not logged in, instead of the form, a message will remind the user to log in before posting. 
- The Edit Post option accessible from the Post Detail page by the authenticated owner, displays a pre-populated form on a separate page with the post fields. Tags are not editable by the user. 
- All actions recevie a feedback message.
- Users can undo their actions before submissions and be redirected to the main page by clicking on the Discard button. 
- The user is automatically redirected to the main page after 2.5s. 
- Edited and newly created posts won't appear before admins' approval. 
![Create a post](https://github.com/cla-cif/The-Boxscape-Blog/blob/main/screenshots/create_post.png)

### Existing Features - Create and edit comments
- It's possible for authenticated users to comment a post using the box right under every post (Post Detail page). 
- It's possible to edit only one's own comments from the list of comments pertaining to the post. The edit functionality is presented as a pre-populated field on a separate page. 
- All actions recevie a feedback message.
- Users can undo the comment editing before submissions and be redirected to the main page by clicking on the Discard button. 
- The user is automatically redirected to the main page after 2.5s after editing a comment. 
- Edited and newly created comments won't appear before admins' approval. 
![Create Comment](https://github.com/cla-cif/The-Boxscape-Blog/blob/main/screenshots/create_comment.png)

### Existing Features - Delete functionalities
- The logged in users can delete their own posts and comments from the Post Detail page. 
- A pop up message asks users to confirm (or not - there's a "take me back" button) their choice as the action is not undoable. 
- Posts and comments are deleted immediately.
![Delete Post](https://github.com/cla-cif/The-Boxscape-Blog/blob/main/screenshots/delete_post.png)

### Existing Features - Contact us page
- The contact us page presents a form, similar in style to all the other forms across the blog, with the following mandatory fields: name, email, message. 
- Admins will receive the messages on the.boxscape.blog@gmail.com
![Contact us](https://github.com/cla-cif/The-Boxscape-Blog/blob/main/screenshots/contact_us.png)

### Existing Features - Log in, Log out, Register page
- These functionalities are provided by [allauth!](https://django-allauth.readthedocs.io/en/latest/) a library containing a set of Django applications addressing authentication, registration, account management as well as 3rd party (social) account authentication. For the purposes of this blog only log in, log out and register functionalities were implemented. 

### Existing Features - Common

- __UI/UX Features__ 

    -   Responsive on all device sizes. How it looks like on iPhone 12: [Home page](https://github.com/cla-cif/RPS-Lizard-Spock/blob/main/assets/screenshots/Homepage%20layout%20on%20iPhone%2012.jpg) / [Post Detail page](https://github.com/cla-cif/RPS-Lizard-Spock/blob/main/assets/screenshots/Support%20page%20layout%20on%20iPhone%2012.png)

    -   Accessible for users with hearing and visual impairments.
    -   Interactive elements and animated buttons.
    -   All user actions will receive a feedback (successfully submtted posts and comments waiting for approval, successful login, email sent)
    -   All delete actions require a double confirmation. 

![Home page screenshot from createmockup.com](https://github.com/cla-cif/The-Boxscape-Blog/blob/main/screenshots/responsive_mockup.png)

- __Other features__ 
    - The website is deployed on Heroku [here](https://the-boxscape-blog.herokuapp.com/)
    - The website's static files are hosted on [Cloudinary](https://cloudinary.com/)
    - The emails are sent via [AWS SimpleMail](https://aws.amazon.com/ses/)
    - The website has a "Google site verification" to verify the website's ownership as shown [here](####).
    - Browsers can crawl the website thanks to a robots.txt file and a sitemap.xml. 
    - The website has an [apple-touch-icon](###) with the blog main logo (an open box laying on its side) to make the page stand out from other bookmarks
    - The same [symbol](###) was chosen to create a 'favicon' and make the home page easy to find among the many open tabs. 
    - The site has keywords and a description of appropriate length to give the user a brief impression of the site on the browser results page.

### Features to implement
- Reply to comments and create chain of comments. 
- Like or report comments.
- Edit comments "on the same page". 
- Subscription to the newsletter.
- Bookmark pages to access easily the favourite posts. 
- Share posts via email and social networks.
- Extend the range of allowed image formats and use a Cloud service for storage. 
- Add privacy policy and copyright information. 
- Get the website a domain name. 
- Authentication with social media. 
- Reset password functionality. 

## User Experience (UX)
User Experience is how a user interacts with and experiences a product, system or service. It includes a person's perceptions of utility, ease of use, and efficiency and how you feel about the interaction. 

### User stories

- __First-time Visitor Goals__
    - As a First-time visitor, I want to explore the blog, read the posts and contact the admins if I have any enquiry. 
        -   The layout is simple, the icons are intuitive, all essential information are displayed.
    - As a First-time visitor, I want to learn more about the blog and its founder
        - The About page is easily reachable from the Header and Footer links as well as the option to send and email to the admin through a simple form.
    - As a First-time visitor with an impairment, I want to be able to read all the text by myself or with a screen reader and find colours that are not misleading.
        - Colours contrast with the background and are colour blindness friendly as information is still clear regardless of visual impairment.
        - Font sizes are sufficiently large by default and therefore easy to read.
        - All text, labels and images are readable with the Chrome Screen Reader extension.
        - Animations are disabled when the user sets the “prefer reduced motion” option. 
        
- __Returning Visitor Goals__
    - As a returning visitor, I want to find the same blog philosophy but with advanced features. 
        - The first version of this website was deployed on August 2022, the developer strives to work on the webiste and improve its usability.
    - As a returning visitor with a disability, I want to find the same or even better accessibility than before.
        - Accessibility will be kept up to date in accordance with the latest guidelines and users’ feedback.

### Wireframes 
The site is designed with an intuitive layout, it is accessible, easy to browse, and minimalistic.
- [Balsamiq](https://balsamiq.com/) was used to put "ideas on paper". 
    - Home page | Detail Post | Generic Form template: ![Desktop view]https://github.com/cla-cif/The-Boxscape-Blog/blob/main/screenshots/all_wireframes.png()

### Improvements
- Enable Gzip compression for a faster loading and why it's [important](https://blog.hubspot.com/website/gzip-compression)
- Continuous research to identify the users goals, needs, behaviors, and pain points involved with the Boxcape blog interaction.
- Perform more tests as the project grows.

## User interface (UI)
UI refers to the screens, buttons, toggles, icons, and other visual elements that users interact with when using a website, app, or other electronic device.  

### Design

- __Colours__
    The five main colours used are a pure of white, light lilac, Pantone's very-peri, an energising shade of orange and olive green.
    The choices of colour reflect the blog's energy, creativity, spiritely and dynamic attitude. To achieve an optimal contrast all the blog elements cotaining text are encapsulated in a total white box. Text colour is black for all the the blog-related content (articles and comments). Veri-peri is the colour of choice for the details and side-text.

- __Typography__
    The font "Roboto" from Google Fonts was chosen for its modern and clean style. 

- __Shapes__
    The shapes are squared and neat to recall the geometry of a Box. The lines are simple and clean. 

- __Interactive elements__
    - The sidebar collapses on medium and small screens and a button will appear instead. The round button will toggle the sidebar on the left. The only option available will be _Create a post_  while all the others will be hidden due to space reasons.
    - On hover the orange buttons used to confirm actions will turn very-peri and the innert text white.
    - On hover the headers link and the post title turn orange while the post image will briefly lose its transparency.

### Improvements
Always on the lookout for better design, layouts, colour palettes, fonts, smoother interactive elements. 

## Developer Experience
This project is inspired to the [Agile Principles](https://www.agilealliance.org/), planned according to the [Design Thinking](https://canvas.unl.edu/courses/73802/pages/5-stages-of-design-thinking) process and organized following the [Kanban method](https://kanbanize.com/kanban-resources/getting-started/what-is-kanban#:~:text=The%20Kanban%20method%20is%20designed,due%20to%20fear%20or%20uncertainty.) through the GitHub Project tool. 

### Agile approach
Here are some of the guiding principles behind the [Agile Manifesto](https://www.agilealliance.org/agile101/12-principles-behind-the-agile-manifesto/) and how they were implemented.
1. __Our highest priority is to satisfy the customer through early and continuous delivery of valuable software__
The project is ready in all it's essential features it means that a user can create, read, update and delete Posts and Comments (Read about [CRUD](here)) as long as some other minor features (like and dislike a post). From now on any further stable implementation will be immediately available to the users.
2. __Welcome changing requirements, even late in development. Agile processes harness change for the customer’s competitive advantage.__
Despite late changes can be demanding as they might involve quite a long list of alteration that span across several files, adapt to users requests is essential for a project to be appreciated. An example was switching from CKEditor to Summernote, the first app is incompatible with the main requirement to deploy the project on Heroku.
3. __Deliver working software frequently, from a couple of weeks to a couple of months, with a preference to the shorter timescale.__
Now that the main architecture is in place, new scalable features can be added _step by step_. Some will require a reasonably short amount of time like "liking comments" others require a longer adaptation (implementing the REST Framework). 
4. __Business people and developers must work together daily throughout the project.__
The developers promise to the users is to comunicate often and efficently, primarly through the blog's dedicated email box and to ask for feedback.
5. __Simplicity–the art of maximizing the amount of work not done–is essential.__
The blog is now on its initial version, the basic features are in place but many more are just around the corner (See the list of [Features to implement](#Features-to-implement))

### Design Thinking process
The project's features are planned using Users'stories built around a 'blog reader' _persona_.
- __Define__
    > I like reading blogs and engage with the ones I like most. I want to contribute to the blog by writing some articles or forwarding to the admins complaints and suggestions. I want to engage in discussions with other members by commenting posts and replying to comments. I want to express appreciation by upvoting or downvoting a post. I also would like and easy login through my favourite social apps. 

- __Empathise__
I tried to understand what the potential readers may want from Boxscape by thinking as a blog reader myself. To do this, I researched blogs and conducted interviews that led to the creation of a potential user persona.
I then implemented a solution keeping this question in mind: _"What solves the problem according to the reader's needs and goals?"_ 
    __Let us call our reader Nastia.__

- __Ideate__
The brainstorming phase followed by research, challenges and discussions lead to the integration of the following tools to find a solution to the stated problem. 
    - [Django](https://en.wikipedia.org/wiki/Django_(web_framework)) and its apps are ideal for creating a simple blog.
    - The Heroku-based app provides an easy-to-use solution to deploy a project (What is [Heroku](https://en.wikipedia.org/wiki/Heroku))
    - [GitHub](https://en.wikipedia.org/wiki/GitHub) is the go to solution to host a repository.
    - [Boostrap](https://getbootstrap.com/docs/5.0/getting-started/introduction/) for the front-end design of the project as it's easy to use, responsive, consistency and browser compatibility.
- __Prototype__
And that is how I arrived at the [current version](###). It is a scaled-down version of a fully functioning blog ready to become a thriving comunity with hundreds of daily readers.
Other important points took into account:
  - Design consistency across pages.
  - Constant availability of information and functions.
  - Creation of a solid architecture for future scalability.
  - Handling of invalid inputs and the avoidance of unexpected behaviour. 
 
  >My personal challenge was to put myself in the shoes of the user: What is clear, obvious and self-evident to the developer may not be to the user.

- __Test__
I brought together people who matched the _persona_ aka our blog reader Nastia. 
I presented the initial release of the blog to them and asked them to comment and raise questions while browsing the blog.
I listened to their comments, observed their reactions, took notes and showed my appreciation for their feedback. 
 >I then used their feedback to go to-and-fro the Design Thinking stages.

### Kanban board
A Kanban-like board based on the User Stories was set using GitHub Project tool and divided in:
To Do | In progress | Done | Issues | Future features 
Have a look at my board [here](https://github.com/cla-cif/The-Boxscape-Blog/projects/1)

## Technologies used
A list of programming languages, frameworks, SaaS, PaaS, Softwares used to develop Boxscape. 

### Languages

-   [HTML5](https://en.wikipedia.org/wiki/HTML5)
-   [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
-   [JavaScript](https://en.wikipedia.org/wiki/JavaScript) and it's library [jQuery](https://en.wikipedia.org/wiki/JQuery)

### Frameworks
- [Django](https://en.wikipedia.org/wiki/Django_(web_framework)) and some of its installable applications:
    - [allauth](https://django-allauth.readthedocs.io/en/latest/) for quick users authentications, 
    - [widget-tweaks](https://pypi.org/project/django-widget-tweaks/) for form fiels rendering
    - [cloudinary and cloudinary storage](https://pypi.org/project/django-cloudinary-storage/) to facilitate integration with Cloudinary.
    - [crispy forms](https://pypi.org/project/django-crispy-forms/) for better form rendering. 
    - [summernote](https://github.com/summernote/django-summernote) to style the articles from the create and edit post forms.
    - [taggit](https://pypi.org/project/django-taggit/) to cathegorize posts with tags. 
    - [django-humanize](https://pypi.org/project/django-humanize/) to show the post creation date in a more user friendly way. 
    - [crispy-bootsrap](https://pypi.org/project/crispy-bootstrap5/) to facilitate integration with Bootstrap5.

- [Bootsrap](https://getbootstrap.com/docs/5.0/getting-started/introduction/) to enhance the project responsivness, design and features.

### Platforms 
- [Gitpod](https://www.gitpod.io/) Gitpod Dashboard was used to write the code and its terminal to 'commit' to GitHub and 'push' to GitHub Pages.
- [GitHub:](https://github.com/) To store the project code after being pushed from Gitpod.
- [Heroku](https://en.wikipedia.org/wiki/Heroku) To deploy this project

### Services
- [AWS Simple Email:](https://aws.amazon.com/ses/) To implement the Contact us functionality
- [Gmail:](https://en.wikipedia.org/wiki/Gmail) To create the Blog's email address the.boxscape.blog@gmail.com
- [Cloudinary:](https://en.wikipedia.org/wiki/Cloudinary) To store the static files of this project and potentially upload pictures of posts created from Django's admin panel. 

### Libraries
- [Google Fonts:](https://fonts.google.com/) To import the 'Roboto' font into the HTML pages  
- [Font Awesome:](https://fontawesome.com/) To import the post button icons and logos of the social networks.

### Software
- [Balsamiq:](https://balsamiq.com/)
    - Balsamiq was used to create the [wireframe](https://github.com/cla-cif/english-with-claudia/blob/main/screenshot/index-wireframe.png) before the deployment process began.
 

## Testing 
This paragraph includes Django testings, general testing for SEO and accessibility parameters and common language validators.

### Django Testing
Some blog's basic functionalities have been subjected to automatic testing using [model bakery](https://model-bakery.readthedocs.io/en/latest/) to test the creation of instances on a temporary test database and test on those instances the delete function. Also were tested urls and views with the Django built-in [testing](https://docs.djangoproject.com/en/4.0/topics/testing/overview/). 

### General Testing 

The website's features were thoroughly tested using some well-known free web testers. Both pages (home page and support page) were tested.

- __Web Responsiveness__
    - The responsive feature has been tested using Chrome DevTools and an online Web Design checker from [Media Genesis](https://responsivedesignchecker.com/). 
Here is the [result](https://responsivedesignchecker.com/checker.php?url=https%3A%2F%2F8000-clacif-theboxscapeblog-psrjys8p4b8.ws-eu59.gitpod.io%2F&width=1400&height=700).
The website's layout has been tested on a range of different screen sizes, from small 320x480 screens (e.g. Apple iPhone 3) to widescreen 24" and their landscape view providing a good user experience. 
    - The website has passed the [Google mobile-friendly test](https://search.google.com/test/mobile-friendly/result?id=ZZfvk8iiRDYc3lIXuuDzoA).

- __Accessibility__

  - __Colours:__ All colours checked with [WebAim](https://wave.webaim.org/report#/https://the-boxscape-blog.herokuapp.com/) orange text on white background especially if small presents low contrast. 
  - __Reduced motion:__ All animations are disabled when "Show animation in Windows" is disabled from settings in Win10. 
  - __Colour blindness:__ Colour-blind webpage filters have been taken into account with [Toptal](https://www.toptal.com/designers/colorfilter/) e.g. Here is how the website looks like for users affected by [Protanopia](https://www.toptal.com/designers/colorfilter?orig_uri=https://the-boxscape-blog.herokuapp.com/&process_type=protan)
  - __Screen Reader:__ Texts, links and images' 'alt text' were read with the Google Chrome extension Screen Reader (version 53.0.2784.13). 
  - __Presbiopia:__ All fonts are 'sans serif' and the essential elements have a sufficient size so that the text can be easily read without glasses.
  - __General Accessibility:__ has been tested with satisfactory results on:
      1. Google Light House (mobile and desktop version). 
      2. [Power Mapper - Home page](https://www.powermapper.com/) showing minor issues. 
      3. [Wave - Home and Support pages](https://wave.webaim.org/report#/https://the-boxscape-blog.herokuapp.com/).

- __Browser Compatibility__
    - The website's pages were tested with [Power Mapper](https://www.powermapper.com/) no compatibility issues were found.[See](https://try.powermapper.com/demo/Report/6fbfbb33-b889-41df-8ead-c60b95ab9f41)

- __SEO__
  - The website's Home page was tested on [Seobility](https://www.seobility.net/en/seocheck/) and even better results were achieved on post details pages. [Follow for results](https://freetools.seobility.net/en/seocheck/check?url=https%3A%2F%2Fthe-boxscape-blog.herokuapp.com%2Fthe-inner-life-of-cats%2F&crawltype=1) [and](https://freetools.seobility.net/en/seocheck/check?url=https%3A%2F%2Fthe-boxscape-blog.herokuapp.com%2F&crawltype=1)
  - Tests ran with Google Light House (mobile and desktop version) on both pages obtained a SEO score of 100%.

- __Performances__
  - The website was tested on [Power Mapper](https://www.powermapper.com/) see results [here](https://try.powermapper.com/demo/Report/6fbfbb33-b889-41df-8ead-c60b95ab9f41).
  - The general performance was evaluated by [GTMetrix](https://gtmetrix.com/) see results [here](https://gtmetrix.com/reports/www.powermapper.com/x3lYl49t/).

### Validator Testing 

- HTML
  - No errors were returned when running the official [W3C validator](https://validator.w3.org/). [Results here](https://validator.w3.org/nu/?doc=https%3A%2F%2Fthe-boxscape-blog.herokuapp.com%2F)
  __Note__: Errors were naturally raised by Django Template Tags implemented in the HTML files and filtered out.
- CSS
  - No errors were found when running the official [(Jigsaw) validator](https://jigsaw.w3.org/css-validator/). [Results here](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fthe-boxscape-blog.herokuapp.com%2F&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en).
  __Note__: Many parameters such margins and paddings are set in the HTML files as standard Bootstrap classes. 
- JavaScript
  - The code passed through [JSHint](https://jshint.com/) with no issues. 
  __Note__: The project needed just few scripts which were embedded in the HTML files.
- PEP8
    - The code passed through [PEP8](http://pep8online.com/) with no issues.
    __Note__: The code was constantly monitored and linted according to the GitPod integrated [Pylint](https://en.wikipedia.org/wiki/Pylint) (some options were customized from the pylintric file)

## Bugs and Future developments
A brief description of some fixed and unfixed bugs arose during the developing process. This section also contains ides for further development.

### Fixed Bugs

- ##  
     - __Description__ : A post featuring a unique tag (a new tag that has not been used before by other posts), on request will throw a NoneType error.
     - __Bug__: This is due to a reverse query on tags ids: when querying a reverse foreign key, None appears for tags not having any post. Documentation about django [values_list](https://docs.djangoproject.com/en/4.0/ref/models/querysets/)
     - __Fix/Workaround__: The issue was due to a bad query filtering post under the same tag and excluding the post itself.  ``` similar_posts = Post.objects.filter(tags__in=post_tags_ids).exclude(id=post.id) ``` Fix by removed the .exclude function. 
    
- ##   
     - __Description__: Application preventing successful deployment on Heroku. 
     - __Bug__: The issue was due to a bad compatibility between Heroku and Django CKEditor installed to style the post content from the admin panel, create and edit form.
     - __Fix/Workaround__: Django [summernote](https://github.com/summernote/django-summernote) was installed instead.
     
- ##   
     - __Description__: Can't update or upload pictures to cloudinary when editing or creating post but if I upload the picture when creating a post from the admin panel, it will show correctly.
     - __Bug__: Bad compatibility or wrong settings. The attempts to fix the bug became more time consuming than working on a fix.  
     - __Fix/Workaround__: While still researching for a better cloud service to fulfill the functionality, the image will be rendered and edited from a CharField after being validated by a suitable RegEx allowing urls ending with .gif .jpg .png and/or a querystring. 
     __Note__: the above workaround is intended a temporary workaround as url links are subjected to changes and won't be as reliable as a cloud storage service. 

### Unfixed Bugs
- For now the user can't edit the tags from their own posts in the edit form due to a non-user-friendly display of the tag list presented as a Django queryset: tags are wrapped in square and rounded parenthesis as a _values_list_. 

### Future Developments
- Relying on the Django REST Framework for advanced functionalities (better defined m2m relations, serializers, authentications)
- Wider use of API and cloud based services for content delivery and archiving (like [AWS](https://aws.amazon.com/))
- Fix or improve any other issue highlighted by user. 

## Deployment
The project is coded and hosted on GitHub and deployed with [Heroku](https://www.heroku.com/). 

### Creating the Heroku app 
The steps needed to deploy this projects are as follows:

1. Create a `requirement.txt` file in GitHub, for Heroku to read, listing the dependancies the program needs in order to run.
2. Set `DEBUG=False` from the `settings.py` file when switching from production to deployment environment.
3. `push` the recent changes to GitHub and go to your [Heroku account page](https://id.heroku.com/login) to create and deploy the app running the project. 
4. Chose "CREATE NEW APP", give it a unique name, and select a geographical region. 
5. From the _Settings_ tab, configure the environment variables (`CONFIG VARS` section).
6. Make sure to disable `COLLECT_STATIC` from Heroku `CONFIG VARS` here's [why](https://vonkunesnewton.medium.com/understanding-static-files-in-django-heroku-1b8d2f003977).
7. For this project I had to set other `CONFIG VARS` for AWS, Cloudinary, Postgres DB. 
8. Create another config var, set `PORT` as KEY and assign it the VALUE `8000`.
9. Add    `heroku/python` buildpack from the _Settings_ tab.
10. From the _Deployment_ tab, chose GitHub as deployment method, connect to GitHub and select the project's repository. 
11. Click to "Enable Automatic Deploys " or chose to "Deploy Branch" from the _Manual Deploy_ section. 
12. Wait for the logs to run while the dependencies are installed and the app is being built.
11. The mock terminal is then ready and accessible from a link similar to `https://your-projects-name.herokuapp.com/`

### GitHub Pages
- A video showing how a similar repository was deployed is available [here](https://github.com/cla-cif/RPS-Lizard-Spock/blob/main/assets/screenshots/create-publish-repository.mp4). 
- The site has been deployed on GitHub pages. The steps to deploy and publish the repository are as follows: 
    - Create a new repository:
        - Click on "New" button (top-right of the page). 
        - Select the "Owner" (your account for instance). 
        - Chose a Repository name. Note: The name must be unique among all the user's repositories and words must be separated by hypen. 
        - The repository will be "public" by default. Note: a "private" repository can't be hosted on [GitHub pages](https://pages.github.com/).
        - Click on "Create Repository". 
        - The page will refresh and the Repository is successfully created. 
     - Host repository on GitHub Pages:
        - Click on "Settings" (top-right of the page).
        - Click on "Pages" (menu on the left). 
        - Select branch > main from the "Source" section. (or any other if present). 
        - Click on "Save", the page will refresh and the site, now hosted on GitHub Pages is ready to be published. 
        - After a few minutes, the ribbon will turn green and the site is reachable at an address similar to your-username/.github.io/your-repository-name/. 
        - Develop the project, commit, push and the changes will be visible on the page within a few minutes. 

### Forking the Repository

- By forking this GitHub Repository you make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original repository. The steps to fork the repository are as follows:
    - Locate the [GitHub Repository](https://github.com/cla-cif/The-Boxscape-Blog) of this project and log into your GitHub account. 
    - Click on the "Fork" button, on the top right of the page, just above the "Settings". 
    - Decide where to fork the repository (your account for instance)
    - You now have a copy of the original repository in your GitHub account.

### Making a local clone

- Cloning a repository pulls down a full copy of all the repository data that GitHub.com has at that point in time, including all versions of every file and folder for the project. The steps to clone a repository are as follows:
    - Locate the [GitHub Repository](https://github.com/cla-cif/The-Boxscape-Blog) of this project and log into your GitHub account. 
    - Click on the "Code" button, on the top right of the page, next to the green "Gitpod" button. 
    - Chose one of the available options: Clone with HTTPS, Open with Git Hub desktop, Download ZIP. 
    - To clone the repository using HTTPS, under "Clone with HTTPS", copy the link.
    - Open Git Bash. [How to download and install](https://phoenixnap.com/kb/how-to-install-git-windows).
    - Chose the location where you want the repository to be created. 
    - Type:
    ```
    $ https://github.com/cla-cif/The-Boxscape-Blog.git
    ```
    - Press Enter, the following lines will appear and your repository is now created.
    ```
    $ git clone https://github.com/cla-cif/The-Boxscape-Blog.git
    Cloning into 'The-Boxscape-Blog'...
    remote: Enumerating objects: 1429, done.
    remote: Counting objects: 100% (492/492), done.
    remote: Compressing objects: 100% (159/159), done. eceiving objects:   3% (43/1
    Rremote: Total 1429 (delta 358), reused 454 (delta 331), pack-reused 937
    objects:  96% (1372/1429)
    Receiving objects: 100% (1429/1429), 364.66 KiB | 1.05 MiB/s, done.
    Resolving deltas: 100% (1030/1030), done.
    ```
    - Click [Here](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository#cloning-a-repository-to-github-desktop) for a more detailed explaination. 

__You can find the live link to the site here: [TheBoxscape Blog](https://the-boxscape-blog.herokuapp.com/)__

## Credits 

### Code

-  All content written by developer Claudia Cifaldi - [cla-cif](https://github.com/cla-cif) on GitHub. 
-  The Blog was inspired to Code Institute's [Code Star Blog](https://github.com/Code-Institute-Solutions/Django3blog)
-  The template used for this project belongs to CodeInstitute - [GitHub](https://github.com/Code-Institute-Submissions) and [website](https://codeinstitute.net/global/).

### Content and Media
- The Code of Conduct is inspired to Facebook's
- The articles are from other blogs and webisites which are properly cited at the bottom of the article.

## Extra 

### Links to people we like. 

- [Dillinger](https://github.com/joemccann/dillinger) used to write this README.md file. 
- [GitHub supporting Ukraine](https://github.blog/2022-03-02-our-response-to-the-war-in-ukraine/).
- [GitHub repository by AndrewStetsenko](https://github.com/AndrewStetsenko/Support-Ukraine).

[Link to top](#top) 
