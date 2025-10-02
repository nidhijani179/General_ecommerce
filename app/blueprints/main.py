from flask import Blueprint, render_template, request
from app.models import Product, Category

main = Blueprint('main', __name__)

@main.route('/')
def index():
    trending_products = Product.query.order_by(Product.rating.desc()).limit(6).all()
    categories = Category.query.all()
    return render_template('index.html', trending_products=trending_products, categories=categories)

@main.route('/search')
def search():
    query = request.args.get('q', '')
    products = Product.query.filter(Product.name.contains(query)).all() if query else []
    return render_template('search.html', products=products, query=query)