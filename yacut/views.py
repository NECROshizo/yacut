from flask import flash, redirect, render_template, Response
from flask import Markup

from . import app
from .constants import FlashMessege as flmessege
from .forms import LinkForm
from .models import URLMap
from .routes import ViewsRoute as route
from .utils import create_link, create_url_map, get_unique_short_id


@app.route(route.CONVERTER_VIEW.value, methods=['GET', 'POST'])
def converter_view() -> Response:
    """
    Обработчик страници конвертера ссылок с использованием формы
    Returns:
        Response: Страница с формой и краткой ссылкой.
    """
    form = LinkForm()
    if form.validate_on_submit():
        exists_entry = False
        short = form.custom_id.data
        original = form.original_link.data
        if not short:
            short, exists_entry = get_unique_short_id(url=original)
        elif URLMap.query.filter_by(short=short).first():
            flash(flmessege.TAKEN_ID.value.format(short))
            return render_template('convert.html', form=form)
        if not exists_entry:
            create_url_map(original, short)
        link = create_link(short)
        flash(Markup(flmessege.SHORT_LINK.value.format(link=link)))
    return render_template('convert.html', form=form)


@app.route(route.FOLLOWING_LINK_VIEW.value)
def following_link_view(custom_id: str) -> Response:
    """
    Перенаправляет пользователя по оригинальной ссылке на основе пользовательского ID.
    Args:
        custom_id (str): Пользовательский ID, используемый для идентификации сокращенной ссылки.
    Returns:
        Response: Страница пользователя по оригинальной ссылке.
    """
    link = URLMap.query.filter_by(short=custom_id).first_or_404().original
    return redirect(link)