from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
from routes import routes_blueprint
from flask_jwt_extended import JWTManager

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['JWT_SECRET_KEY'] = 'lol_ezz'
# db = SQLAlchemy(app)

jwt = JWTManager(app)
app.register_blueprint(routes_blueprint)

# def create_tables():
#     from models.user import User
#     with app.app_context():
#         db.create_all()

if __name__ == '__main__' :
    # create_tables()
    app.run(debug=True)