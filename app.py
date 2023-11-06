from flask import Flask
from routes.main import main_bp, render_template
from routes.destinations import destinations_bp
from routes.trips import trips_bp

app = Flask(__name__)

# register the main blueprint
app.register_blueprint(main_bp)
app.register_blueprint(trips_bp)
app.register_blueprint(destinations_bp)

# path for templates and static files
app.template_folder = 'templates'
app.static_folder = 'public'

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')


if __name__ == '__main__':
    app.run(debug=True)
