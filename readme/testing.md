# **CODE INSTITUTE: MILESTONE PROJECT 3**

# **larder**

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

| HTML Page | Warnings / Errors |
| --------- | ----------------- |

|

CSS Errors:

- CSS passed with no errors.

![CSS Validation](https://github.com/iainm342/milestone-4/blob/master/readme/images/testing/CSS-validated.png)

JShint Errors:

[Back to Contents](#contents)

PEP8 Errors:

![Python Validation](https://github.com/iainm342/milestone-4/blob/master/readme/images/testing/python-validate.png)

### <ins>ACCESIBILITY VALIDATION</ins>

The site was tested on the [WAVE](https://wave.webaim.org/) site.

![Webaim Validation](https://github.com/iainm342/milestone-4/blob/master/readme/images/testing/webaim.png)

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
- As a **user**, I want to be able to log on and off the site after I have registered.
  - The **user** can log on to the system by clicking the My Account icon in the top right of the screen and selecting Login. The **user** is prompted for their username and password. Form validation is present and once the **user** has inputed the information and clicked Sign In, they are redirected to the Home screen and are presented with a Bootstrap Toast confirming they have successfully logged in. **This requirement is deemed as being completed.**
    - Sign In Screen
      ![Log In](https://github.com/iainm342/milestone-4/blob/master/readme/images/testing/login.png)
  - The **user** can log out of the system by clicking the My Account icon in the top right of the screen and selecting Logout. The **user** is redirected to the Sign Out screen and is asked to confirm they wish to log out. On clicking the Sign Out button they are redirected to the Home screen and are presented with a Bootstrap Toast confirming they have successfully logged out. **This requirement is deemed as being completed.**
    - Sign Out Screen
      ![Log Out](https://github.com/iainm342/milestone-4/blob/master/readme/images/testing/logout.png)
- As a **user**, I want to be able to recover my password if I no longer remember it.
  - The **user** can recover their password, if forgotten, by clicking the `<a>Forgot Password?</a>` underneath the Sign In button. The **user** is asked to input their email address and on cllicking the Reset My Password button, and email will be sent to their email address if it is in the database. On following the link in the email the **user** will be allowed to reset their password and properly Sign In to the full site.
  - ![Recover Password](https://github.com/iainm342/milestone-4/blob/master/readme/images/testing/recover-password.png)
- As a **user**, I want to receive confirmation emails throughout the registration process.
  ![Registration Confirmation](https://github.com/iainm342/milestone-4/blob/master/readme/images/testing/reg-conf.png)
- As a **user**, I want to have a personal profile.
  ![Profile](https://github.com/iainm342/milestone-4/blob/master/readme/images/testing/profile.png)
- As a **user**, I want to be able to view all the products available for purchase.
  ![All Products](https://github.com/iainm342/milestone-4/blob/master/readme/images/testing/all-products.png)
- As a **user**, I want to be able to view products by Category.
  ![View by Category](https://github.com/iainm342/milestone-4/blob/master/readme/images/testing/view-category.png)
- As a **user**, I want to be able to see more detailed product information about products I am interested in.
  ![Product Detail](https://github.com/iainm342/milestone-4/blob/master/readme/images/testing/prod-detail.png)
- As a **user**, I want to be able to view the content, and associated cost, of my "bag" throughout my site use.
  ![Bag Toast](https://github.com/iainm342/milestone-4/blob/master/readme/images/testing/bag-toast.png)
- As a **user**, I want to be able to sort the products using pre-defined filters.
  ![Sorting](https://github.com/iainm342/milestone-4/blob/master/readme/images/testing/sorting.png)
- As a **user**, I want to be able to sort a specific Category of product.
  ![Category Search](https://github.com/iainm342/milestone-4/blob/master/readme/images/testing/cat-order-btn.png)
  ![Category Results](https://github.com/iainm342/milestone-4/blob/master/readme/images/testing/cat-order.png)
- As a **user**, I want to be able to add products to my basket easily.
  ![Add Product](https://github.com/iainm342/milestone-4/blob/master/readme/images/testing/add-item.png)
- As a **user**, I want to be able to view the items in my basket.
  ![View Basket Button](https://github.com/iainm342/milestone-4/blob/master/readme/images/testing/view-basket-1.png)
  ![View Basket](https://github.com/iainm342/milestone-4/blob/master/readme/images/testing/view-basket-2.png)
- As a **user**, I want to be able to adjust the quantity of items in my basket.
  ![Adjust Basket](https://github.com/iainm342/milestone-4/blob/master/readme/images/testing/basket-adjust.png)
- As a **user**, I want to be able to easily enter my payment details.
  ![Payment](https://github.com/iainm342/milestone-4/blob/master/readme/images/testing/payment.png)
- As a **user**, I want to be able to view an order confirmation after checkout.
  ![Order Confirmation](https://github.com/iainm342/milestone-4/blob/master/readme/images/testing/order-conf.png)
- As a **user**, I want to be able to see what events are happening within the region.
  ![Events](https://github.com/iainm342/milestone-4/blob/master/readme/images/testing/events-1.png)
  ![Events Detail](https://github.com/iainm342/milestone-4/blob/master/readme/images/testing/events-2.png)
- As a **site owner**, I want to be able to Add a product to the site.
  ![Add Product Dropdown](https://github.com/iainm342/milestone-4/blob/master/readme/images/testing/add-product-1.png)
  ![Add Product Screen](https://github.com/iainm342/milestone-4/blob/master/readme/images/testing/add-product-2.png)
- As a **site owner**, I want to be able to Edit a product to the site.
  ![Edit Product Pill](https://github.com/iainm342/milestone-4/blob/master/readme/images/testing/edit-product-1.png)
  ![Edit Product Screen](https://github.com/iainm342/milestone-4/blob/master/readme/images/testing/edit-product-2.png)
- As a **site owner**, I want to be able to Delete a product from the site.
  ![Delete Product Pill](https://github.com/iainm342/milestone-4/blob/master/readme/images/testing/delete-product-1.png)
  ![Delete Product Confirmation](https://github.com/iainm342/milestone-4/blob/master/readme/images/testing/delete-product-2.png)
- As a **site owner**, I want to be able to Add an event to the site.
  ![Add Event Button](https://github.com/iainm342/milestone-4/blob/master/readme/images/testing/add-event-1.png)
  ![Add Event Screen](https://github.com/iainm342/milestone-4/blob/master/readme/images/testing/add-event-2.png)
- As a **site owner**, I want to be able to Edit an event on the site.
  ![Edit Event Pill](https://github.com/iainm342/milestone-4/blob/master/readme/images/testing/edit-event-1.png)
  ![Edit Event Screen](https://github.com/iainm342/milestone-4/blob/master/readme/images/testing/edit-event-2.png)
- As a **site owner**, I want to be able to Delete an event from the site.
  ![Delete Event Pill](https://github.com/iainm342/milestone-4/blob/master/readme/images/testing/delete-event-1.png)
  ![Delete Event Confirmation](https://github.com/iainm342/milestone-4/blob/master/readme/images/testing/delete-event-2.png)

[Back to Contents](#contents)
