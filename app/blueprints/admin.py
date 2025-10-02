from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from functools import wraps
from app import db
from app.models import Product, Category, Order

admin = Blueprint('admin', __name__)

def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.is_authenticated or not current_user.is_admin:
            flash('Admin access required')
            return redirect(url_for('main.index'))
        return f(*args, **kwargs)
    return decorated_function

@admin.route('/')
@login_required
@admin_required
def dashboard():
    products_count = Product.query.count()
    orders_count = Order.query.count()
    recent_orders = Order.query.order_by(Order.created_at.desc()).limit(5).all()
    return render_template('admin/dashboard.html', 
                         products_count=products_count, 
                         orders_count=orders_count,
                         recent_orders=recent_orders)

@admin.route('/products')
@login_required
@admin_required
def products():
    products_list = Product.query.all()
    return render_template('admin/products.html', products=products_list)

@admin.route('/products/add', methods=['GET', 'POST'])
@login_required
@admin_required
def add_product():
    if request.method == 'POST':
        product = Product(
            name=request.form['name'],
            description=request.form['description'],
            price=float(request.form['price']),
            image_url=request.form['image_url'],
            category_id=int(request.form['category_id']),
            stock=int(request.form['stock'])
        )
        db.session.add(product)
        db.session.commit()
        flash('Product added successfully!')
        return redirect(url_for('admin.products'))
    
    categories = Category.query.all()
    return render_template('admin/add_product.html', categories=categories)

@admin.route('/orders')
@login_required
@admin_required
def orders():
    orders_list = Order.query.order_by(Order.created_at.desc()).all()
    return render_template('admin/orders.html', orders=orders_list)