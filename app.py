from flask import Flask, render_template
from backend.config import Config
from backend.database import db 
from flask_restful import Api

def create_app():
    app = Flask(__name__,template_folder='frontend',static_folder='frontend/static')
    app.config.from_object(Config) 
    # Database Initialization
    db.init_app(app)

    #API Intialization
    api = Api(app)
    with app.app_context():
        db.create_all()
    app.app_context().push()

    return app,api
app,api = create_app()
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8000,debug=True)