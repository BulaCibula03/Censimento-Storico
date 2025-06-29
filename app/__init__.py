from flask import Flask
import os

def create_app():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    project_root = os.path.abspath(os.path.join(current_dir, '..'))
    
    app = Flask(
        __name__,
        template_folder=os.path.join(current_dir, 'templates'),
        static_folder=os.path.join(project_root, 'static')
    )
    
    app.config['SECRET_KEY'] = 'BVAKHKVJVABKL'
    app.config['DEBUG'] = True

    from .routes import bp
    app.register_blueprint(bp)
    
    return app