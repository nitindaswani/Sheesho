# Sheesho

> A clean, full-stack Django e-commerce web app with custom admin operations, product discovery, reviews, and direct order placement.

[![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-Web%20Framework-092E20?logo=django&logoColor=white)](https://www.djangoproject.com/)
[![Database](https://img.shields.io/badge/Database-SQLite-003B57?logo=sqlite&logoColor=white)](https://www.sqlite.org/)
[![License](https://img.shields.io/badge/License-Not%20Specified-lightgrey)](#license)

## Overview

Sheesho is a Django-powered e-commerce platform focused on a smooth, direct-buy shopping flow.
Customers can register, browse products, view details, place orders, and track their own order history.
Administrators can manage products and view incoming orders through a custom admin panel.

## Highlights

- Customer registration and authentication
- Product listing and detail pages
- Product category support
- Product reviews and ratings
- Direct product order placement (buy-now flow)
- Customer-specific order history
- Custom admin login and dashboard
- Product management (create, update, delete)
- Media handling for product images

## Tech Stack

- Backend: Django
- Database: SQLite
- Frontend: HTML, CSS, Django Templates
- Media and static serving support: WhiteNoise + Django static/media configuration

## Architecture Notes

- Uses a custom `admin` app for admin-facing routes and dashboard behavior.
- Uses direct order flow per product (no cart/checkout aggregation model).
- Uses UUID-style identifiers across key business models.
- Uses separate Django apps for domain separation: `home`, `products`, `orders`, `register`, `login`, and custom `admin`.

## Quick Start

### 1. Clone the repository

```bash
git clone https://github.com/nitindaswani/Sheesho.git
cd Sheesho
```

### 2. Create and activate a virtual environment

```bash
# Windows
python -m venv .venv
.venv\Scripts\activate

# macOS/Linux
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install django pillow whitenoise
```

### 4. Apply migrations

```bash
python manage.py migrate
```

### 5. Create an admin account

```bash
python manage.py createsuperuser
```

### 6. Run the development server

```bash
python manage.py runserver
```

Visit: http://127.0.0.1:8000

## Core Routes

| Route                               | Description                      |
| ----------------------------------- | -------------------------------- |
| `/`                                 | Home page                        |
| `/about/`                           | About page                       |
| `/register/`                        | Customer registration            |
| `/login/`                           | Customer login                   |
| `/logout/`                          | Customer logout                  |
| `/orders/<pro_name>/<pro_id>/`      | Place order for selected product |
| `/orders/<user_id>/<name>/`         | Customer order history           |
| `/products/`                        | Admin product management         |
| `/products/add_product/`            | Add product                      |
| `/products/update_product/<pro_id>` | Update product                   |
| `/products/delete_product/<pro_id>` | Delete product                   |
| `/products/view_orders/`            | View all orders (admin)          |
| `/admin/`                           | Custom admin login               |

## Data Model Snapshot

### `products.Products`

- `pro_id` (UUID)
- `pro_name`
- `pro_desc`
- `pro_price`
- `pro_category`
- `pro_stock`
- `pro_image`

### `register.Users`

- `user_id` (UUID)
- `name`
- `email` (unique)
- `password` (hashed)
- `number`
- `address`
- `city`
- `state`
- `pincode`

### `orders.Orders`

- `order_id` (UUID)
- `ord_date`
- `status`
- `user_id`
- `name`
- `email`
- `address`
- `city`
- `state`
- `zip_code`
- `phone`
- `ord_pro_id`
- `ord_price`
- `ord_pro_name`

### `home.Review`

- `product` (FK -> Products)
- `user` (FK -> Users)
- `rating`
- `comment`
- `created_at`

## Project Structure

```text
sheesho/
|-- manage.py
|-- db.sqlite3
|-- sheesho/           # Project settings and root URLs
|-- home/              # Home pages and review logic
|-- login/             # Login flow
|-- register/          # User registration and profile data
|-- products/          # Product management and catalog
|-- orders/            # Order placement and history
|-- admin/             # Custom admin auth and dashboard
|-- templates/         # Django templates
|-- static/            # Source static assets
|-- staticfiles/       # Collected static files
`-- media/             # Uploaded product media
```

## Local Development Notes

- If local debugging is needed, set `DEBUG = True` in project settings.
- Confirm `ALLOWED_HOSTS` includes local hostnames for your environment.
- Static and media configuration is already present in the project.

## Contributing

1. Fork the repository.
2. Create a feature branch.
3. Commit with clear messages.
4. Open a pull request with a concise change summary.

## License

No explicit license file is currently included in this repository.

## Author

Nitin Daswani

- GitHub: https://github.com/nitindaswani
- Repository: https://github.com/nitindaswani/Sheesho
