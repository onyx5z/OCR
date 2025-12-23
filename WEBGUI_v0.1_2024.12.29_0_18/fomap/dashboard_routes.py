from flask import Blueprint, render_template

dashboard_routes = Blueprint('dashboard_routes', __name__)

@dashboard_routes.route('/')
def dashboard():
    return render_template('dashboard.html')

@dashboard_routes.route('/analytics')
def analytics():
    return render_template('analytics.html')