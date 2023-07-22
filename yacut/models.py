from datetime import datetime

from . import db


class URLMap(db.Model):
    """ Представляет собой отображение URL в базе данных.

    Attributes:
        __tablename__ (str): Имя таблицы базы данных.
        id (int): Первичный ключ отображения URL.
        original (str): Исходный URL.
        short (str): Сокращенный URL.
        timestamp (datetime): Временная метка создания отображения URL.
    """
    __tablename__ = 'URLMap'
    id = db.Column(db.Integer, primary_key=True)
    original = db.Column(db.String(256), nullable=False)
    short  = db.Column(db.String(24), unique=True, nullable=False)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
