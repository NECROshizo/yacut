import os
from enum import Enum


class Config(object):
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv('SECRET_KEY') 


class ViewsRoute(Enum):
    CONVERTER_VIEW = '/'
    FOLLOWING_LINK_VIEW = '/<custom_id>'

HOSTS = "http://127.0.0.1:5000/"