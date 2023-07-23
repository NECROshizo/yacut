from http import HTTPStatus as code
from re import match
from typing import Dict, Any, Tuple

from flask import jsonify, request

from . import app
from .constants import APIErrorMessege as ermessege
from .constants import RePattern
from .error_handlers import InvalidAPIUsage
from .models import URLMap
from .routes import APIViewsRoute as route
from .utils import create_link, create_url_map, get_unique_short_id


@app.route(route.GET_SHORT_URL.value, methods=['POST'])
def get_short_url() -> Tuple[Dict[str, Any], int]:
    """
    Обработка POST-запроса для получения ссылки с коротким индефикатором.
    Returns:
        JSON-ответ с оригинальным URL и коротким URL
        и статус кодом 201 (CREATED) в случае успеха.
        Исключение InvalidAPIUsage с пользовательским сообщением
        и статус кодом 400 (BAD REQUEST).
    """
    data = request.get_json()
    exists_entry = False

    if not data:
        raise InvalidAPIUsage(ermessege.NOT_REQUEST.value)

    url = data.get('url')
    if not url:
        raise InvalidAPIUsage(ermessege.NOT_URL.value)
    elif not match(RePattern.URL.value, url):
        raise InvalidAPIUsage(ermessege.INVALID_URL.value.format(url))

    custom_id = data.get('custom_id')
    if not custom_id:
        custom_id, exists_entry = get_unique_short_id(url=url)
    elif custom_id and URLMap.query.filter_by(short=custom_id).first():
        raise InvalidAPIUsage(ermessege.TAKEN_ID.value.format(custom_id))
    elif not match(RePattern.SHORT_ID.value, custom_id):
        raise InvalidAPIUsage(ermessege.INVALID_ID.value)

    if not exists_entry:
        create_url_map(url, custom_id)

    response = {
        'url': url,
        'short_link': create_link(custom_id)
    }
    return jsonify(response), code.CREATED


@app.route(route.GET_URL.value, methods=['GET'])
def get_url(short_id: str) -> Tuple[Dict[str, Any], int]:
    """
    Обработка GET-запроса для получения URL по заданному short_id.
    Args:
        short_id (str): идентификатор URL
    Returns:
        - JSON-ответ с оригинальным URL и статус кодом 200 (OK),
          в случае успеха.
        - Исключение InvalidAPIUsage с пользовательским сообщением
          и статус кодом 404 (NOT FOUND).
    """
    link = URLMap.query.filter_by(short=short_id).first()
    if not link:
        raise InvalidAPIUsage(ermessege.NOT_ID.value, code.NOT_FOUND)
    request = {
        'url': link.original
    }
    return jsonify(request), code.OK
