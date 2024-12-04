from flask import Flask, jsonify, Blueprint
from ma import ma
from db import db
from routes import book_routes
from server.instance import server
from flask_migrate import Migrate

api = server.api
app = server.app
db.init_app(app)
ma.init_app(app)
migrate = Migrate(app, db)

def create_database():
    with app.app_context():
        db.create_all()  

book_routes.register_routes(api)

if __name__ == '__main__':
    create_database()
    server.run()
