from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify
from flask_login import login_required, current_user
from app import db
from app.models import Product, CartItem, Order, OrderItem
import stripe
import os

stripe.api_key = os.getenv('STRIPE_SECRET_KEY')

cart = Blueprint('cart', __name__)

@cart.route('/')
@login_required
def index():
    cart_items = CartItem.query.filter_by(user_id=current_user.id).all()
    total = sum(item.product.price * item.quantity for item in cart_items)
    return render_template('cart/index.html', cart_items=cart_items, total=total)

@cart.route('/add/<int:product_id>')
@login_required
def add(product_id):
    product = Product.query.get_or_404(product_id)
    cart_item = CartItem.query.filter_by(user_id=current_user.id, product_id=product_id).first()
    
    if cart_item:
        cart_item.quantity += 1
    else:
        cart_item = CartItem(user_id=current_user.id, product_id=product_id, quantity=1)
        db.session.add(cart_item)
    
    db.session.commit()
    flash('Product added to cart!')
    return redirect(request.referrer or url_for('main.index'))

@cart.route('/remove/<int:item_id>')
@login_required
def remove(item_id):
    cart_item = CartItem.query.get_or_404(item_id)
    if cart_item.user_id == current_user.id:
        db.session.delete(cart_item)
        db.session.commit()
    return redirect(url_for('cart.index'))

@cart.route('/checkout')
@login_required
def checkout():
    cart_items = CartItem.query.filter_by(user_id=current_user.id).all()
    if not cart_items:
        flash('Your cart is empty!')
        return redirect(url_for('cart.index'))
    
    total = sum(item.product.price * item.quantity for item in cart_items)
    return render_template('cart/checkout.html', cart_items=cart_items, total=total)

@cart.route('/process-payment', methods=['POST'])
@login_required
def process_payment():
    cart_items = CartItem.query.filter_by(user_id=current_user.id).all()
    total = sum(item.product.price * item.quantity for item in cart_items)
    
    try:
        # Create Stripe payment intent
        intent = stripe.PaymentIntent.create(
            amount=int(total * 100),  # Convert to cents
            currency='usd',
            metadata={'user_id': current_user.id}
        )
        
        # Create order
        order = Order(user_id=current_user.id, total=total, status='completed')
        db.session.add(order)
        db.session.flush()
        
        # Add order items
        for item in cart_items:
            order_item = OrderItem(
                order_id=order.id,
                product_id=item.product_id,
                quantity=item.quantity,
                price=item.product.price
            )
            db.session.add(order_item)
        
        # Clear cart
        CartItem.query.filter_by(user_id=current_user.id).delete()
        db.session.commit()
        
        flash('Order placed successfully!')
        return redirect(url_for('auth.profile'))
        
    except Exception as e:
        flash('Payment failed. Please try again.')
        return redirect(url_for('cart.checkout'))