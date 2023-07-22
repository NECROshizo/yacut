from flask import flash, redirect, render_template, request, url_for, Response
from flask import Markup

from . import app, db, HOSTS, ViewsRoute
from .forms import LinkForm
from .models import URLMap
from .utils import get_unique_short_id



@app.route(ViewsRoute.CONVERTER_VIEW.value, methods=['GET', 'POST'])
def converter_view():
    form = LinkForm()
    if form.validate_on_submit():
        short = form.custom_id.data
        if not short:
            short = get_unique_short_id()
        elif URLMap.query.filter_by(short = short).first():
            flash(f'Имя {short} уже занято!')
            return render_template('convert.html', form=form)
        url_map = URLMap(
            original=form.original_link.data,
            short=short,
        )
        db.session.add(url_map)
        db.session.commit()
        link = url_for(
            "following_link_view",
            custom_id=short,
            _external=True,)
        flash(Markup(f'Ваша новая ссылка готова:\n'
              f'<a href="{link}">'
              f'{link}</a>'))
    return render_template('convert.html', form=form)  


@app.route(ViewsRoute.FOLLOWING_LINK_VIEW.value)
def following_link_view(custom_id: str) -> Response:
    """
    Перенаправляет пользователя по оригинальной ссылке на основе пользовательского ID.
    Args:
        custom_id (str): Пользовательский ID, используемый для идентификации сокращенной ссылки.
    Returns:
        Redirect: Перенаправляет пользователя по оригинальной ссылке.
    """
    link = URLMap.query.filter_by(short = custom_id).first_or_404().original
    return redirect(link)