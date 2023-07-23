import csv
from datetime import datetime as dt

import click
from tqdm import tqdm

from . import app, db
from .models import URLMap


@app.cli.command('load_links')
@click.argument('file_csv', required=False)
def load_opinions_command(file_csv=None):
    """Функция загрузки мнений в базу данных."""
    if file_csv is None:
        date = dt.now().strftime('%Y-%m-%d')
        file_csv = f'database_{date}.csv'
    with open(file_csv, 'w', encoding='utf-8', newline='') as f:
        counter = 0
        query = db.session.query(URLMap).all()
        if not query:
            click.echo('База данных пуста')
        else:
            colums = ('id', 'original', 'short', 'timestamp')
            writer = csv.DictWriter(f, fieldnames=colums)
            writer.writeheader()
            for item in tqdm(query):
                writer.writerow(item.to_dict())
                counter += 1
            click.echo(f'Записано {counter} записей в фаил {file_csv}')


@app.cli.command('drop_db')
def drop():
    """Стирание базы данных"""
    db.drop_all()
    click.echo('База данных стерта')


@app.cli.command('create_db')
def drop():
    """Создание базы данных"""
    db.create_all()
    click.echo('База данных создана')