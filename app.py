from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

# Sample products
products = [
    {"id": 1, "name": "Bat", "price": 500},
    {"id": 2, "name": "Ball", "price": 150},
    {"id": 3, "name": "Gloves", "price": 200},
    {"id": 4, "name": "Shoes", "price": 1000},
    {"id": 5, "name": "Guard", "price": 120},
    {"id": 6, "name": "Helmet", "price": 1500},
    {"id": 7, "name": "Pads", "price": 400},
    {"id": 8, "name": "Wickets", "price": 700},
]

cart = []

@app.route('/')
def index():
    return render_template('index.html', products=products)

@app.route('/add_to_cart/<int:product_id>')
def add_to_cart(product_id):
    product = next((item for item in products if item["id"] == product_id), None)
    if product:
        cart.append(product)
    return redirect(url_for('index'))

@app.route('/cart')
def view_cart():
    total = sum(item['price'] for item in cart)
    return render_template('cart.html', cart=cart, total=total)

@app.route('/checkout', methods=['GET', 'POST'])
def checkout():
    if request.method == 'POST':
        # Here you can handle the payment methods
        payment_method = request.form.get('payment')
        return f"Payment through {payment_method} successful!"
    return render_template('checkout.html')

# Updated to bind the app to all available network interfaces
if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)

