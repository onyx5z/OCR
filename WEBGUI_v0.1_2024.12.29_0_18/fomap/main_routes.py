from flask import Blueprint, render_template

# Create a Blueprint for main routes
main_routes = Blueprint('main_routes', __name__)

@main_routes.route('/')
def home():
    return render_template('home.html')  # Render home.html from the templates folder

@main_routes.route('/about')
def about():
    return render_template('about.html')  # Render about.html from the templates folder