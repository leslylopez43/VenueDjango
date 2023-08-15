# VenueDjango

allauth app itself log in and out

kaggle.com

###  "GET /favicon.ico HTTP/1.1" 404 2109

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

### Apartments 

| Field            | Description            |
|------------------|------------------------|
| Accommodation ID | Unique identifier for the apartment  |
| Check-in         | Date and time of check-in  |
| Check-out        | Date and time of check-out |
| Guest            | Number of guests          |
| Rooms            | Number of rooms           |
| Check Availability | Availability of the apartment |

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


## Guest Stories
# Accommodation Management System Ariel 
[![Ariel](/img/Ariel%20Logo.webp)](/img/LogoAriel.webp)


Welcome to the Accommodation Management System! This system helps you manage tenant information, tenancy details, accommodation availability, and payments. Let's dive into the story of how these tables work together to streamline the accommodation management process.

## Tenant Table

The **Tenant Table** serves as the foundation of the system. It stores essential information about tenants, such as their names, dates of birth, contact details, and addresses. Each tenant is assigned a unique **Tenant ID** to ensure accurate identification.

## Tenancy Table

As tenants book accommodations, their tenancy details are recorded in the **Tenancy Table**. This table links the tenants from the **Tenant Table** to their respective accommodations. I track the check-in and check-out dates, the number of people accommodated (**Sleeps**), and the type of venue they choose (**Venue Type**).

## Accommodation Table

To maintain a comprehensive view of each tenant's accommodations, I connect the **Tenant Table** and the **Tenancy Table** through the **Accommodation Table**. This table holds the unique identifiers for both the tenants and the accommodations.

### Hall Table and Apartments Table

Depending on the type of accommodation, I have two additional tables. The **Hall Table** manages availability for our halls, catering to various events like weddings, birthdays, parties, and more. On the other hand, the **Apartments Table** handles the availability of our apartments, specifying check-in and check-out dates, the number of guests, rooms, and the option to check availability.

## Payments

To ensure seamless and secure transactions, I have the **Payments Table**. This table connects with the **Tenant Table** using the **Tenant ID**. I store the tenant's payment details, including their full name, postal code, email address, contact details, billing address, payment method, and the option to add new cards. Additionally, tenants have the option to donate to charity through our system. The **Subtotal** and **Order Total** fields provide a clear overview of the payment details.

## Business or Owner Name

Finally, I have the **Business or Owner Name Table**. This table connects with the **Accommodation Table** and stores the details of the business or owner associated with each accommodation. It includes their name, business name, address, email address, and VAT information.

That wraps up my story of the Accommodation Management System and the interconnected tables within it. With this system in place, you can efficiently manage tenant information, tenancy details, accommodation availability, and payments. 


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
