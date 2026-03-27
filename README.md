# 🛍️ Sheesho - E-Commerce Platform

A modern, feature-rich e-commerce web application built with Django. Sheesho enables users to browse products, place orders, and manage their purchases with an intuitive and responsive interface.

---

## ✨ Features

- **User Authentication** - Secure registration and login system
- **Product Management** - Browse and view detailed product information
- **Shopping Cart** - Add products to cart and manage quantities
- **Order Management** - Place orders and track order history
- **Admin Dashboard** - Manage products, orders, and users
- **User Dashboard** - View personal profile and order history
- **Responsive Design** - Mobile-friendly interface
- **Category Organization** - Products organized by categories
- **Product Images** - Support for product images and media

---

## 🛠️ Tech Stack

- **Backend:** Django 3.x+
- **Database:** SQLite
- **Frontend:** HTML, CSS, JavaScript
- **Server:** Django Development Server
- **Version Control:** Git

---

## 📋 Table of Contents

- [Installation](#installation)
- [Environment Setup](#environment-setup)
- [Running the Application](#running-the-application)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [URL Routing](#url-routing)
- [Database Models](#database-models)
- [Contributing](#contributing)
- [License](#license)
- [Author](#author)

---

## 🚀 Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Git

### Step-by-Step Setup

1. **Clone the repository**

   ```bash
   git clone https://github.com/nitindaswani/Sheesho.git
   cd sheesho
   ```

2. **Create a Virtual Environment**

   ```bash
   # On Windows
   python -m venv venv
   venv\Scripts\activate

   # On macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install Dependencies**

   ```bash
   pip install django
   ```

4. **Apply Database Migrations**

   ```bash
   python manage.py migrate
   ```

5. **Create a Superuser (Admin Account)**

   ```bash
   python manage.py createsuperuser
   ```

   Follow the prompts to create your admin account.

---

## ⚙️ Environment Setup

The application uses SQLite as the default database, which requires no additional configuration. However, you may customize settings in `sheesho/settings.py`:

- **Database:** Located in `db.sqlite3`
- **Static Files:** Located in `static/` directory
- **Media Files:** Located in `media/` directory
- **Templates:** Located in `templates/` directory

---

## ▶️ Running the Application

Start the development server:

```bash
python manage.py runserver
```

The application will be available at:

```
http://localhost:8000
```

### Accessing Admin Panel

1. Navigate to: `http://localhost:8000/admin`
2. Log in with your superuser credentials
3. Manage products, orders, and users

---

## 💻 Usage

### For Users

1. **Register an Account**
   - Navigate to the registration page
   - Fill in your details (name, email, phone, password)
   - Submit to create your account

2. **Login**
   - Use your email and password to log in
   - Access your personal dashboard

3. **Browse Products**
   - Visit the home page to see all available products
   - Click on a product to view details
   - Add products to your cart

4. **Place an Order**
   - Navigate to the checkout page
   - Confirm your order details
   - Submit your order
   - Track your orders in the user dashboard

### For Administrators

1. Log in to the admin panel at `/admin`
2. Manage products: Add, edit, or delete products and categories
3. View all orders and user information
4. Monitor user registrations and activity

---

## 📁 Project Structure

```
sheesho/
├── manage.py                 # Django management script
├── db.sqlite3               # SQLite database
├── README.md                # Project documentation
│
├── sheesho/                 # Main Django project folder
│   ├── settings.py          # Project settings
│   ├── urls.py              # Main URL configuration
│   ├── wsgi.py              # WSGI configuration
│   └── asgi.py              # ASGI configuration
│
├── admin/                   # Admin app (admin dashboard)
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── admin.py
│
├── home/                    # Home app (landing page)
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── migrations/
│
├── products/                # Products app
│   ├── models.py            # Product and Category models
│   ├── views.py             # Product listing and detail views
│   ├── urls.py
│   └── migrations/
│
├── orders/                  # Orders app
│   ├── models.py            # Order model
│   ├── views.py             # Order creation and management
│   ├── urls.py
│   └── migrations/
│
├── register/                # Registration and authentication
│   ├── models.py            # User model
│   ├── views.py             # Registration and login views
│   ├── urls.py
│   └── migrations/
│
├── login/                   # Login app
│   ├── views.py             # Login logic
│   └── urls.py
│
├── templates/               # HTML templates
│   ├── base.html
│   ├── index.html
│   ├── login.html
│   ├── register.html
│   ├── product_detail.html
│   ├── show_products.html
│   ├── place_order.html
│   ├── user_orders.html
│   ├── admin_login.html
│   ├── all_orders.html
│   └── 404.html
│
├── static/                  # Static files (CSS, JS)
│   ├── css/
│   └── random/
│
├── media/                   # User-uploaded files
│   └── products/
│
└── staticfiles/             # Collected static files
```

---

## 🔗 URL Routing

Main URL patterns configured in `sheesho/urls.py`:

- `/` - Home page
- `/admin/` - Admin dashboard
- `/register/` - User registration
- `/login/` - User login
- `/products/` - Product listings
- `/orders/` - Order management
- `/user-orders/` - User's order history

---

## 🗄️ Database Models

### Key Models

**Products**

- `pro_id` - Product ID
- `pro_name` - Product name
- `pro_category` - Product category
- `pro_price` - Product price
- `pro_image` - Product image

**Users**

- `id` - User ID
- `name` - User's full name
- `email` - Email address
- `number` - Phone number
- `password` - Encrypted password

**Orders**

- `ord_id` - Order ID
- `ord_pro_id` - Product ordered
- `phone` - Delivery phone number
- `user_id` - User who placed the order
- `timestamp` - Order creation time

---

## 🤝 Contributing

Contributions are welcome! To contribute:

1. **Fork the repository**

   ```bash
   git clone https://github.com/nitindaswani/Sheesho.git
   ```

2. **Create a new branch**

   ```bash
   git checkout -b feature/your-feature-name
   ```

3. **Make your changes** and test them

4. **Commit your changes**

   ```bash
   git commit -m "Add your descriptive commit message"
   ```

5. **Push to your fork**

   ```bash
   git push origin feature/your-feature-name
   ```

6. **Submit a Pull Request** to the main branch

### Contribution Guidelines

- Follow PEP 8 style for Python code
- Write clear commit messages
- Test your changes before submitting
- Update documentation as needed

---

## 📄 License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

---

## 👤 Author

**Nitin Daswani**

- GitHub: [@nitindaswani](https://github.com/nitindaswani)
- Project: [Sheesho](https://github.com/nitindaswani/Sheesho)

---

## 📞 Support

For questions or issues:

- Open an issue on GitHub
- Contact the author through GitHub profile

---

## 🎯 Quick Start Summary

```bash
# 1. Clone and navigate
git clone https://github.com/nitindaswani/Sheesho.git
cd sheesho

# 2. Create virtual environment
python -m venv venv
venv\Scripts\activate

# 3. Install dependencies
pip install django

# 4. Run migrations
python manage.py migrate

# 5. Create superuser
python manage.py createsuperuser

# 6. Start server
python manage.py runserver
```

Then visit `http://localhost:8000` to see your application!

---

**Happy coding! 🚀**
