# Импортируем метод jsonify
from random import randrange
from http import HTTPStatus as code
from re import match

from flask import jsonify, request, url_for

from . import app, db
from .error_handlers import InvalidAPIUsage
from .models import URLMap
from .utils import get_unique_short_id

pattern = r'^[A-Za-z0-9]{1,24}$'


@app.route('/api/id/', methods=['POST'])  
def get_short_url():
    data = request.get_json()
    if not data:
        raise InvalidAPIUsage("Отсутствует тело запроса", code.BAD_REQUEST)
    if 'url' not in data:
        raise InvalidAPIUsage('\"url\" является обязательным полем!', code.BAD_REQUEST)
    custom_id = data.get('custom_id')
    if not custom_id or custom_id=='':
        custom_id=get_unique_short_id()
    elif custom_id and URLMap.query.filter_by(short = custom_id).first():
        raise InvalidAPIUsage(f'Имя "{custom_id}" уже занято.', code.BAD_REQUEST)
    elif not match(pattern, custom_id):
        raise InvalidAPIUsage('Указано недопустимое имя для короткой ссылки', code.BAD_REQUEST)

    url_map = URLMap(
            original=data.get('url'),
            short=custom_id,
        )
    db.session.add(url_map)
    db.session.commit()
    response = {
        'url':url_map.original,
        'short_link':url_for(
            "following_link_view",
            custom_id=url_map.short,
            _external=True,)
    }
    return jsonify(response), code.CREATED


@app.route('/api/id/<short_id>/', methods=['GET'])  
def get_url(short_id):
    link = URLMap.query.filter_by(short = short_id).first()
    if not link:
        raise InvalidAPIUsage("Указанный id не найден", code.NOT_FOUND)
    request = {
         'url': link.original
    }

    return jsonify(request), code.OK