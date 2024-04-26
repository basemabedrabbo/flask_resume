from flask import Flask, render_template

app = Flask(__name__)

# @app.route() are Routes for the web pages. They are called decorators

# Create index page
@app.route('/')
def index():
	first_name = "John"
	pizza_topping  = ['Cheese', 'Pepperoni', 'Mashroum', 'Olives']
	topping_choice = pizza_topping[2]
	return render_template('index.html', toppings = pizza_topping, 
										 f_name = first_name,
										 choice = topping_choice)

# Create About page
@app.route('/about')
def about():
	#pass
	return render_template('about.html')