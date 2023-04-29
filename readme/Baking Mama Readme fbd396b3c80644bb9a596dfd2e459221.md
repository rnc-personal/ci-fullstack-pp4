# Baking Mama Readme

# Baking Mama

Baking Mama is a place for mums to share their own recipes online. Everyone enjoys “Mums Cooking” and many recipes online are either too complicated or are exotic dishes that get made once and forgotten about. Baking Mama aims to be a place to share recipes in a simple way with clear instructions and ingredients that is easy to navigate.

Site URL: [ci-pp4-baking.herokuapp.com](http://ci-pp4-baking.herokuapp.com/)

Preview:

![https://github.com/rnc-personal/ci-fullstack-pp4/blob/main/readme/desktop-baking-mama.png](http://ci-pp4-baking.herokuapp.com/)

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

The colour scheme for the site came from the logo. The client wanted a very cute, semi ”Anime” look to it, which was mostly achieve using images and characters throughout the site. Initially I looked at creating a logo that would fit this best and the sites colour scheme was derived from this, with some minor adjustment for contrast and readability.

The main palette is made up of 4 key colours:

![Untitled](Baking%20Mama%20Readme%20fbd396b3c80644bb9a596dfd2e459221/Untitled.png)

#DF7374 (’highlight-dark’)

#FDE0DE (’highlight-light’)

#FFFFFF(’site-bg’)

#343a40(’site-text’)

Some additional complimentary colors have been used for key bits of data about recipes like the user rating and difficulty scores.

### Typography

Throughout Development I was using a standard Bootstrap Font butfelt that it did not lend itself well to the look and feel of the site. Although functional, it was a bit too serious for the brief of the site. The font was replaced with Nunito from Google Fonts as this is rounded, more ‘friendly’ feeling font that is not too overly stylised or cartoonish;

Nunito:

![Untitled](Baking%20Mama%20Readme%20fbd396b3c80644bb9a596dfd2e459221/Untitled%201.png)

### Imagery

The imagery was a key part of making the site exciting and attractive to visitors. The sites design overall needed to be simple and easy to navigate with the imagery being the key feature about a recipe visually. The client wanted to go for very professional looking, blogger style photography shots with lots of depth of field that really focused on the food itself. 

All images for the site were generated using Midjourney.

### Wireframes

Before the Figma mockup I created a brief wirefame (below), This helped when looking around for Bootstrap templates to fit around the planned design.

![wireframes-pp4.png](Baking%20Mama%20Readme%20fbd396b3c80644bb9a596dfd2e459221/wireframes-pp4.png)

## Features

### Site General Features

Each page has as responsive navbar at the top, which also serve as the sites main search as well as footer that provides some quick links to navigate to the various categories / filters for the recipes.

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
    - Current Users can fill out an additional form with some personal info and they an be give permission to publish or submit articles for an admin to approve and publish
- Nested Comments
    - Use a plugin like Disqus or develop myself, a way for users to reply to each others comments on a recipe to get a better flow of conversation going

### Accessibility

I planned to use a bootstrap template / components for much of the layout so care was taken to find good assets that had accessibility options implemented well as this ensured nothing would be missed.

While initially the colour scheme for the site appeared to be okay for contrast and legibility , the testing towards the end of development revealed that some of the buttons with hover state changes were not really ideal. These were all changed out to be much higher contrast without impacting the look and feel of the site too much.

## Technologies Used

### Languages Used

The site was put developed using HTML/CSS/JS/Python

### Frameworks, Libraries & Programs Used

The site was built using the Django framework for Python, which is the most popular web application framework for the language. A few additional libraries were added to improve on it’s built-in functionality.

Most notably summernote for enhanced content editing, Crispy Forms for handling forms(comments/ratings) and cloudinay for image hosting/CDN.

## Deployment & Local Development

👩🏻‍💻 View an example of a completed Deployment & Local Development section [here](https://github.com/kera-cudmore/TheQuizArms#Deployment)

### Deployment

Include instructions here on how to deploy your project. For your first project you will most likely be using GitHub Pages.

### Local Development

The local development section gives instructions on how someone else could make a copy of your project to play with on their local machine. This section will get more complex in the later projects, and can be a great reference to yourself if you forget how to do this.

### How to Fork

Place instructions on how to fork your project here.

### How to Clone

Place instructions on how to clone your project here.

## Testing

Start as you mean to go on - and get used to writing a [TESTING.md](http://testing.md/) file from the very first project!

Testing requirements aren't massive for your first project, however if you start using a [TESTING.md](http://testing.md/) file from your first project you will thank yourself later when completing your later projects, which will contain much more information.

Use this part of the README to link to your [TESTING.md](http://testing.md/) file - you can view the example [TESTING.md](http://testing.md/) file [here](notion://www.notion.so/milestone1-testing.md)

## Credits

👩🏻‍💻 View an example of a completed Credits section [here](https://github.com/kera-cudmore/BookWorm#Credits)

The Credits section is where you can credit all the people and sources you used throughout your project.

### Code Used

If you have used some code in your project that you didn't write, this is the place to make note of it. Credit the author of the code and if possible a link to where you found the code. You could also add in a brief description of what the code does, or what you are using it for here.

### Content

Who wrote the content for the website? Was it yourself - or have you made the site for someone and they specified what the site was to say? This is the best place to put this information.

### Media

If you have used any media on your site (images, audio, video etc) you can credit them here. I like to link back to the source where I found the media, and include where on the site the image is used.

### Acknowledgments

If someone helped you out during your project, you can acknowledge them here! For example someone may have taken the time to help you on slack with a problem. Pop a little thank you here with a note of what they helped you with (I like to try and link back to their GitHub or Linked In account too). This is also a great place to thank your mentor and tutor support if you used them.