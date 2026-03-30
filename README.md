# Sheesho - Django E-Commerce Project

Sheesho is an e-commerce web application built with Django. It supports customer registration and login, product browsing, product reviews, direct order placement, and a custom admin dashboard for managing products and orders.

## Features

- Customer registration and login (session-based)
- Product listing with category filtering
- Product detail page with customer reviews
- Direct order placement for a selected product
- Customer order history view
- Custom admin login and dashboard
- Product CRUD for admins
- Media upload support for product images

## Tech Stack

- Backend: Django (project generated with Django 6.0 settings template)
- Database: SQLite
- Frontend: HTML, CSS, Django Templates
- Static serving support: WhiteNoise middleware configured

## Project Notes

- This project uses a custom app named admin for admin login/dashboard routes.
- django.contrib.admin is currently disabled in settings.
- The order flow is direct buy-now checkout, not a multi-item cart.

## Installation

### Prerequisites

- Python 3.8+
- pip

### Setup

1. Clone the repository:

```bash
git clone https://github.com/nitindaswani/Sheesho.git
cd Sheesho
```

2. Create and activate virtual environment:

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

3. Install dependencies:

```bash
pip install django whitenoise pillow
```

4. Run migrations:

```bash
python manage.py migrate
```

5. Create an admin user for custom admin login (Django auth user with staff access):

```bash
python manage.py createsuperuser
```

6. Start development server:

```bash
python manage.py runserver
```

Open: http://127.0.0.1:8000

## URL Overview

Main URL mappings are defined in sheesho/urls.py.

- / -> Home page
- /about/ -> About page
- /register/ -> Customer registration
- /login/ -> Customer login
- /logout/ -> Customer logout
- /products/ -> Admin product management page
- /products/add_product/ -> Add product (admin)
- /products/update_product/<pro_id> -> Update product (admin)
- /products/delete_product/<pro_id> -> Delete product (admin)
- /products/view_orders/ -> View all orders (admin)
- /orders/<pro_name>/<pro_id>/ -> Place order for a product
- /orders/<user_id>/<name>/ -> Customer order history page
- /admin/ -> Custom admin login page

## Data Models

### products.products

- pro_id (UUID)
- pro_name
- pro_desc
- pro_price
- pro_category
- pro_stock
- pro_image

### register.users

- user_id (UUID)
- name
- email (unique)
- password (hashed)
- number
- address
- city
- state
- pincode

### orders.orders

- order_id (UUID)
- ord_date
- status
- user_id
- name
- email
- address
- city
- state
- zip_code
- phone
- ord_pro_id
- ord_price
- ord_pro_name

### home.Review

- product (FK -> products)
- user (FK -> users)
- rating
- comment
- created_at

## Project Structure

```text
sheesho/
|-- manage.py
|-- db.sqlite3
|-- README.md
|-- sheesho/
|   |-- settings.py
|   |-- urls.py
|   |-- wsgi.py
|   `-- asgi.py
|-- home/
|-- login/
|-- register/
|-- products/
|-- orders/
|-- admin/
|-- templates/
|-- static/
|-- media/
`-- staticfiles/
```

## Development Notes

- DEBUG is currently set to False in settings. For local development, set it to True if needed.
- ALLOWED_HOSTS includes localhost and 127.0.0.1.
- Static and media paths are configured in settings.py.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push and open a pull request

## License

No license file is currently included in this repository.

## Author

Nitin Daswani

- GitHub: https://github.com/nitindaswani
- Project: https://github.com/nitindaswani/Sheesho
