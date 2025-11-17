# 📦 **E-commerce Web Application using Django**

## 📌 **Project Overview**

This project is a fully functional e-commerce web application built using Django. It enables users to browse products, manage a shopping cart, register/login, and securely place orders. The system includes admin-level product management and cloud deployment support.

---

## 🎯 **Objectives**

* Develop a user-friendly and responsive e-commerce platform using Django.
* Implement core features such as user authentication, product catalog, shopping cart, and secure payment processing.
* Test and deploy the application on a cloud hosting platform.

---

## 📚 **Features**

### 👤 User Features

* User registration & login
* User profile & order history
* Password reset functionality

### 🛍️ Shopping Features

* Product listing & filtering
* Product detail pages
* Add to cart / remove from cart
* Cart quantity updates

### 💳 Checkout & Payment

* Checkout page
* Order creation & tracking
* Secure payment gateway integration

### 🛠 Admin Features

* Add, edit, delete products
* Manage categories & inventory
* Manage orders
* Basic analytics dashboard

---

## 🧱 **Technology Stack**

| Component       | Technology                                                |
| --------------- | --------------------------------------------------------- |
| Backend         | Django                                                    |
| Frontend        | HTML, CSS, JavaScript, Bootstrap/Tailwind                 |
| Database        | SQLite (development), PostgreSQL (production recommended) |
| Deployment      | Render / Railway / AWS / Docker                           |
| Version Control | Git & GitHub                                              |

---

## ⚙️ **Installation & Setup**

### 1️⃣ Clone the Repository

```
git clone https://github.com/m-ijaz-hussnain/ecommerce-webapp-django.git
cd eshop
```

### 2️⃣ Create a Virtual Environment

```
python -m venv venv
venv/Scripts/activate      # Windows
source venv/bin/activate   # Linux/Mac
```

### 3️⃣ Install Dependencies

```
pip install -r requirements.txt
```

### 4️⃣ Apply Migrations

```
python manage.py migrate
```

### 5️⃣ Create Superuser

```
python manage.py createsuperuser
```

### 6️⃣ Run the Server

```
python manage.py runserver
```

---

## 🔐 **Environment Variables**

Create `.env` file in root:

```
SECRET_KEY=your-secret-key
DEBUG=True
DATABASE_URL=
EMAIL_HOST=
EMAIL_PORT=
EMAIL_USER=
EMAIL_PASSWORD=
PAYMENT_GATEWAY_KEY=
```

---

## 🧪 **Testing**

```
python manage.py test
```

---

## ☁️ **Deployment**

Supported platforms:

* Render
* Railway
* Heroku
* AWS EC2
* Docker

---

## 🚀 **Future Enhancements**

* Wishlist system
* Product reviews & ratings
* REST API (Django REST Framework)
* Mobile app integration
* Inventory management system

---

## 🤝 **Contributing**

Pull requests are welcome. For major changes, please open an issue first.

---

## 📄 **License**

This project is licensed under the MIT License.
