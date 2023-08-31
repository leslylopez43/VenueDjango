# VenueDjango
![Ariel Logo](/media/logoariel.webp)
allauth app itself log in and out

kaggle.com

###  "GET /favicon.ico HTTP/1.1" 404 2109

## Wireframe
![Ariel Logo](/media/products/wireframe_search.webp)
#### Front Website
![Ariel Logo](/media/products/wireframe_frontpage.webp)




## Tenant Table

| Field            | Description            |
|------------------|------------------------|
| Tenant ID        | Unique identifier for the tenant      |
| Name             | Tenant's first name     |
| Last Name        | Tenant's last name      |
| DOB              | Tenant's date of birth  |
| Plus 18's        | Number of tenants aged 18 and above   |
| Under 18's       | Number of tenants below 18 years old  |
| Email Address    | Tenant's email address  |
| Mobile Phone     | Tenant's mobile phone number |
| Address          | Tenant's address        |
| Post Code        | Tenant's postal code    |
| Country          | Tenant's country        |
| Billing Address  | Tenant's billing address |


## Tenancy Table

| Field            | Description            |
|------------------|------------------------|
| Accommodation ID | Unique identifier for the accommodation  |
| Tenant ID        | Unique identifier for the tenant  |
| Check-in         | Date and time of check-in  |
| Check-out        | Date and time of check-out |
| Sleeps           | Number of people accommodated |
| Venue Type       | Type of venue (e.g., hall, apartment) |

## Accommodation Table

| Field            | Description            |
|------------------|------------------------|
| Tenant ID        | Unique identifier for the tenant  |
| Accommodation ID | Unique identifier for the accommodation  |

### Hall 

| Field            | Description            |
|------------------|------------------------|
| Accommodation ID | Unique identifier for the hall  |
| Weddings         | Availability for weddings |
| Birthdays        | Availability for birthdays |
| Parties          | Availability for parties   |
| Baby Shower      | Availability for baby showers |
| Corporate Events | Availability for corporate events |
| Christmas        | Availability for Christmas events |
| Lilmedshoot & Photoshoot | Availability for lifestyle and photoshoots |


## Payments

| Field              | Description            |
|--------------------|------------------------|
| Tenant ID          | Unique identifier for the tenant  |
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

## Business or Owner Name

| Field              | Description            |
|--------------------|------------------------|
| Accommodation ID   | Unique identifier for the accommodation  |
| Name               | Name of the business or owner  |
| Business Name      | Name of the business  |
| Address            | Business or owner's address |
| Email Address      | Business or owner's email address |
| VAT                | VAT (Value Added Tax) information |



# Venue Ariel Reservation Management System

Welcome to the Venue Reservation Management System! This system allows customers to browse, reserve, and manage event venues, while venue managers can efficiently manage reservations and resources. Let's explore the detailed user stories and features of this system.
![Ariel Logo](/media/products/frontwebsite.webp)
## Customer User Stories

### Browse Available Venues
As a customer, I want to browse through a list of available event venues with details such as types, capacities, amenities, and photos.
![Ariel Logo](/media/products/all_products.webp)

### Check Venue Availability
I should be able to check the real-time availability of a specific venue for my desired date and time.
![Ariel Logo](/media/products/events.webp)
![Ariel Logo](/media/products/features.webp)
![Ariel Logo](/media/products/special_offer.webp)

### Reserve a Venue
I want to reserve a venue by specifying the event date, time, and amenities, as well as customize event details.

### View and Manage Reservations
I need a dashboard to view and manage my reservations, including editing event details, updating timings, and making payments.

### Make Payments Online
I should be able to make online payments for my reservations, displaying the total cost and additional service fees.

### Receive Booking Confirmation
After making a reservation and payment, I should receive a booking confirmation email with event details and contact information.

### Request Support and Assistance
During the reservation process, I should have the option to request assistance from venue staff.

## Venue Manager User Stories

### Manage Venue Listings
As a venue manager, I can manage venue listings by adding new venues, updating details, and marking venues as unavailable.

### Approve Reservation Requests
I need to review and approve customer reservation requests, including payment status and event details.

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
