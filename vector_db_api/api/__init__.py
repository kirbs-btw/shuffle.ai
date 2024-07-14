from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = '__something__to__see__'
    
    # telling app the sites exist 
    from .api import api
    
    # register blueprints
    app.register_blueprint(api, url_prefix='/')
    
    return app