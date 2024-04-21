
# OnlineNurseryStore

GreenAura is a vibrant online nursery store built with Django, JavaScript, and Bootstrap. Dive into a world of greenery and gardening essentials!



## Features

- Browse and purchase a variety of plants and gardening products.
- User authentication and authorization system.
- Shopping cart functionality.
- Order management for users and administrators.
- Responsive design for a seamless experience across devices.


## Requirements
- Python
- Django
- JavaScript
- Bootstrap
## Installation

1. Clone the repository:

```bash
  git clone <repository-url>
```
2. Navigate into the project directory:

```bash
  cd NurserStore
```
3. Install dependencies:
```bash
    pip install -r requirements.txt
```
4. Run migrations:
```bash
    python manage.py migrate
```
5. Run the development server:
```bash
    python manage.py runserver
```
6. Access the application at http://localhost:8000 in your web browser.
## Configuration
- Database settings can be configured in settings.py.
- Static files and media settings can be adjusted in settings.py
## Usage
1. Register for an account or log in if you already have one.
2. Browse through the available plants and gardening products.
3. Add items to your cart and proceed to checkout.
4. Monitor your orders through the user dashboard.
5. With the provided credentails, one will be logged in to the respective interface.
- If a user log in, it takes to the customer user interface.
- If admin log in, it takes to the custom admin interface.
5. Administrators can manage products, orders, and users through the custom admin interface and also by django default admin ('/admin').

