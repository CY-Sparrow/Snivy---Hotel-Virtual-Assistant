import os
from flask import Flask 
from config import Config
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
load_dotenv()


app = Flask(__name__,instance_relative_config=True)
app.secret_key = os.getenv("SECRET_KEY")
app.config.from_object(Config)
os.makedirs(app.instance_path, exist_ok=True)
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.path.join(app.instance_path, 'snivy_database.db')}"
db = SQLAlchemy(app)
migrate = Migrate(app,db)
from app import routes, models, flow, refrence_no

