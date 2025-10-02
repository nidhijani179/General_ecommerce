from app import db
from app.models import User, Category, Product

def create_sample_data():
    if User.query.first():
        return
    
    # Create admin user
    admin = User(username='admin', email='admin@example.com', is_admin=True)
    admin.set_password('admin123')
    db.session.add(admin)
    
    # Create categories
    categories = [
        Category(name='Electronics'),
        Category(name='Fashion'),
        Category(name='Home & Garden'),
        Category(name='Sports')
    ]
    
    for cat in categories:
        db.session.add(cat)
    
    db.session.commit()
    
    # Create sample products
    products = [
        Product(name='Wireless Headphones', description='Premium wireless headphones with noise cancellation', 
                price=199.99, image_url='https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=400', 
                category_id=1, stock=50, rating=4.5),
        Product(name='Smart Watch', description='Fitness tracking smartwatch with heart rate monitor', 
                price=299.99, image_url='https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=400', 
                category_id=1, stock=30, rating=4.3),
        Product(name='Designer T-Shirt', description='Premium cotton t-shirt with modern design', 
                price=49.99, image_url='https://images.unsplash.com/photo-1521572163474-6864f9cf17ab?w=400', 
                category_id=2, stock=100, rating=4.7),
        Product(name='Running Shoes', description='Lightweight running shoes for maximum comfort', 
                price=129.99, image_url='https://images.unsplash.com/photo-1542291026-7eec264c27ff?w=400', 
                category_id=4, stock=75, rating=4.6),
        Product(name='Coffee Maker', description='Automatic coffee maker with programmable timer', 
                price=89.99, image_url='https://images.unsplash.com/photo-1495474472287-4d71bcdd2085?w=400', 
                category_id=3, stock=25, rating=4.2),
        Product(name='Yoga Mat', description='Non-slip yoga mat for home workouts', 
                price=39.99, image_url='https://images.unsplash.com/photo-1544367567-0f2fcb009e0b?w=400', 
                category_id=4, stock=60, rating=4.4)
    ]
    
    for product in products:
        db.session.add(product)
    
    db.session.commit()