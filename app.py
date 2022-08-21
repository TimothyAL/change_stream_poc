
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://post:post@192.168.2.3:5432/changePOC"
    
    from models import db
    db.init_app(app)

    from person import people
    app.register_blueprint(people)

    app.run()

if __name__ == "__main__":
    create_app()