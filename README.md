# VenueDjango
![Ariel Logo](/media/logoariel.webp)
allauth app itself log in and out

kaggle.com

###  "GET /favicon.ico HTTP/1.1" 404 2109

## Wireframe
![Ariel Logo](/media/products/wireframe_search.webp)
#### Front Website
![Ariel Logo](/media/products/wireframefrontpagewebsite.webp)
#### Front Website air ipad
![Ariel Logo](/media/products/wireframeipad_frontpage.webp)
#### Front Website iphone 14 pro max
![Ariel Logo](/media/products/wireframeiphonefrontpage.webp)




## Customer Table

| Field            | Description            |
|------------------|------------------------|
| Tenant ID        | Unique identifier for the Customer  |
| First Name       | Tenant's first name     |
| Last Name        | Tenant's last name      |
| Date of Birth    | Tenant's date of birth  |
| Email Address    | Tenant's email address  |
| Contact Details  | Tenant's contact details |
| Billing Address  | Tenant's billing address |

## Venue Table

| Field            | Description            |
|------------------|------------------------|
| Product ID       | Unique identifier for the product |
| Price            | Price of the product    |
| Rating           | Rating of the product   |
| Category         | Category of the product |
| Description      | Description of the product |
| Image URL        | URL of the product image |
| Has Sizes        | Indicates if the product has sizes |
| Capacity         | Capacity of the product (e.g., people) |
| Square Feet      | Square footage of the product |
| Has Free Wi-Fi   | Indicates if free Wi-Fi is available |
| Has Catering     | Indicates if catering is available |
| Is Accessible    | Indicates if the product is accessible |

## Events Table

| Field            | Description            |
|------------------|------------------------|
| Event ID         | Unique identifier for the event |
| Product ID       | ID of the associated product |
| Weddings         | Availability for weddings |
| Birthdays        | Availability for birthdays |
| Parties          | Availability for parties   |
| Baby Shower      | Availability for baby showers |
| Corporate Events | Availability for corporate events |
| Christmas        | Availability for Christmas events |
| Lifestyle & Photoshoots | Availability for lifestyle and photoshoots |
| Event Type       | Type of venue (e.g., hall, apartment) |

## Features Table

| Field            | Description            |
|------------------|------------------------|
| Feature ID       | Unique identifier for the feature |
| Product ID       | ID of the associated product |
| Outdoor Space    | Availability of outdoor space |
| Music            | Availability of music      |
| City             | Availability of a city view |
| Big Screen       | Availability of a big screen |
| Exclusive Hire   | Availability for exclusive hire |
| Disabled Access  | Availability of disabled access |
| Air Conditioning | Availability of air conditioning |

## Special Offer Table

| Field            | Description            |
|------------------|------------------------|
| Offer ID         | Unique identifier for the special offer |
| Product ID       | ID of the associated product |
| Family Packages  | Availability for family packages |
| Summer Party     | Availability for summer parties |
| Club             | Availability for club events |
| All Special Offers | Availability for all special offers |
| Baby Shower      | Availability for baby showers |
| Corporate Events | Availability for corporate events |
| Christmas        | Availability for Christmas events |
| Lifestyle & Photoshoots | Availability for lifestyle and photoshoots |

## Payments Table

| Field              | Description            |
|--------------------|------------------------|
| Payment ID         | Unique identifier for the payment |
| Tenant ID          | ID of the associated tenant |
| Full Name          | Full name of the tenant  |
| Post Code          | Tenant's postal code    |
| Email Address      | Tenant's email address  |
| Contact Details    | Tenant's contact details  |
| Billing Address    | Tenant's billing address |
| Pay with           | Payment method (e.g., credit card, PayPal) |
| Add new card       | Option to add a new payment card |
| Donate to Charity  | Option to donate to charity |
| Subtotal           | Subtotal amount for the payment |
| Order Total        | Total amount to be paid |




# Venue Ariel Reservation Management System

Welcome to the Venue Reservation Management System! This system allows customers to browse, reserve, and manage event venues, while venue managers can efficiently manage reservations and resources. Let's explore the detailed user stories and features of this system.
### Website front page
![Ariel Logo](/media/products/frontwebsite.webp)
## Customer User Stories

### Browse Available Venues
As a customer, I want to browse through a list of available event venues with details such as types, capacities, amenities, and photos.
by Price, Rating Category, By Products.

![Ariel Logo](/media/products/all_products.webp)

### Check Venue Availability
I should be able to check the real-time availability of a specific venue for my desired date and time. and for the Type of the event

![Ariel Logo](/media/products/events.webp)
### check venue Features
as a user I can xploring the Features
with the List in menu features or functionalities of the venue.
For each feature, provide a clear description of what it does and how users can use it.
Include any relevant tips or best practices.
![Ariel Logo](/media/products/features.webp)
### special Offer
as a user members can easily find the section for special offers. You can include a dedicated "Special Offers"
![Ariel Logo](/media/products/special_offer.webp)

