# Baking Mama Readme

# Baking Mama

Baking Mama is a place for mums to share their own recipes online. Everyone enjoys “Mums Cooking” and many recipes online are either too complicated or are exotic dishes that get made once and forgotten about. Baking Mama aims to be a place to share recipes in a simple way with clear instructions and ingredients that is easy to navigate.

Site URL: [ci-pp4-baking.herokuapp.com](http://ci-pp4-baking.herokuapp.com/)

Preview:

![http://ci-pp4-baking.herokuapp.com/](https://raw.githubusercontent.com/rnc-personal/CI-First-Project/main/readme/desktop-baking-mama.png)

---

## CONTENTS

- [User Experience](notion://www.notion.so/Baking-Mama-Readme-fbd396b3c80644bb9a596dfd2e459221#user-experience-ux)
    - [User Stories](notion://www.notion.so/Baking-Mama-Readme-fbd396b3c80644bb9a596dfd2e459221#user-stories)
- [Design](notion://www.notion.so/Baking-Mama-Readme-fbd396b3c80644bb9a596dfd2e459221#design)
    - [Colour Scheme](notion://www.notion.so/Baking-Mama-Readme-fbd396b3c80644bb9a596dfd2e459221#colour-scheme)
    - [Typography](notion://www.notion.so/Baking-Mama-Readme-fbd396b3c80644bb9a596dfd2e459221#typography)
    - [Imagery](notion://www.notion.so/Baking-Mama-Readme-fbd396b3c80644bb9a596dfd2e459221#imagery)
    - [Wireframes](notion://www.notion.so/Baking-Mama-Readme-fbd396b3c80644bb9a596dfd2e459221#wireframes)
- [Features](notion://www.notion.so/Baking-Mama-Readme-fbd396b3c80644bb9a596dfd2e459221#features)
    - [General Features on Each Page](notion://www.notion.so/Baking-Mama-Readme-fbd396b3c80644bb9a596dfd2e459221#general-features-on-each-page)
    - [Future Implementations](notion://www.notion.so/Baking-Mama-Readme-fbd396b3c80644bb9a596dfd2e459221#future-implementations)
    - [Accessibility](notion://www.notion.so/Baking-Mama-Readme-fbd396b3c80644bb9a596dfd2e459221#accessibility)
- [Technologies Used](notion://www.notion.so/Baking-Mama-Readme-fbd396b3c80644bb9a596dfd2e459221#technologies-used)
    - [Languages Used](notion://www.notion.so/Baking-Mama-Readme-fbd396b3c80644bb9a596dfd2e459221#languages-used)
    - [Frameworks, Libraries & Programs Used](notion://www.notion.so/Baking-Mama-Readme-fbd396b3c80644bb9a596dfd2e459221#frameworks-libraries--programs-used)
- [Deployment & Local Development](notion://www.notion.so/Baking-Mama-Readme-fbd396b3c80644bb9a596dfd2e459221#deployment--local-development)
    - [Deployment](notion://www.notion.so/Baking-Mama-Readme-fbd396b3c80644bb9a596dfd2e459221#deployment)
    - [Local Development](notion://www.notion.so/Baking-Mama-Readme-fbd396b3c80644bb9a596dfd2e459221#local-development)
        - [How to Fork](notion://www.notion.so/Baking-Mama-Readme-fbd396b3c80644bb9a596dfd2e459221#how-to-fork)
        - [How to Clone](notion://www.notion.so/Baking-Mama-Readme-fbd396b3c80644bb9a596dfd2e459221#how-to-clone)
- [Testing](notion://www.notion.so/Baking-Mama-Readme-fbd396b3c80644bb9a596dfd2e459221#testing)
- [Credits](notion://www.notion.so/Baking-Mama-Readme-fbd396b3c80644bb9a596dfd2e459221#credits)
    - [Code Used](notion://www.notion.so/Baking-Mama-Readme-fbd396b3c80644bb9a596dfd2e459221#code-used)
    - [Content](notion://www.notion.so/Baking-Mama-Readme-fbd396b3c80644bb9a596dfd2e459221#content)
    - [Media](notion://www.notion.so/Baking-Mama-Readme-fbd396b3c80644bb9a596dfd2e459221#media)
    - [Acknowledgments](notion://www.notion.so/Baking-Mama-Readme-fbd396b3c80644bb9a596dfd2e459221#acknowledgments)

---

## User Experience (UX)

### Initial Discussion

Baking Mama is a group of mums that often shared recipes with each other, often by email and Facebook Messenger, who wanted a way to share those recipes with others and their small group in an easier way.

### Key information for the site

- List of Recipes
- Being able to filter Recipes by various requirements/options
- Be able to leave feedback and suggestions on each recipe

## User Stories

### Client Goals

- To be able to view the site on a range of device sizes.
- Easily Search for a recipe by name or ingredients
- Filter Recipes by relevant information (e.g, Cooking Time, Difficulty)

### User Goals

- Easily find some of the best / newest recipes
- Navigate the site easily to find information either through the navigation or a search.
- To signup and offer feedback and ratings on recipes that I try out.

## Design

The basic design can be viewed in Figma here: [https://www.figma.com/file/wMtqtStV6pOwUY887wxd4V/PP4-UI?node-id=0%3A1&t=ZruK5vsb6ZiQAh1y-1](https://www.figma.com/file/wMtqtStV6pOwUY887wxd4V/PP4-UI?node-id=0%3A1&t=ZruK5vsb6ZiQAh1y-1)

### Colour Scheme

The colour scheme for the site came from the logo. The client wanted a very cute, semi ”Anime” look to it, which was mostly achieve using images and characters throughout the site. Initially, I looked at creating a logo that would fit this best and the sites colour scheme was derived from this, with some minor adjustment for contrast and readability.

The main palette is made up of 4 key colours:

![Palette](https://raw.githubusercontent.com/rnc-personal/CI-First-Project/main/readme/Untitled.png)

#DF7374 (’highlight-dark’)

#FDE0DE (’highlight-light’)

#FFFFFF(’site-bg’)

#343a40(’site-text’)

Some additional complimentary colors have been used for key bits of data about recipes like the user rating and difficulty scores.

### Typography

Throughout Development I was using a standard Bootstrap Font but felt that it did not lend itself well to the look and feel of the site. Although functional, it was a bit too serious for the brief of the site. The font was replaced with Nunito from Google Fonts as this is rounded, more ‘friendly’ feeling font that is not too overly stylised or cartoonish;

Nunito:

![Font](https://raw.githubusercontent.com/rnc-personal/CI-First-Project/main/readme/Untitled%201.png)

### Imagery

The imagery was a key part of making the site exciting and attractive to visitors. The sites design overall needed to be simple and easy to navigate with the imagery being the key feature about a recipe visually. The client wanted to go for very professional looking, "blogger" style photography shots with lots of depth of field that really focused on the food itself. 

All images for the site were generated using Midjourney.

### Wireframes

Before the Figma mockup I created a brief wirefame (below), This helped when looking around for Bootstrap templates to fit around the planned design.

![wireframes-pp4.png](https://raw.githubusercontent.com/rnc-personal/CI-First-Project/main/readme/wireframes-pp4.png)

## Features

### Site General Features

Each page has a responsive navbar at the top, which also serve as the sites main search as well as footer that provides some quick links to navigate to the various categories/filters for the recipes.

- Home
    - Responsive Hero Slider: Links to selected recipes and shows of some of the photography. Can be edited via the admin panel.
- Card Section
    - Lists out the 4 newest recipes on the site and the 8 highest rated recipes below that.
- Call To Action
    - A place for some additional text content about the site to live. Can be edited in the admin.
- Promo/About;
    - Small Area for an image and some text
- Recipe listings
    - Recipes list features several filters to navigate through the recipes
        - Category
        - Rating
        - Cooking Time
        - Difficulty
- Recipe
    - Image
    - Instructions
    - Ingredients
    - Time to Cook
    - Difficulty Rating
    - Average Score from Users
    - Leave a comment+rating (If logged in)
    - Baking Mama tips (based on difficulty rating)

### Future Implementations

Some features I would like to implement are:

- Apply to Be an Author
    - Current Users can fill out an additional form with some personal info and they can be give permission to publish or submit articles for an admin to approve and publish
- Nested Comments
    - Use a plugin like Disqus or develop myself, a way for users to reply to each others comments on a recipe to get a better flow of conversation going

### Accessibility

I planned to use a bootstrap template/components for much of the layout so care was taken to find good assets that had accessibility options implemented well as this ensured nothing would be missed.

While initially, the colour scheme for the site appeared to be okay for contrast and legibility, the testing towards the end of development revealed that some of the buttons with hover state changes were not really ideal. These were all changed out to be much higher contrast without impacting the look and feel of the site too much.

## Technologies Used

### Languages Used

The site was put developed using HTML/CSS/JS/Python

### Frameworks, Libraries & Programs Used

The site was built using the Django framework for Python, which is the most popular web application framework for the language. A few additional libraries were added to improve on its built-in functionality.

Most notably Summernote for enhanced content editing, Crispy Forms for handling forms(comments/ratings) and Cloudinary for image hosting/CDN.

## Deployment & Local Development

### Deployment

By following the steps below, part of the deployment process will be taken care of for you.
For a full deployment:

- Change the DEBUG setting in your main project folders settings.py file to "False" (no quotes)
- Remove the DISABLE_COLLECTSTATIC variable inside of Heroku
- Connect to Github in the deploy tab of the project
- Go to the deploy tab of the project, at the bottom the 'Manual Deploy' option will deploy the project from the branch that is currently selected
- Optionally you can enable automatic deploys each time a new commit is made. This isn't recommended while development is ongoing necessarily as it is quicker to view changes locally and many times it will require changing the debug setting each time you want to view the 'live' site hosted on Heroku.

### Local Development

Once the project is forked or checked out, you will need to check in baking_mama/settings.py and set the DEBUG variable to 'False' (without quotes).
You will also need to setup a Heroku, Cloudinary, and ElephantSQL account:

You will need to replace 2 keys within the settings.py and env.py files for your own deployment.

### Elephant SQL(elephantsql.com):

- Create an Account
- Click “Create New Instance”
- Set up your plan;
- Give your plan a Name (this is commonly the name of the project)
    - Select the Tiny Turtle (Free) plan
    - You can leave the Tags field blank
- Click “Select Region”
    - Select a data center near you
    - If you receive a message saying "Error: No cluster available in your-chosen-data-center yet", choose another region
- Click Review and check the details
- Return to the ElephantSQL dashboard and click on the database instance name for this project
- Copy your ElephantSQL database URL using the Copy icon. It will start with postgres://

### Cloudinary(cloudinary.com):

- Copy your CLOUDINARY_URL e.g. API Environment Variable.
- Add Cloudinary URL to env.py (should look like os.environ["CLOUDINARY_URL"] = "cloudinary://************************" )

### Heroku(heroku.com):

- Create an Account
- Top Right, Create new Heroku App
    - APP_NAME, Location = Europe
    - Open the settings tab
    - Click Reveal Config Vars
    - Add a Config Var called DATABASE_URL
    - Note: This is the ElephantSQL database url you copied in the previous step
- Back in the editor, edit the env.py file and change the below line so it has your unique key in:
    - os.environ["DATABASE_URL"] = "Paste in ElephantSQL database URL"
- Replace the secret key value with some value (doesn't matter what it is but it should not be easily guessed or shared).

The settings.py file has been configured to use the SECRET_KEY and DATABASE_URL variables automatically and will update the project with the value you enter for your own project. 

Back in Heroku/settings/reveal config vars, add the cloudinary key (CLOUDINARY_URL, cloudinary://************************)

Finally, add DISABLE_COLLECTSTATIC to Heroku Config Vars and set the value to 1. This is temporary for development and will need to be removed prior to launching the project yourself. Having it set to 1 means that Django is serving the assets locally, when it is disabled, Cloudinary will serve them for you.

The directories and config has already been done for you, you just need to replace the keys with your own.

The final step is updating your settings.py file in the main project directory.
The line that reads: ALLOWED_HOSTS = ["ci-pp4-baking.herokuapp.com", "localhost"] needs to be updated to match the name of your Heroku project you just created. It always ends with "...herokuapp.com", the localhost must remain there.


## Testing
| Task                                            | Description                                                                                           | Status |
| ----------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ------ |
| Check all Links and Buttons                     | Manually test all links and buttons, for broken links. Do broken links take you to a proper 404 page? | PASS   |
| Spell Check                                     | Check in content and templates for any typos and correct them                                         | PASS   |
| Check for any empty content (including Ratings) | Check for blank content                                                                               | PASS   |
| Create Dummy Content (Comments + Ratings)       | As a logged in user, create some comments and ratings for each recipe                                 | PASS   |
| Check Pagination                                | Does any pagination behave as you expect?                                                             | PASS   |
| HTML Validation                                 | Use External HTML Validator to check for layout errors                                                | PASS   |
| CSS Validation                                  | Use External CSS Validator to check for layout errors/bad practices                                   | PASS   |
| Python Validation                               | Use External python validator/linter to check for layout errors/bad practices                         | PASS   |
| Browser Testing                                 | Check across various browsers and operating systems for incompatiblities (if available)               | PASS   |
| Lighthouse Testing                              | Take a lighthouse score for desktop and mobile                                                        | PASS   |
| Responsive Testing                              | Test on a mobile device for any layout issues                                                         | PASS   |
| 404 page                                        | Check that the 404 page only displays for incorrect links and not links that should be working        | PASS   |
| Login and Signup                                | Check new users can signupand then login                                                              | PASS   |


### Code Used
- Boostrap template: "Start bootstrap" (https://startbootstrap.com/previews/blog-post)
- No direct code has been used from an external source, though a combination of Stack overflow, dajngo documentation and blog posts have been looked up for reference purposes only

### Content
All content was written by ChatGPT4 aside from Home Page CTA(Calls to Action)


### Media
All Images generated by Midjourney V5




