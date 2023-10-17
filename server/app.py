from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from server.routes.routes import create_routes

def create_app():
    app = Flask(__name__)
    db = SQLAlchemy()
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:142804@localhost:5432/sistema_notas'
    db.init_app(app)
    create_routes(app)
    CORS(app)
    return app

if __name__ == "__main__":
    app = create_app()
    try:
        app.run()
    except Exception as e:
        print(e)