# Проект YaCut
## Технологии
[![Python](https://img.shields.io/badge/-Python-464646?style=flat&logo=Python&logoColor=56C0C0&color=gray)](https://www.python.org/) [![Flask](https://img.shields.io/badge/-Flask-464646?style=flat&logo=Flask&logoColor=56C0C0&color=gray)](https://flask.palletsprojects.com/) [![Jinja2](https://img.shields.io/badge/-Jinja2-464646?style=flat&logo=Jinja&logoColor=56C0C0&color=gray)](https://jinja.palletsprojects.com/) [![SQLAlchemy](https://img.shields.io/badge/-SQLAlchemy-464646?style=flat&logo=sqlalchemy&logoColor=56C0C0&color=gray)](https://www.sqlalchemy.org/)
##### Полный список модулей, используемых в проекте, доступен в [requirements.txt](https://github.com/NECROshizo/yacut/blob/master/requirements.txt)
## Линтеры
[![Flake8](https://img.shields.io/badge/-flake8-464646?style=flat&logo=flake8&logoColor=56C0C0&color=gray)](https://flake8.pycqa.org/)


## Описание проекта
**Проект YaCut** — это сервис укорачивания ссылок. Его назначение — ассоциировать длинную пользовательскую ссылку с короткой, которую предлагает сам пользователь или предоставляет сервис.
#### Реализовано:
- генерация коротких ссылок для ссылок пользователя
- переадресация по коротким ссылкам на исходные ссылки пользователя
- дополнительные команды для записи в фаил css базы связей ссылок и коротких ссылок
- реализовано RESTful API для данного проекта

## Установка и настройки
#### Клонировать репозиторий:

```
git clone git@github.com:NECROshizo/yacut.git
cd yacut
```



#### Создание виртуального окружения:

```
python -m venv venv
```

#### Запуск виртуального окружения:

```
source venv/Scripts/activate - команда для Windows
source venv/bin/activate - команда для Linux и macOS
```
#### Установка зависимостей:

```
python -m pip install --upgrade pip
pip install -r requirements.txt
```
#### Настройка параметров допуска окружения к базе данных
```
touch .env
```
Шаблон файла **.env**
```
FLASK_APP=yacut
DATABASE_URI=<расположение и тип базы данных>
SECRET_KEY=<секретный ключ>
```
#### Создание базы данных
```
flask create_db
```
#### Запуск
```
flask run
```

## Автор
[**Оганин Пётр**](https://github.com/NECROshizo) 
2023 г.