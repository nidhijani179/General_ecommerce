from flask import Blueprint, render_template, request
from app.models import Product, Category

products = Blueprint('products', __name__)

@products.route('/')
def index():
    category_id = request.args.get('category')
    if category_id:
        products_list = Product.query.filter_by(category_id=category_id).all()
    else:
        products_list = Product.query.all()
    
    categories = Category.query.all()
    return render_template('products/index.html', products=products_list, categories=categories)

@products.route('/<int:id>')
def detail(id):
    product = Product.query.get_or_404(id)
    related_products = Product.query.filter(
        Product.category_id == product.category_id,
        Product.id != product.id
    ).limit(4).all()
    return render_template('products/detail.html', product=product, related_products=related_products)