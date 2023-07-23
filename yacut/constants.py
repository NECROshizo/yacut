from enum import Enum


class RePattern(Enum):
    SHORT_ID = r'^[A-Za-z0-9]{1,24}$'
    URL = r'^(https?|ftp)://[^\s/$.?#].[^\s]*$'


class APIErrorMessege(Enum):
    NOT_REQUEST = 'Отсутствует тело запроса'
    NOT_URL = '\"url\" является обязательным полем!'
    INVALID_URL = '"{}" не является ссылкой!'
    TAKEN_ID = 'Имя "{}" уже занято.'
    INVALID_ID = 'Указано недопустимое имя для короткой ссылки'
    NOT_ID = 'Указанный id не найден'


class FlashMessege(Enum):
    TAKEN_ID = 'Имя {} уже занято!'
    SHORT_LINK = (
        'Ваша новая ссылка готова:\n'
        '<a href="{link}">{link}</a>'
    )


class FormErrorMessage(Enum):
    DATA_REQIIRED = 'Обязательное поле'
    URL = 'В поле должна быть ссылка'
    LENGTH = 'Недопустимый длина. Максимальный размер {}'
    REQEXP = (
        'Недопустимы символы, разрешены только строчные'
        'и прописные латинские символы и цифры'
    )


class ModelParametr(Enum):
    MAX_LEN_ORIGINAL = 256
    MAX_LEN_SHORT = 24