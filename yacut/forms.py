from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length, Optional, Regexp, URL

from .constants import FormErrorMessage as ermessage
from .constants import ModelParametr as param
from .constants import RePattern


class LinkForm(FlaskForm):
    """Форма для заполнения полей модели URLMap"""
    original_link = StringField(
        'Длинная ссылка',
        validators=[
            DataRequired(message=ermessage.DATA_REQIIRED.value),
            URL(require_tld=False, message=ermessage.URL.value),
            Length(
                1, param.MAX_LEN_ORIGINAL.value,
                message=ermessage.LENGTH.value.format(
                    param.MAX_LEN_ORIGINAL.value)
            ),
        ]
    )
    custom_id = StringField(
        'Ваш вариант короткой ссылки',
        validators=[
            Optional(),
            Length(
                1, param.MAX_LEN_SHORT.value,
                message=ermessage.LENGTH.value.format(
                    param.MAX_LEN_SHORT.value)
            ),
            Regexp(RePattern.SHORT_ID.value, message=ermessage.REQEXP.value)
        ]
    )
    submit = SubmitField('Создать')