from datetime import datetime

from . import db
from .constants import ModelParametr as param


class URLMap(db.Model):
    """ Представляет собой отображение URL в базе данных.

    Attributes:
        __tablename__ (str): Имя таблицы базы данных.
        id (int): Первичный ключ отображения URL.
        original (str): Исходный URL.
        short (str): Сокращенный URL.
        timestamp (datetime): Временная метка создания отображения URL.
    """
    __tablename__ = 'url_map'
    id = db.Column(
        db.Integer,
        primary_key=True)
    original = db.Column(
        db.String(param.MAX_LEN_ORIGINAL.value),
        nullable=False,
    )
    short = db.Column(
        db.String(param.MAX_LEN_SHORT.value),
        unique=True,
        index=True,
        nullable=False,
    )
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return dict(
            id=self.id,
            original=self.original,
            short=self.short,
            timestamp=str(self.timestamp),
        )

    def __repr__(self):
        return str(self.to_dict())
