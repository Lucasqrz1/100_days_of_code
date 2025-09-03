# * This project still needs error fixing and fine tuning *

# Flask eCommerce Website

A complete eCommerce web application built with Flask, featuring user authentication, shopping cart functionality, and real payment processing with Stripe.

## Features

### 🛒 **Core eCommerce Features**
- Product catalog with categories
- Shopping cart with session management
- Real payment processing via Stripe
- Order management and history
- Stock tracking and management

### 🔐 **Authentication & Security**
- User registration and login system
- Password hashing with Werkzeug
- Session-based authentication
- Protected routes for checkout and orders

### 💳 **Payment System**
- Stripe integration for secure payments
- Real-time payment processing
- Payment confirmation and receipts
- Order tracking with payment status

### 📱 **User Interface**
- Responsive Bootstrap design
- Mobile-friendly interface
- Shopping cart badge with item count
- Flash messages for user feedback
- Clean, modern design

## Technology Stack

- **Backend**: Flask (Python web framework)
- **Database**: SQLite with SQLAlchemy ORM
- **Authentication**: Flask-Login
- **Payment Processing**: Stripe API
- **Frontend**: Bootstrap 5, HTML5, CSS3, JavaScript
- **Icons**: Font Awesome

## Installation & Setup

### Prerequisites
- Python 3.7+
- pip package manager
- Stripe account (for payment processing)

### 1. Clone and Setup Environment
```bash
# Create project directory
mkdir flask-ecommerce
cd flask-ecommerce

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate
```

### 2. Install Dependencies
```bash
pip install flask flask-sqlalchemy flask-login stripe
```

### 3. Stripe Configuration
1. Create a Stripe account at [stripe.com](https://stripe.com)
2. Get your API keys from the Stripe dashboard
3. Replace the keys in `app.py`:
   ```python
   stripe.api_key = 'sk_test_your_stripe_secret_key_here'
   STRIPE_PUBLISHABLE_KEY = 'pk_test_your_stripe_publishable_key_here'
   ```

### 4. File Structure
Create the following directory structure:
```
flask-ecommerce/
│
├── app.py                 # Main Flask application
├── templates/             # HTML templates directory
│   ├── base.html
│   ├── index.html
│   ├── login.html
│   ├── register.html
│   ├── cart.html
│   ├── checkout.html
│   ├── payment_success.html
│   └── orders.html
└── ecommerce.db          # SQLite database (auto-generated)
```

### 5. Create Template Files
Copy each HTML template from the templates artifact into separate files in the `templates/` directory.

### 6. Security Configuration
**IMPORTANT**: Change the secret key in `app.py`:
```python
app.config['SECRET_KEY'] = 'your-super-secret-key-here-change-this'
```

## Running the Application

### Development Mode
```bash
python app.py
```

The application will run on `http://localhost:5000`

### Production Deployment
For production deployment, consider using:
- **Gunicorn** as WSGI server
- **PostgreSQL** instead of SQLite
- **Environment variables** for sensitive configuration
- **SSL certificate** for HTTPS

## Usage Guide

### For Customers

1. **Browse Products**
   - Visit the homepage to see available products
   - Products show name, description, price, and stock levels

2. **Shopping Cart**
   - Click "Add to Cart" to add products
   - View cart by clicking the cart icon in navigation
   - Remove items or adjust quantities in cart

3. **Account Management**
   - Register for a new account or login
   - View order history in "My Orders" section

4. **Checkout Process**
   - Login required for checkout
   - Review order summary
   - Enter payment details (use Stripe test cards)
   - Receive confirmation after successful payment

### Test Payment Cards (Stripe)
Use these test card numbers for development:
- **Visa**: 4242 4242 4242 4242
- **Mastercard**: 5555 5555 5555 4444
- **American Express**: 3782 822463 10005
- **Declined Card**: 4000 0000 0000 0002

Use any future expiry date and any CVC code.

## Database Models

### User Model
- ID, username, email, password_hash
- One-to-many relationship with orders

### Product Model
- ID, name, description, price, stock, image_url, category
- Linked to order items

### Order Model
- ID, user_id, total_amount, status, stripe_payment_id
- One-to-many relationship with order items

### OrderItem Model
- Links orders with products
- Stores quantity and price at time of purchase

## API Endpoints

### Public Routes
- `GET /` - Homepage with product catalog
- `GET /login` - Login form
- `POST /login` - Process login
- `GET /register` - Registration form  
- `POST /register` - Process registration
- `GET /cart` - View shopping cart
- `GET /add_to_cart/<product_id>` - Add product to cart

### Protected Routes (Login Required)
- `GET /checkout` - Checkout page
- `POST /process_payment` - Process Stripe payment
- `GET /payment_success/<order_id>` - Payment confirmation
- `GET /orders` - User's order history
- `GET /logout` - Logout user

## Customization

### Adding New Products
Products are automatically created when the app first runs. To add more:
1. Access the database directly, or
2. Create an admin interface, or
3. Add products via database management tool

### Styling Customization
- Modify Bootstrap classes in templates
- Add custom CSS for additional styling
- Update color scheme in Bootstrap variables

### Payment Gateway
Currently uses Stripe, but can be extended to support:
- PayPal
- Square
- Other payment processors

## Security Considerations

### Current Security Features
- Password hashing with Werkzeug
- CSRF protection via Flask-WTF (recommended to add)
- SQL injection prevention via SQLAlchemy ORM
- Session management

### Recommended Enhancements
- Add CSRF protection
- Implement rate limiting
- Add email verification
- Use HTTPS in production
- Environment variables for configuration
- Input validation and sanitization

## Troubleshooting

### Common Issues

**Database doesn't exist**
- The app creates the database automatically on first run
- Delete `ecommerce.db` to reset the database

**Stripe payments not working**
- Check your Stripe API keys
- Ensure you're using test keys in development
- Verify webhook endpoints if using webhooks

**Templates not found**
- Ensure all HTML files are in the `templates/` directory
- Check file names match exactly

**Cart not persisting**
- Cart uses Flask sessions
- Ensure secret key is set
- Check browser cookies are enabled

## Future Enhancements

### Planned Features
- **Admin Dashboard**: Product management interface
- **Email Notifications**: Order confirmations and updates
- **Reviews & Ratings**: Customer feedback system
- **Search & Filtering**: Advanced product search
- **Inventory Management**: Low stock alerts
- **Discounts & Coupons**: Promotional codes
- **Shipping Integration**: Real shipping calculations
- **Multi-currency Support**: International sales

### Technical Improvements
- **API Development**: REST API for mobile apps
- **Caching**: Redis for session and cart storage
- **Testing**: Unit and integration tests
- **Documentation**: API documentation with Swagger
- **Monitoring**: Application performance monitoring

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is open source and available under the MIT License.

---

**Happy selling!** 🛍️

For questions or support, please check the documentation or create an issue in the repository.