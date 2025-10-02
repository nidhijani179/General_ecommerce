
<img width="1909" height="870" alt="Screenshot 2025-10-02 220016" src="https://github.com/user-attachments/assets/28818c6e-e40f-4170-b7fc-885dc3805fb1" />
<img width="1896" height="872" alt="Screenshot 2025-10-02 215954" src="https://github.com/user-attachments/assets/62c5b855-0ed7-4c9c-bdb7-8b523f1f9939" />
<img width="1883" height="868" alt="Screenshot 2025-10-02 220040" src="https://github.com/user-attachments/assets/55ff0e9a-b272-4bda-8d01-37f395ebc4f0" />
<img width="1914" height="873" alt="Screenshot 2025-10-02 220027" src="https://github.com/user-attachments/assets/d24a9d16-dbae-43ac-a669-f34401a03fb8" />

# ModernShop - Full-Stack E-commerce Website

A modern, Gen Z-friendly e-commerce website built with Flask, featuring a beautiful UI with animations and secure payment processing.

## Features

### 🎨 Modern Design
- Gen Z-friendly minimal layout with pastel/gradient color scheme
- Responsive design (mobile-first approach)
- Dark/Light mode toggle
- Smooth animations with GSAP and AOS
- Hover effects and parallax scrolling

### 🛍️ E-commerce Functionality
- Product catalog with categories
- Shopping cart and checkout
- User authentication and profiles
- Order history and management
- Admin panel for product/order management
- Search functionality

### 🔒 Security & Payments
- Secure user authentication with hashed passwords
- Stripe payment integration (demo mode)
- Session-based authentication
- CSRF protection

### 🎭 Animations & Interactions
- Scroll-triggered fade-in and slide animations
- Product card hover effects with zoom
- Smooth page transitions
- Interactive cart animations
- Parallax hero section

## Tech Stack

- **Backend**: Flask (Python)
- **Database**: SQLAlchemy + SQLite
- **Frontend**: Jinja2 templates
- **Styling**: Bootstrap 5 + TailwindCSS
- **Animations**: GSAP, AOS (Animate On Scroll)
- **Payments**: Stripe API
- **Authentication**: Flask-Login

## Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd Ecommerce
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   venv\Scripts\activate  # Windows
   # source venv/bin/activate  # Linux/Mac
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   - Copy `.env` file and update with your keys:
   ```
   SECRET_KEY=your-secret-key-here
   DATABASE_URL=sqlite:///ecommerce.db
   STRIPE_PUBLISHABLE_KEY=pk_test_your_stripe_key
   STRIPE_SECRET_KEY=sk_test_your_stripe_secret
   ```

5. **Run the application**
   ```bash
   python app.py
   ```

6. **Access the website**
   - Open http://localhost:5000 in your browser
   - Admin login: admin@example.com / admin123

## Project Structure

```
Ecommerce/
├── app/
│   ├── blueprints/          # Route blueprints
│   │   ├── main.py         # Home and search routes
│   │   ├── auth.py         # Authentication routes
│   │   ├── products.py     # Product routes
│   │   ├── cart.py         # Shopping cart routes
│   │   └── admin.py        # Admin panel routes
│   ├── templates/          # Jinja2 templates
│   │   ├── base.html       # Base template
│   │   ├── index.html      # Home page
│   │   ├── auth/           # Authentication templates
│   │   ├── products/       # Product templates
│   │   ├── cart/           # Cart templates
│   │   └── admin/          # Admin templates
│   ├── static/             # Static files
│   │   ├── css/style.css   # Custom styles
│   │   └── js/main.js      # JavaScript functionality
│   ├── __init__.py         # App factory
│   ├── models.py           # Database models
│   └── utils.py            # Utility functions
├── requirements.txt        # Python dependencies
├── .env                    # Environment variables
└── app.py                 # Application runner
```

## Key Features Explained

### 🏠 Home Page
- Animated hero banner with call-to-action
- Trending products carousel
- Shop by category section
- Feature highlights

### 🛒 Shopping Experience
- Product listing with filters
- Detailed product pages with zoom
- Shopping cart with quantity management
- Secure checkout process

### 👤 User Management
- User registration and login
- Profile page with order history
- Session-based authentication

### 🔧 Admin Panel
- Product management (add/edit/delete)
- Order management and tracking
- Dashboard with statistics

### 🎨 UI/UX Features
- Responsive design for all devices
- Dark/light mode toggle
- Smooth animations and transitions
- Modern gradient color schemes
- Interactive hover effects

## Customization

### Colors
Update CSS variables in `app/static/css/style.css`:
```css
:root {
    --primary-gradient: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    --accent-gradient: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
}
```

### Database
The app uses SQLite by default. For production, update `DATABASE_URL` in `.env` to use PostgreSQL:
```
DATABASE_URL=postgresql://username:password@localhost/dbname
```

### Payment Processing
Update Stripe keys in `.env` with your actual keys for production use.

## Deployment

### Heroku
1. Create Procfile: `web: python app.py`
2. Set environment variables in Heroku dashboard
3. Deploy using Git

### PythonAnywhere
1. Upload files to your account
2. Set up virtual environment
3. Configure WSGI file
4. Set environment variables

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

This project is open source and available under the MIT License.

## Support

For support or questions, please open an issue in the repository.

---

Built with ❤️ using Flask and modern web technologies.
