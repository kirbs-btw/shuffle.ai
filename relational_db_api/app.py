from api import create_app
from apiflask import APIFlask
import os


port = os.getenv('PORT', '5001')
if __name__ == "__main__":
    app = create_app()
    app.run(host='0.0.0.0',port=int(port))