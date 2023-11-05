from flask import Flask
from routes.main import main_bp

app = Flask(__name__)

# register the main blueprint
app.register_blueprint(main_bp)

# path for templates and static files
app.template_folder = 'templates'
app.static_folder = 'public'

if __name__ == '__main__':
    app.run(debug=True)
