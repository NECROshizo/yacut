from enum import Enum


class ViewsRoute(Enum):
    """Маршруты для Web"""
    CONVERTER_VIEW = '/'
    FOLLOWING_LINK_VIEW = '/<custom_id>'


class APIViewsRoute(Enum):
    """Маршруты для API"""
    GET_SHORT_URL = '/api/id/'
    GET_URL = '/api/id/<short_id>/'