as a user how can easy see the website in Ipad Screen size
### Ipad Air front page
![Ariel Logo](/media/products/ipad_allproducts.webp)


as a user how can easy see the website in Iphone 14 pro Screen size
### Iphone 14 pro max front page
![Ariel Logo](/media/products/iphone_fronts.webp)

### Enjoy Browsing: 
Now, you can easily see and interact with the website on your website, iPad's or iphone screen. You can tap links, buttons, and images to navigate and explore the Venue Ariel website's content.


### Reserve a Venue
I want to reserve a venue by specifying the event date, time, and amenities, as well as customize event details.

### View and Manage Reservations
I need a dashboard to view and manage my reservations, including editing event details, updating timings, and making payments.
![Ariel Logo](/media/products/shopping.webp)
### Make Payments Online
I should be able to make online payments for my reservations, displaying the total cost and additional service fees.
![Ariel Logo](/media/products/checkup.webp)

### Receive Booking Confirmation
After making a reservation and payment, I should receive a booking confirmation email with event details and contact information.

### Request Support and Assistance
During the reservation process, I should have the option to request assistance from venue staff.

## Venue Manager User Stories

### Data Store Access Control

In our Venue Reservation Management System, we have implemented security measures to ensure that non-admin users cannot access the data store directly without going through the code. This is done to protect sensitive data and maintain the integrity of the system.  This ensures that sensitive data can only be accessed through the provided application interfaces, rather than through direct database queries or URL manipulation.

### How It Works

We have employed a custom middleware, `AdminAccessMiddleware`, to intercept incoming requests. This middleware checks whether the user attempting to access the data store is an admin (staff member) or not. If the user is not an admin, they will encounter a `PermissionDenied` exception, preventing them from accessing the data store directly.

### Why Is This Important?

1. **Data Security**: By restricting direct access, we enhance data security, ensuring that only authorized personnel can interact with the data store.

2. **Controlled Access**: This approach enforces controlled access to sensitive information, reducing the risk of unauthorized data retrieval.

### What Happens When a Non-Admin User Tries to Access the Data Store?

When a non-admin user attempts to access the data store directly, they will receive a `PermissionDenied` exception. This exception can be customized to handle the situation according to your application's requirements. For instance, you can redirect the user to a login page, display a custom error message, or take any other appropriate action.

### Customizing Exception Handling

To customize the behavior when a non-admin user encounters the `PermissionDenied` exception, you can modify the `AdminAccessMiddleware` or create a custom view and URL pattern to handle this exception gracefully.

Here's an example of how to create a custom view for handling the exception:

```python
from django.core.exceptions import PermissionDenied
from django.shortcuts import render

def permission_denied_view(request, exception):
    return render(request, 'custom_permission_denied.html', {'exception': exception})
![Ariel Logo](/media/products/middleware.webp)

### Manage Venue Listings
As a venue manager, I can manage venue listings by adding new venues, updating details, and marking venues as unavailable.
![Ariel Logo](/media/products/django_administration.webp)
### Approve Reservation Requests
I need to review and approve customer reservation requests, including payment status and event details.
![Ariel Logo](/media/products/django_categories.webp)
### User Managment Menu
![Ariel Logo](/media/products/django_menue.webp)
### User Managment Product
![Ariel Logo](/media/products/django_products.png)
### User Managment order
![Ariel Logo](/media/products/django_orders.webp)
### User Managment Site
![Ariel Logo](/media/products/django_sites.webp)
### User Managment 
![Ariel Logo](/media/products/django_user.webp)

### Set Pricing and Rental Policies
I should be able to set pricing for venues and additional services, such as rental rates and amenity fees.

### Manage Event Calendar
I need an event calendar to view confirmed reservations, pending requests, and blocked dates.

### Coordinate Staff and Resources
For approved reservations, I want to coordinate staff assignments, equipment setups, and logistical aspects.

### Generate Reports and Analytics
I need access to reports and analytics to analyze reservation trends, popular venues, and revenue generated.

## Customer Support

For assistance, customers can contact our support team at support@venuereserve.com or call 1-800-123-4567.

## Installation

1. Clone the repository: `git clone https://github.com/venue-reservation.git`
2. Install dependencies: `npm install`
3. Start the application: `npm start`

## License

Venue Reservation Management System is licensed under the [MIT License](LICENSE).

---
© 2023 Your Company Name

## Logo Creator

I used the website http://www.freelogocreator.com



## Logo Creator

I used the website hhttp:/www/freelogocreator.com


makemigrations --dry-run
showmigrations
migrate --plan
migrate

create a super user admin
python3 manage.py createsuperuser

install flake8 

pip install gunicorn whitenoise
pip3 install psycopg2-binary
pip3 install gunicorn

how to create a file pip3 freeze --local > requirements.txt
