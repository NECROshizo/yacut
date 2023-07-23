from typing import Tuple
from random import choices
from string import ascii_letters, digits

from flask import url_for

from . import db
from .models import URLMap


def create_link(custom_id: str, func: str = "following_link_view") -> str:
    """
    Создает ссылку на основе переданных параметров.
    Args:
        custom_id (str):        Идентификатор для короткой ссылке.
        func (str, optional):   Имя функции представления
                                для формирования ссылки.
    Returns:
        str: Сгенерированная ссылка.
    """
    link = url_for(
        func,
        custom_id=custom_id,
        _external=True,
    )
    return link


def create_url_map(original: str, short: str) -> None:
    """
    Создает записи URLMap.
    Args:
        original (str): Оригинальный URL.
        short (str):    Короткий URL.
    """
    url_map = URLMap(
        original=original,
        short=short,
    )
    db.session.add(url_map)
    db.session.commit()


def get_unique_short_id(url: str, quantity: int = 6) -> Tuple[str, bool]:
    """
    Получает уникальный короткий идентификатор для заданного URL
    Args:
        original (str): Оригинальный URL.
        quantity (int): Длина сгенерированного идентификатора.
                        По умолчанию равно 6.
    Returns:
        tuple:  Содержащий два элемента
                - сгенерированный идентификатор
                - булевое значение, указывающее существует ли
                  в базе идентификатор
    """
    target_url = URLMap.query.filter_by(
        original=url).order_by(URLMap.timestamp.desc()).first()
    if target_url is not None:
        return target_url.short, True
    simbol = ascii_letters + digits
    return ''.join(choices(simbol, k=quantity)), False
