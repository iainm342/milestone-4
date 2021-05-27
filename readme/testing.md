# **CODE INSTITUTE: MILESTONE PROJECT 4**

# **DELI SW**

# Testing

[back to README.md file](https://github.com/iainm342/milestone-4/blob/master/README.md/#testing)

---

## **CONTENTS**

- [Manual Testing](#manual-testing)
- [Automated Testing](#automated-testing)
  - [Code Validation](#code-validation)
  - [Accesibility Validation](#accesibility-validation)
  - [Browser Validation](#browser-validation)
- [User Testing](#user-testing)
  - [Peer Testing](#peer-testing)
  - [User Testing](#user-testing)

---

## **MANUAL TESTING**

- Chrome Developer Tools were used to test responsiveness on all screen sizes.
- Physical testing was carried out on Desktop, Tablet and various Mobile devices.
  - Throughout the whole process, I was testing the responsiveness of the site with my laptop, iPhone X and iPad.
  - Once the site was in a state that I was happy with, I submitted it for Peer review.
  - I also asked friends and family to have a look at the site from a user perspective, rather than a coders perspective.
- All links were tested to ensure they worked on all devices.
- NavBar was tested to ensure it worked on all devices.
- All CRUD functions were tested to ensure they worked on all devices.

[Back to Contents](#contents)

---

## **AUTOMATED TESTING**

### <ins>CODE VALIDATION</ins>

All HTML and CSS was passed through [W3C Validator](https://validator.w3.org/), [W3C Validator CSS](https://jigsaw.w3.org/css-validator/), JavaScript and jQuery through [JShint](https://jshint.com/) and Python through [PEP8 Online](http://pep8online.com/).

HTML Errors:

All pages passed through the Validator with the following results:

| HTML Page                   | Warnings / Errors                  |
| --------------------------- | ---------------------------------- |
| /home/                      | None                               |
| /accounts/login/            | None                               |
| /accounts/logout/           | None                               |
| /accounts/signup/           | None                               |
| /products/1/                | None                               |
| /products/add/              | None                               |
| /products/edit/1            | None                               |
| /reviews/add_review/1       | None                               |
| /reviews/edit/review/1      | None                               |
| /profile/                   | None                               |
| /profile/order_history/     | None                               |
| /events/                    | None                               |
| /events/add_event/          | None                               |
| /events/edit_event/         | None                               |
| /events/detail/             | None                               |
| /bag/                       | None                               |
| /checkout/                  | Empty heading - processing overlay |
| /checkout.checkout_success/ | None                               |

CSS Errors:

- CSS passed with no errors.

![CSS Validation](https://github.com/iainm342/milestone-4/blob/master/readme/images/testing/CSS-validated.png)

JShint Errors:

- all JS and jQuery has been passed through the Validator, however, various warnings were presented with regards to the $ in jQuery. Searching has shown that some extra code should be added to the .jshintrc to remove these warnings - this is outwith my current knowledge and skill base and will need some further research on my part.

[Back to Contents](#contents)

PEP8 Errors:

All .py files passed through the Validator with the following errors which have been resolved where possible

| Python File                    | Warnings / Errors                             | Pass |
| ------------------------------ | --------------------------------------------- | ---- |
| bag > contexts.py              |                                               | Pass |
| bag > urls.py                  |                                               | Pass |
| bag > views.py                 | Lines 1, 26 and 45 too long                   | Pass |
| -----------------              | ---------------------------                   | ---- |
| checkout > admin.py            |                                               | Pass |
| checkout > apps.py             |                                               | Pass |
| checkout > forms.py            |                                               | Pass |
| checkout > models.py           | Lines 15 and 48 too long                      | Pass |
| Checkout > signals.py          |                                               | Pass |
| Checkout > urls.py             |                                               | Pass |
| Checkout > views.py            | Lines 1, 72, 84, 92, 102 too long             | Fail |
|                                | Line 74 too long and unsure how to resolve it |      |
| Checkout > webhook_handlers.py | Lines 73, 74, 104 and 104 too long            | Fail |
|                                | Unsure how to resolve                         |      |
| Checkout > webhooks.py         | Line 43 too long                              | Fail |
|                                | Unsure how to resolve                         |      |
| -----------------              | ---------------------------                   | ---- |
| Contact > forms.py             |                                               | Pass |
| Contact > urls.py              |                                               | Pass |
| Contact > views.py             |                                               | Pass |
| -----------------              | ---------------------------                   | ---- |
| Events > admin.py              |                                               | Pass |
| Events > forms.py              |                                               | Pass |
| Events > models.py             |                                               | Pass |
| Events > urls.py               |                                               | Pass |
| Events > views.py              |                                               | Pass |
| -----------------              | ---------------------------                   | ---- |
| Home > urls. py                |                                               | Pass |
| Home > views.py                |                                               | Pass |
| -----------------              | ---------------------------                   | ---- |
| Products > admin.py            |                                               | Pass |
| Products > forms.py            |                                               | Pass |
| Products > models.py           |                                               | Pass |
| Products > urls.py             |                                               | Pass |
| Products > views.py            | Lines 57, 103, 132 too long                   | Pass |
| -----------------              | ---------------------------                   | ---- |
| Profiles > forms.py            |                                               | Pass |
| Profiles > models.py           | Lines 16, 17, 18, 19 and 21 too long          | Pass |
| Profiles > urls.py             |                                               | Pass |
| Profiles > views.py            | Line 22 too long                              | Pass |
| -----------------              | ---------------------------                   | ---- |
| Reviews > admin.py             |                                               | Pass |
| Reviews > forms.py             |                                               | Pass |
| Reviews > models.py            |                                               | Pass |
| Reviews > urls.py              |                                               | Pass |
| Reviews > views.py             |                                               | Pass |

[Back to Contents](#contents)

### <ins>ACCESIBILITY VALIDATION</ins>

The site was tested on the [WAVE](https://wave.webaim.org/) site. Passed with minimal contrast errors - both main colours tested against white background.

- #2b4612
  ![Webaim Validation](https://github.com/iainm342/milestone-4/blob/master/readme/images/testing/webaim-2b4612.png)
- #721817
  ![Webaim Validation](https://github.com/iainm342/milestone-4/blob/master/readme/images/testing/webaim-721817.png)

[Back to Contents](#contents)

### <ins>BROWSER VALIDATION</ins>

The site was tested on the following browsers that I have access to:

- Google Chrome

![Chrome](https://github.com/iainm342/milestone-4/blob/master/readme/images/testing/chrome.png)

- Mozilla Firefox

![Firefox](https://github.com/iainm342/milestone-4/blob/master/readme/images/testing/firefox.png)

- Microsoft Edge

![Edge](https://github.com/iainm342/milestone-4/blob/master/readme/images/testing/edge.png)

[Back to Contents](#contents)

---

## **USER TESTING**

### <ins>PEER TESTING</ins>

I submitted the project for Peer Review on Slack. The following comments were made:

[Back to Contents](#contents)

### <ins>USER TESTING</ins>

I asked various friends and family to test the site as **users** and not as coders to gain a different perspective. This happened towards the end of the project to ensure that the User Stories had been met. The following feedback was given from the group:

- As a **user**, I want to be able to register as a new user on the site.
  - The **user** click the My Account dropdown icon in the top right of the screen and selects Register from the dropdown list. They are then able to complete the form that is displayed which has 5 fields that need to be completed. Form validation is present with the **user** being unable to sign up unless the form is completed correctly. On pressing the Sign Up button, the **user** is presneted with a Verify Your E-Mail Address screen. The **user** must then check their email and confirm their request to register before they are able to fully access the site. **This requirement is deemed as being completed.**
    ![Register](https://github.com/iainm342/milestone-4/blob/master/readme/images/testing/register.png)

[Back to Contents](#contents)

- As a **user**, I want to be able to log on and off the site after I have registered.
  - The **user** can log on to the system by clicking the My Account icon in the top right of the screen and selecting Login. The **user** is prompted for their username and password. Form validation is present and once the **user** has inputed the information and clicked Sign In, they are redirected to the Home screen and are presented with a Bootstrap Toast confirming they have successfully logged in. **This requirement is deemed as being completed.**
    - Sign In Screen
      ![Log In](https://github.com/iainm342/milestone-4/blob/master/readme/images/testing/login.png)
  - The **user** can log out of the system by clicking the My Account icon in the top right of the screen and selecting Logout. The **user** is redirected to the Sign Out screen and is asked to confirm they wish to log out. On clicking the Sign Out button they are redirected to the Home screen and are presented with a Bootstrap Toast confirming they have successfully logged out. **This requirement is deemed as being completed.**
    - Sign Out Screen
      ![Log Out](https://github.com/iainm342/milestone-4/blob/master/readme/images/testing/logout.png)

[Back to Contents](#contents)

- As a **user**, I want to be able to recover my password if I no longer remember it.
  - The **user** can recover their password, if forgotten, by clicking the `<a>Forgot Password?</a>` underneath the Sign In button. The **user** is asked to input their email address and on cllicking the Reset My Password button, and email will be sent to their email address if it is in the database. On following the link in the email the **user** will be allowed to reset their password and properly Sign In to the full site. **This requirement is deemed as being completed.**
  - ![Recover Password](https://github.com/iainm342/milestone-4/blob/master/readme/images/testing/recover-password.png)

[Back to Contents](#contents)

- As a **user**, I want to receive confirmation emails throughout the registration process.
  - The **user**, once they have completed the full registration form, will be prompted to check their email inbox for the email verification message. This message, as previously explained, contains a link to confirm their registration on the site. **This requirement is deemed as being completed.**
    ![Registration Confirmation](https://github.com/iainm342/milestone-4/blob/master/readme/images/testing/reg-conf.png)

[Back to Contents](#contents)

- As a **user**, I want to have a personal profile.
  - The **user**, once registered and signed in to the site, is able to view their profile by clicking the My Account button in the top right of the screen and selecting My Profile. The My Profile screen is divided in to two sections - Default Delivery Information and Order History. The **user** can update their delivery information and click the Update Info button. This information is then automatically filled in on the Billing Screen for a better User Experience. Once orders are added to the site, they are saved in the database and are visible to the **user**. The **user** can hover over their mouse over the order number and the full order number will be displayed. Clicking the order number brings the **user** to the order summary screen and a Bootstrap Toast lets them know this is a past order that they are viewing. **This requirement is deemed as being completed.**
    - Profile Page
      ![Profile No Order](https://github.com/iainm342/milestone-4/blob/master/readme/images/testing/profile-1.png)
    - Profile Page with Completed Orders
      ![Profile With Orders](https://github.com/iainm342/milestone-4/blob/master/readme/images/testing/profile-2.png)

[Back to Contents](#contents)

- As a **user**, I want to be able to view all the products available for purchase.
  - The **user** can access the All Products screen by clicking the Shop Now button on the Home page or by selecting All Products from the All Products Dropdown on the central navbar. The **user** is then presented with a card layout showing all the products on the site. Each card contains the product image, name, county, price, category, rating and, dependant on their user rights, the edit and delete buttons. **This requirement is deemed as being completed.**
    ![All Products](https://github.com/iainm342/milestone-4/blob/master/readme/images/testing/all-products.png)

[Back to Contents](#contents)

- As a **user**, I want to be able to view products by Category/Price/Rating.
  - The **user** is able to sort the All Products screen by either selecting the appropriate dropdown action in the All Products menu or using the filter box in the top right of the main body. The filter box allows the user to view the products in alphabetical/numerical order dependant on which category they have selected and also to reverse the order of their chosen sort method. **This requirement is deemed as being completed.**
    ![View by Category](https://github.com/iainm342/milestone-4/blob/master/readme/images/testing/view-category.png)

[Back to Contents](#contents)

- As a **user**, I want to be able to see more detailed product information about products I am interested in.
  - The **user** on clicking a product image on the All Product screen is taken to the relevant product-detil.html page. The product detail page contains the product information along with a more detailed description of the product. The **user** is able to add products to their basket through using the plus/minus buttons, direct entry to the input field or using the arrows within the input field. The **user** is also able to continue shopping from this screen by clicking the Keep Shopping button.
    ![Product Detail](https://github.com/iainm342/milestone-4/blob/master/readme/images/testing/prod-detail.png)

[Back to Contents](#contents)

- As a **user**, I want to be able to view the content, and associated cost, of my "bag" throughout my site use.
  - The **user**, once items have been added to their bag, will be shown a Bootstrap Success message confirming the item(s) addition to the bag. Continued addition of items will increase the information contained in the Toast and the **user** will be able to scroll through their bag without having to leave the product screens. The **user** is also able to click the Go to Secure Checkout button to take them immediately to the full Shopping Bag page.
    ![Bag Toast](https://github.com/iainm342/milestone-4/blob/master/readme/images/testing/bag-toast.png)

[Back to Contents](#contents)

- As a **user**, I want to be able to see all products from a specific County.
  - The **user** is able to filter all the products by County by clicking the County name on the All Product page or on the Product Detail page. The County name is an <a> tag that contains the url information for the product page.
    - County <a> Tag
      ![County Order Button](https://github.com/iainm342/milestone-4/blob/master/readme/images/testing/county-order-btn.png)
    - Filtered Product Results
      ![County Order](https://github.com/iainm342/milestone-4/blob/master/readme/images/testing/county-order.png)

[Back to Contents](#contents)

- As a **user**, I want to be able to add products to my basket easily.
  - The **user** is able to add items to their bag by clicking the plus and minus buttons held within the Product Detail page. There are two <a> tags to allow the **user** to quickly update the quantity within the bag or to rmeove the product line from the bag if desired. The location below the quantity input field allows for minimal disruption to the **user** flow.
    ![Add Product](https://github.com/iainm342/milestone-4/blob/master/readme/images/testing/add-item.png)

[Back to Contents](#contents)

- As a **user**, I want to be able to view the items in my basket.
  - The **user** clicks the basket icon in the top right of the page and is taken to the Shopping Bag summary page. The **user** can alter the quantity of a specific product by clicking the plus/minus icons on either side of the input field, manually change the quantity within the field with keyboard input or by using the up/down arrow that appear in the field when hovering.Navigation buttons are visible to alow the **user** to either continue shopping or to move to the Checkout page.
    - Navbar icon
      ![View Basket Button](https://github.com/iainm342/milestone-4/blob/master/readme/images/testing/view-basket-1.png)
    - Shopping basket
      ![View Basket](https://github.com/iainm342/milestone-4/blob/master/readme/images/testing/view-basket-2.png)

[Back to Contents](#contents)

- As a **user**, I want to be able to adjust the quantity of items in my basket.
  - Within all variations of the Shopping Basket page, the **user** can alter the quantity of a product being ordered by clciking th eplus/minus icons on either side of the quantity input field. This alters the quantity ordered value and must be confirmed by clicking the Update <a> tag for it to be confirmed.
    ![Adjust Basket](https://github.com/iainm342/milestone-4/blob/master/readme/images/testing/basket-adjust.png)

[Back to Contents](#contents)

- As a **user**, I want to be able to easily enter my payment details.
  - When the **user** reaches the Checout page they are presented with a two column container that has delivery details on the left and another order summary on the right. The delivery details will be pre-populate if the **user** has logged in with active account. If the **user** is not logged in, the order will still be processed but will be done as an Anonymous user. The **user** can log in by clicking the link at the bottom of the screen which will take them to the log in screen and then back to the Shopping Basket. Credit card details are entered in to the bottom field and the field is validated using Stripe. Clicking Complete Order will display an "processing" overlay and then take the **user** to the Checkout Success page. The **user** is able to return to the Shopping Bag page if they wish to amend the order before payment processing.
    ![Payment](https://github.com/iainm342/milestone-4/blob/master/readme/images/testing/payment.png)

[Back to Contents](#contents)

- As a **user**, I want to be able to view an order confirmation after checkout.
- Once the **user** has clicked the Complete Order button, they are directed to the Checkout Success page which shows a confirmation of their order along with their unique Order Number at the top of the page. The **user** is able to click a button that will take them to the Events page to try and keep them on the site for a longer period of time.
  ![Order Confirmation](https://github.com/iainm342/milestone-4/blob/master/readme/images/testing/order-conf.png)

[Back to Contents](#contents)

- As a **user**, I want to be able to Add a review for a specific product.
  - From an indiviudal items Product Detail page, the **user** is able to add a review for that product. By cllcking the Add a Review button at the bottom of the Product Detail page, the **user** is redirected to the Add a Review page. This page contains a simple form that will allow them to enter a title, description and rating value. The **user** can cancel this process by clicking the Cancel button or submit the review. The review is then displayed at the bottom of the Product Detail page.
    - Add Review Button
      ![Add Review Button](https://github.com/iainm342/milestone-4/blob/master/readme/images/testing/add-review-1.png)
    - Add Review Form
      ![Add Review Screen](https://github.com/iainm342/milestone-4/blob/master/readme/images/testing/add-review-2.png)

[Back to Contents](#contents)

- As a **user**, I want to be able to Edit a review for a product that I have added.
  - If the **user** is logged in and has added the review in question, or a SuperUser, they will see the Edit/Delete pills underneath the review when it is displayed on the Product Detail Page. By clicking the Edit Pill, the **user** is redirected to the Edit Review form. This form is pre-populated with the review informtion which the **user** can then alter and submit the changes to the DB.
    - Edit Review Pill
      ![Edit Review Pill](https://github.com/iainm342/milestone-4/blob/master/readme/images/testing/edit-review-1.png)
    - Edit Review Form
      ![Edit Review Screen](https://github.com/iainm342/milestone-4/blob/master/readme/images/testing/edit-review-2.png)

[Back to Contents](#contents)

- As a **user**, I want to be able to Delete a review for a product that I have added.
  ![Delete Review Pill](https://github.com/iainm342/milestone-4/blob/master/readme/images/testing/delete-review-1.png)
  ![Delete Review Confirmation](https://github.com/iainm342/milestone-4/blob/master/readme/images/testing/delete-review-2.png)

[Back to Contents](#contents)

- As a **user**, I want to be able to see what events are happening within the region.
  ![Events](https://github.com/iainm342/milestone-4/blob/master/readme/images/testing/events-1.png)
  ![Events Detail](https://github.com/iainm342/milestone-4/blob/master/readme/images/testing/events-2.png)

[Back to Contents](#contents)

- As a **user**, I want to be able to search the site for products using key words.
  ![Search](https://github.com/iainm342/milestone-4/blob/master/readme/images/testing/key-item-search.png)
  ![Search Results](https://github.com/iainm342/milestone-4/blob/master/readme/images/testing/search-results.png)

[Back to Contents](#contents)

- As a **user**, I want the site navigation to be inuitive and easy to use.

[Back to Contents](#contents)

- AS a **user**, I want the information to be displayed in a clear and organised manner to allow for quick decisions to be made.

[Back to Contents](#contents)

- As a **site owner**, I want to be able to Add a product to the site.
  ![Add Product Dropdown](https://github.com/iainm342/milestone-4/blob/master/readme/images/testing/add-product-1.png)
  ![Add Product Screen](https://github.com/iainm342/milestone-4/blob/master/readme/images/testing/add-product-2.png)

[Back to Contents](#contents)

- As a **site owner**, I want to be able to Edit a product to the site.
  ![Edit Product Pill](https://github.com/iainm342/milestone-4/blob/master/readme/images/testing/edit-product-1.png)
  ![Edit Product Screen](https://github.com/iainm342/milestone-4/blob/master/readme/images/testing/edit-product-2.png)

[Back to Contents](#contents)

- As a **site owner**, I want to be able to Delete a product from the site.
  ![Delete Product Pill](https://github.com/iainm342/milestone-4/blob/master/readme/images/testing/delete-product-1.png)
  ![Delete Product Confirmation](https://github.com/iainm342/milestone-4/blob/master/readme/images/testing/delete-product-2.png)

[Back to Contents](#contents)

- As a **site owner**, I want to be able to Add an event to the site.
  ![Add Event Button](https://github.com/iainm342/milestone-4/blob/master/readme/images/testing/add-event-1.png)
  ![Add Event Screen](https://github.com/iainm342/milestone-4/blob/master/readme/images/testing/add-event-2.png)

[Back to Contents](#contents)

- As a **site owner**, I want to be able to Edit an event on the site.
  ![Edit Event Pill](https://github.com/iainm342/milestone-4/blob/master/readme/images/testing/edit-event-1.png)
  ![Edit Event Screen](https://github.com/iainm342/milestone-4/blob/master/readme/images/testing/edit-event-2.png)

[Back to Contents](#contents)

- As a **site owner**, I want to be able to Delete an event from the site.
  ![Delete Event Pill](https://github.com/iainm342/milestone-4/blob/master/readme/images/testing/delete-event-1.png)
  ![Delete Event Confirmation](https://github.com/iainm342/milestone-4/blob/master/readme/images/testing/delete-event-2.png)

[Back to Contents](#contents)
