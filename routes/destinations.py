# main_routes.py
from flask import Blueprint, render_template

destinations_bp = Blueprint('destinations', __name__)

@destinations_bp.route('/destinations')
def destinations():
    return render_template('destinations.html')
