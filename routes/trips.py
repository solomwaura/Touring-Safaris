# main_routes.py
from flask import Blueprint, render_template

trips_bp = Blueprint('trips', __name__)

@trips_bp.route('/trips')
def trips():
    return render_template('trips.html')
