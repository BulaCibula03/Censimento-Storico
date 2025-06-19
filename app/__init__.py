from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

db = SQLAlchemy()

def create_app():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    project_root = os.path.abspath(os.path.join(current_dir, '..'))
    
    app = Flask(
        __name__,
        template_folder=os.path.join(current_dir, 'templates'),
        static_folder=os.path.join(project_root, 'static')
    )
    
    app.config['SECRET_KEY'] = 'BVAKHKVJVABKL'
    app.config['DEBUG'] = True # Imposta a False in produzione!

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(project_root, 'site.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    db.init_app(app)

    from app.routes import bp
    app.register_blueprint(bp)

    from app.models import User, Project, Task
    
    with app.app_context():
        db.create_all()

    return app