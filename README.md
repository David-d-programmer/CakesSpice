## CAKESSPICES
Welcome! to [CAKESSPICES](hhttps://cakesspice-d57190d7147c.herokuapp.com/), An cake ecommerce site where every kind of cake you desire can be gotten with affordable prices and also great tastes. Whether you're craving a special kind of cake, we can make it available to you. 
![ home page](/workspace/CakesSpice/media/pexels-moose-photos-170195-1036621 (1).jpg)
## Table of Contents
* All products
* Cheese Cake
* Carrot Cake
* Chocolate Cake
* Red Velvet Cake
* Butter Cake
## About Us
Welcome to CakeSSpice — where every bite feels like home.

We’re more than just cake makers — we’re flavor creators. At CakeSSpice, we specialize in crafting ready-made cakes infused with our signature blend of unique, heartwarming spices that bring comfort and joy to every celebration. Whether you're marking a milestone, sharing a sweet moment, or just treating yourself (because why not?), our cakes are made to make it special.

Our name says it all — Cake + Spice — a delicious combination that reflects our passion for baking with a twist. Inspired by the rich flavors of home baking and the warmth of tradition, each cake is made with care, quality ingredients, and a whole lot of love.

From birthdays to baby showers, casual get-togethers to grand celebrations, CakeSSpice is here to make your moments a little sweeter.

So go ahead, find your favorite — your next favorite memory is just a slice away.

## TESTING
Testing for the CakeSSpice ecommerce site was conducted using a combination of manual testing and automated testing with pytest to ensure the reliability, responsiveness, and overall performance of the application.

### Manual Testing
Manual testing was performed across all key components of the website, including:

* Product listing and detail pages

* Shopping bag (cart) functionality

* Checkout and order confirmation processes

* User authentication (login, register, logout)

* Navigation and page routing

* Manual checks focused on:

Functionality: Ensuring buttons, links, forms, and logic flows worked correctly

Responsiveness: Testing the site layout and interactions on various screen sizes (mobile, tablet, desktop)

Error Handling: Triggering errors and checking that appropriate messages were shown

Performance: Monitoring page load speeds and smooth transitions

The site was tested on different devices and browsers to validate consistent user experience across platforms.

### Automated Testing
Automated tests were written and run using pytest to validate core logic and backend functionality. These tests helped catch edge-case scenarios and ensured that views and models behaved as expected under various conditions.

### FRONT END VALIDATOR TESTING
 HTML - W3C VALIDATOR 

 CSS - Jigsaw VALIDATOR
### Prerequisites
All manner of testing was done and neceswary installation was done to keep this app running:
npm install and everything in the pip3 list

### Unfixed bug
I encountered a lot bugs when trying to deploy my project which the tutors help me so much to fix and i also made use of some materials to fix some. i encountered some challenges in the database area and i just followed every information about what needed to be done and i fixed it. The only thing left undone is navbar of the home page, i don't think it's responsive enough.

During testing, a few bugs were identified:

Issues with the remove and update functions in the Bag (cart) app. While attempts were made to resolve these, further debugging or assistance may be needed.

Minor UI inconsistencies on smaller screen sizes, which were addressed during the responsive testing phase.

## DEPLOYEMENT
This site was deployed by completing the following steps:

- Log in to Heroku or create an account
- On the main page click the button labelled New in the top right corner and from the drop-down menu select Create New App
- You must enter a unique app name
- Next select your region
- Click on the Create App button
- The next page is the project’s Deploy Tab. Click on the Settings Tab and scroll down to Config Vars
- Click Reveal Config Vars and enter disable collectstatic and give it a value one, also add the api key and the database url  and click the Add button
- Scroll down to the Buildpack section click Add Buildpack select python and click Save Changes
- Scroll to the top of the page and choose the Deploy tab
- Select Github as the deployment method
- Confirm you want to connect to GitHub
- Search for the repository name and click the connect button
- Scroll to the bottom of the deploy page and select the preferred deployment type
- Click either Enable Automatic Deploys for automatic deployment when you push updates to Github
you can see the live link [here](https://cakesspice-d57190d7147c.herokuapp.com/)

## CREDIT
### Contents
- Most images were gotten from Pixabay 
- The terminal function and template for the deployable application was provided by [Code Institute - Template](https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+EA101+7/courseware/eb05f06e62c64ac89823cc956fcd8191/2ad6f973a09b4b70a08943a73c9ac0ab/?child=last)

## Information Sources
- [Stackoverflow](https://stackoverflow.com/questions/44935514/heroku-uploading-a-static-site-on-heroku)
- [Django documentation](https://docs.djangoproject.com/en/5.1/)
- [Code Institute template]((https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+FSD101_WTS+4/courseware/713441aba05441dfb3a7cf04f3268b3f/824fccecd0fe4e44871eeabcbf69d830/)
)
## Menu

For a full products list, visit our [website](https://8000-daviddprogra-cakesspice-1odgbs0dfx0.ws-eu118.gitpod.io/products/) or place your order online.
![ products page](https://8000-daviddprogra-cakesspice-1odgbs0dfx0.ws-eu118.gitpod.io/products/)


## Ordering
Ordering at Cakesspices is easy! You can choose from the following methods:
1. Online: Visit our [website link] to browse the menu, place an order for delivery or takeout, and pay securely online.

## Payment Methods
* Credit/Debit Card

## Contact Information
We'd love to hear from you! For inquiries, orders, or any questions, you can reach us via:
* Phone: [Phone number]
* Email: [Email address]
* Address: [Restaurant Address]


## Social Media
Stay updated with our latest offers, events, and mouth-watering pictures by following us:
* Instagram: [Instagram handle]
* Facebook: [Facebook page]
* Twitter: [Twitter handle]
* TikTok: [TikTok handle]

### Summary
Overall, the site performs well across different environments and use cases. Testing helped ensure that the user experience is smooth, intuitive, and reliable, with only a few isolated areas (like cart updates/removal) needing further attention.

# Special thanks
Special thanks to my mentor Sandeep Aggarwal, my tutors at Code Institute, for their assistance throughout this project.