# -*- coding:utf-8 -*-
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from main.utils.jsonencoder import JSONEncoder
from datetime import timedelta
import logging

logger = logging.getLogger("AutoDeploy")
logger.setLevel(logging.INFO)
fh = logging.FileHandler('/home/dongmengyuan/AutoDeploy.logs')  #Log文件
fh.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(process)d - %(thread)d - %(message)s')
fh.setFormatter(formatter)
logger.addHandler(fh)

app = Flask(__name__,static_folder='../static',template_folder='../templates')

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:1322762504@localhost:3306/AutoDeploy"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config['PERMANENT_SESSION_LIFETIME']=timedelta(days=7)
app.config['SECRET_KEY']="123456"
db = SQLAlchemy(app)
db_session = db.session
app.json_encoder = JSONEncoder
from .controller import UserController,AdminController,ApiController