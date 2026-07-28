# 🛒 CodeAlpha E-Commerce Store (`CodeAlpha_Ecommerce_store`)

A full-stack, responsive, modern E-commerce web application built for the **CodeAlpha Full Stack Web Development Internship**.

---

## 📌 Project Features

- 🛍️ **Product Catalog & Search**: Interactive grid featuring product categories, real-time search filtering, prices, badges, and stock levels.
- 🔍 **Product Details Page**: High-resolution image gallery display, stock availability indicator, detailed specifications, and quantity selection.
- 🛒 **Dynamic Shopping Cart**: Real-time quantity adjustment, AJAX cart updates, automatic subtotal/shipping/tax calculation, and cart item removal.
- 💳 **Order Processing & Checkout**: Checkout form capturing shipping details, automatic stock reduction, order summary breakdown, and order confirmation.
- 👤 **User Registration & Login**: Built-in Django authentication allowing user signup, login, logout, and order history tracking.
- 🎨 **Modern Dark Glassmorphism UI**: Premium aesthetic with Google Font Inter, custom CSS glassmorphic cards, vibrant gradient accents, and responsive layout.

---

## 🛠️ Technology Stack

| Layer | Technology Used |
| :--- | :--- |
| **Backend** | Python 3, Django 4.2+ |
| **Database** | SQLite3 (Built-in zero-config database) |
| **Frontend** | HTML5, CSS3 (Custom Glassmorphism + Responsive Design), JavaScript (ES6 Fetch API) |
| **Icons & Fonts** | Bootstrap Icons, Google Fonts (Inter) |

---

## 🚀 Step-by-Step Execution Guide

### Step 1: Clone or Download the Project
```bash
git clone https://github.com/YOUR_GITHUB_USERNAME/CodeAlpha_Ecommerce_store.git
cd CodeAlpha_Simple_Ecommerce_Store
```

### Step 2: Create and Activate a Virtual Environment
- **Windows**:
  ```powershell
  python -m venv venv
  .\venv\Scripts\activate
  ```
- **macOS / Linux**:
  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Run Database Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### Step 5: Seed Sample Data (Categories & Products)
Populate the database with pre-configured products and categories:
```bash
python manage.py seed_data
```

### Step 6: Create an Admin Superuser (Optional)
```bash
python manage.py createsuperuser
```

### Step 7: Launch the Server
```bash
python manage.py runserver
```
Open your browser and visit: **`http://127.0.0.1:8000/`**

---

## 📤 Step-by-Step GitHub Upload Guide (CodeAlpha Submission)

1. **Initialize Git in the project root**:
   ```bash
   git init
   git add .
   git commit -m "Initial commit: CodeAlpha E-Commerce Store project"
   ```

2. **Create a new repository on GitHub**:
   - Go to [GitHub New Repository](https://github.com/new)
   - Repository Name: **`CodeAlpha_Ecommerce_store`**
   - Set visibility to **Public**
   - Click **Create repository**

3. **Link your local repository and push**:
   ```bash
   git branch -M main
   git remote add origin https://github.com/YOUR_GITHUB_USERNAME/CodeAlpha_Ecommerce_store.git
   git push -u origin main
   ```

---

## 📢 Step-by-Step LinkedIn Post & Submission Checklist

1. **Record a Video Explanation**:
   - Record a short 1–2 minute screen demo showing:
     - Browsing product catalog & category filters.
     - Viewing product details and adding items to cart.
     - Adjusting quantities in the shopping cart.
     - Completing the checkout form and order placement.
     - User registration/login feature.

2. **Post on LinkedIn**:
   - Post your demo video on LinkedIn.
   - Tag **@CodeAlpha** in your post content.
   - Include your GitHub Repository URL (`https://github.com/YOUR_GITHUB_USERNAME/CodeAlpha_Ecommerce_store`).
   - Mention your internship domain (*Full Stack Development*).

3. **Submit Task Form**:
   - Copy your GitHub Repository link and LinkedIn post link into the official CodeAlpha submission form.

---

## 📂 Project Directory Structure

```
CodeAlpha_Ecommerce_store/
│── ecommerce_project/        # Root Django settings & URL configuration
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
│── store/                    # E-commerce core application
│   ├── models.py             # Category, Product, Cart, CartItem, Order models
│   ├── views.py              # Catalog, Cart, Checkout, and Order views
│   ├── urls.py               # Store endpoint routing
│   ├── admin.py              # Django Admin panel registration
│   ├── context_processors.py # Dynamic navbar cart badge counter
│   ├── management/commands/  # seed_data command script
│   └── templates/store/      # Product list, detail, cart, checkout templates
│── accounts/                 # User authentication application
│   ├── views.py              # Registration, Login, Logout views
│   ├── urls.py               # Auth routing
│   └── templates/accounts/   # Register and Login UI templates
│── static/                   # Static styling & JS assets
│   ├── css/style.css         # Glassmorphic dark design system
│   └── js/main.js            # Interactive AJAX cart handling
│── manage.py                 # Django command line runner
│── requirements.txt          # Python dependencies
│── .gitignore                # Git exclusion configuration
└── README.md                 # Complete documentation & submission guide
```
