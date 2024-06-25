from flask import Flask
from db import db
from config.mongo import mongo
from dotenv import load_dotenv
import os
from services.liberty_services import liberty
from flask_smorest import Api


def create_app():

    load_dotenv()


    app = Flask(__name__)
    app.config["PROPAGATE_EXCEPTIONS"] = True
    app.config["API_TITLE"] = "API Flask Python"
    app.config["API_VERSION"] = "V1"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
    app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    app.config["TESTING"] = True

    ##Configuración de la BDD
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL", "sqlite:///data.db")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)
 


    app.config['MONGO_URI'] = os.getenv('MONGO_URI')
    mongo.init_app(app=app)

    app.register_blueprint(liberty, url_prefix='/liberty')

    #Creará las tablas de la BBDD
    with app.app_context():
        db.create_all()

    return app


if __name__ == '__main__':
    ##
    app = create_app()
    app.run(debug=True, port=5000)
    
    