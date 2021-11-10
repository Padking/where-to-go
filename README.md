# Where to go

Сайт о самых интересных местах Москвы

## Описание

Интерактивная карта мест для организации досуга

### Начало работы

- Программисту необходимо:
  + создать [суперпользователя](https://github.com/Padking/where-to-go#установка),
  + [наполнить](https://github.com/Padking/where-to-go#установка) базу данных (БД).
- Контент-менеджеру/заказчику необходимо:
  + получить логин и пароль у администратора инф. системы (ИС)
  для работы с [Django admin site](https://docs.djangoproject.com/en/3.1/ref/contrib/admin/)
  или
  создать [суперпользователя](https://github.com/Padking/where-to-go#установка) самостоятельно

### Особенности

- помогает организовать досуг, отображая на карте замечательные места и развлечения возле дома и работы,
- предоставляет возможность:
    * создать/редактировать локации,
    * использовать визуальный редактор для текстовок,
    * поиска локации по названию,
    * создать/редактировать фото локации,
    * просмотра превью фотографий локаций,
    * удобно менять (drag & drop) порядок отображения фото на главной [сайта]((http://127.0.0.1:8000/),
    * подсчёта фото по локациям.
- обеспечивает загрузку информации о локациях в БД, используя [manage-команду](https://github.com/Padking/where-to-go#Manage-команда%20для%20загрузки%20данных%20в%20БД),
- [источник данных](https://github.com/devmanorg/where-to-go-places),
- статус проекта: учебный.

## Примеры использования


  **Выбор места для досуга:**

  ![index_page_1_leisure](https://github.com/Padking/where-to-go/blob/master/screenshots/index_page_1_leisure.gif)


  **Получить сырые данные о локации:**

  ![place_endpoint_page_1](https://github.com/Padking/where-to-go/blob/master/screenshots/place_endpoint_page_1.gif)


  **Создать/редактировать запись локации в БД:**

  ![admin_page_1_edit](https://github.com/Padking/where-to-go/blob/master/screenshots/admin_page_1_edit.gif)



## Сценарии использования

### Проверка работоспособности сайта в prod-среде на localhost

**Цель:** в браузере открывается подобный [сайт](https://devmanorg.github.io/where-to-go-frontend/).

**Шаги** (см. [раздел "Установка"](https://github.com/Padking/where-to-go#установка)):
- 1, [шаги](https://github.com/Padking/where-to-go#Организация%20prod-среды), 3-11 включительно.

### Проверка работоспособности панели администратора

**Цель:** убедиться в появлении на сайте тех локаций, которые были добавлены.

**Шаги** (см. [раздел "Установка"](https://github.com/Padking/where-to-go#установка)) при условии запущенного сайта в dev- или prod-среде:
- 11;

### Потенциальная доработка возможностей сайта в dev-среде на localhost

**Цель:** определяется программистом-исследователем.

**Шаги** (см. [раздел "Установка"](https://github.com/Padking/where-to-go#установка)):
- 1, 2, [шаги](https://github.com/Padking/where-to-go#Организация%20dev-среды), 3-11 включительно.


## Предметная область

### Схема сущностей БД

  ![index_page_1_leisure](https://github.com/Padking/where-to-go/blob/master/screenshots/ER-diagram.png)

### Пример исходных данных

```javascript
{
    "title": "Экскурсионный проект «Крыши24.рф»",
    "imgs": [
        "https://kudago.com/media/images/place/d0/f6/d0f665a80d1d8d110826ba797569df02.jpg",
        "https://kudago.com/media/images/place/66/23/6623e6c8e93727c9b0bb198972d9e9fa.jpg",
        "https://kudago.com/media/images/place/64/82/64827b20010de8430bfc4fb14e786c19.jpg",
    ],
    "description_short": "Хотите увидеть Москву с высоты птичьего полёта?",
    "description_long": "<p>Проект «Крыши24.рф» проводит экскурсии ...</p>",
    "coordinates": {
        "lat": 55.753676,
        "lng": 37.64
    }
}
```


## Структура проекта

### Главная страница

Реализована [html-шаблоном](https://github.com/Padking/where-to-go/blob/master/where_to_go/templates/index.html) и [контекстом](https://github.com/Padking/where-to-go/blob/master/where_to_go/where_to_go/views.py#L32).

[Тут](http://127.0.0.1:8000/).

### Панель администратора

Представляет собой кастомизированное приложение на базе [Django admin site](https://docs.djangoproject.com/en/3.1/ref/contrib/admin/).

Доступна при запущенном сайте по [адресу](http://127.0.0.1:8000/admin/).

### Endpoint сырых данных о локации

Формируется программным объектом [JsonResponse](https://docs.djangoproject.com/en/3.1/ref/request-response/#jsonresponse-objects).

Доступен при запущенном и наполненном данными сайте по [адресу](http://127.0.0.1:8000/places/12/).

### Manage-команда для загрузки данных в БД

Относится к кастомному Dj-приложению `places`, реализована в модуле `load_place.py`.

[Примеры работы](https://github.com/Padking/where-to-go#Примеры%20запуска)

### Используемые технологии

#### Frontend-часть
* [Bootstrap](https://getbootstrap.com/)
* [Leaflet](https://leafletjs.com/)
* [loglevel](https://www.npmjs.com/package/loglevel)
* [Vue.js](https://ru.vuejs.org/)

#### Backend-часть
* [Django](https://docs.djangoproject.com/en/3.1/)
* [django-admin-sortable2](https://django-admin-sortable2.readthedocs.io/en/latest/index.html#)
* [django-cleanup](https://pypi.org/project/django-cleanup/)
* [django-tinymce](https://github.com/jazzband/django-tinymce)
* [Docker](https://docs.docker.com/engine/)
* [Docker Compose](https://docs.docker.com/compose/)
* [geojson](https://python-geojson.readthedocs.io/en/latest/#)
* [Nginx](https://nginx.org/ru/docs/)
* [Pillow](https://pillow.readthedocs.io/en/stable/index.html)
* [PostgreSQL](https://postgrespro.ru/docs/postgresql/14/index)
* [requests](https://requests.readthedocs.io/en/master/)
* [uWSGI](https://uwsgi-docs.readthedocs.io/en/latest/)


## Требования к окружению

* Python 3.8 и выше,
* Linux/Windows,
* Переменные окружения (ПеО),
* Файлы для системы виртуализации (СВ).

Проект настраивается через ПеО, достаточно задать их в файлах `.env.override` и `.env.override.db`.
Передача значений ПеО происходит с использованием [environs](https://pypi.org/project/environs/).

Среды (dev-, prod-) определяются настройками в файлах `docker-compose.yml` и `docker-compose.dev.yml`.
По умолчанию проект подготовлен к запуску в prod-среде.

### Общие

#### Параметры проекта

|       Ключ        |     Назначение     |   По умолчанию   |
|-------------------|------------------|------------------|
|`ALLOWED_HOSTS`| Разрешённые хосты | - |
|`DEBUG`| Режим отладки | `False` |
|`SECRET_KEY`| Уникальное непредсказуемое значение | - |
|`FRONTEND_PART_APP_DIR`| Имя каталога с фронтенд-частью проекта |`where-to-go-frontend`|
|`STATIC_ROOT`| Имя каталога с статикой проекта |`static`|
|`STATIC_URL`| Имя path-части URL для отдачи статики |`/static/`|
|`MEDIA_ROOT`| Имя каталога с медиа-файлами проекта |`media`|
|`MEDIA_URL`| Имя path-части URL для отдачи медиа-файлов |`/media/`|
|`DJANGO_ENV`| Среда, в которой запускается проект |`production`|
|`PSQL_DB_ENGINE`| Имя движка СУБД |`django.db.backends.postgresql`|
|`PSQL_DB_HOST`| Имя сервиса развёрнутого в контейнере для БД | `db` |
|`PSQL_DB_PORT`| Порт СУБД | `5432` |
|`PSQL_DB_NAME`| Имя БД | `where_to_go` |
|`PSQL_DB_USER`| Имя пользователя БД | `proba` |
|`PSQL_DB_PASSWORD`| Пароль пользователя БД | `proba` |

#### Параметры подключения к БД

По умолчанию используется СУБД PostgreSQL.

|       Ключ        |     Назначение     |   По умолчанию   |
|-------------------|------------------|------------------|
|`POSTGRES_USER`| Суперпользователь БД | `postgres` |
|`POSTGRES_PASSWORD`| Пароль суперпользователя БД | - |


### Организация dev-среды

- создать на основе `env.override` и `env.override.db` файлы `env.dev` и `env.dev.db`,
- заполнить значениями ключи, у которых нет значений по умолчанию,
- переопределить значения ключей, указанных в таблице ниже,
- переименовать `docker-compose.dev.yml` в `docker-compose.yml`.

|       Ключ        |     Назначение     |   Должно стать   |
|-------------------|------------------|------------------|
|`DEBUG`| Режим отладки | `True` |
|`DJANGO_ENV`| Среда, в которой запускается проект |`development`|


### Организация prod-среды

- создать на основе `env.override` и `env.override.db` файлы `env.prod` и `env.prod.db`,
- заполнить значениями ключи, у которых нет значений по умолчанию.


## Установка

1. Клонировать проект:
```sh
git clone https://github.com/Padking/where-to-go.git
cd where-to-go
```
2. Создать каталог виртуального окружения (ВО)*,
   связать каталоги ВО и проекта,
   установить зависимости:
```sh
mkvirtualenv -p <path to python> <name of virtualenv>
setvirtualenvproject <path to virtualenv> <path to project>
pip install -r requirements_dev.txt
```
3. [Установить и настроить](https://docs.docker.com/engine/install/) Docker,
4. [Установить и настроить](https://docs.docker.com/compose/install/) Docker Compose,
5. Собрать образы для сервисов проекта,
   запустить контейнеры с сервисами в фоновом режиме:
```sh
docker-compose build
docker-compose up -d
```
6. Применить миграции к проекту:
```sh
docker-compose exec web python manage.py migrate --noinput
```
7. Собрать статику для проекта:
```sh
docker-compose exec web python manage.py collectstatic --clear
```
8. Применить фикстуру
```sh
docker-compose exec web python manage.py loaddata ./places/fixtures/db_data.json
```

9. Запустить [сайт](http://127.0.0.1:8000/),

10. Cоздать суперпользователя в интерактивном режиме**:
```sh
docker-compose exec web python manage.py createsuperuser
```
11. Наполнить БД информацией о локациях одним из способов:
    * через [Django admin site](https://docs.djangoproject.com/en/3.1/ref/contrib/admin/):
      - перейти на [сайт](http://127.0.0.1:8000/admin/),
      - войти под учётной записью, созданной в п.10 или сформированной администратором ИС-ы
      - совершить целевое действие,
      - убедиться в отображении локаций на главной странице [сайта](http://127.0.0.1:8000/).
    * используя manage-команду `load_place`:
      - получить справку по работе с manage-командой:
      ```sh
      docker-compose exec web python manage.py load_data --help
      ```
      - получить ссылку на данными о локации [описанным способом](https://github.com/devmanorg/where-to-go-places#как-скачать),
      - заполнить БД информацией о месте:
      ```sh
      docker-compose exec web python manage.py load_place <ссылка на данными о локации>
      ```
      - совершить целевое действие,
      - убедиться в отображении локаций на главной странице [сайта](http://127.0.0.1:8000/).

12. Завершить работу сайта:
```sh
docker-compose down
```


\* с использованием [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/index.html)

\** для наполнения БД через [Django admin site](https://docs.djangoproject.com/en/3.1/ref/contrib/admin/)


### Примеры запуска

```sh
$ docker-compose exec web python manage.py load_place --help
usage: manage.py load_place [-h] [--version] ... data_file_url

Создаёт записи об интересных местах и их фотографиях в БД.

positional arguments:
  data_file_url         URL-адрес json-файла с данными

optional arguments:
  -h, --help            show this help message and exit
...
```

```sh
$ docker-compose exec web python manage.py load_place https://github.com/devmanorg/where-to-go-places/raw/master/places/Воробьёвы%20горы.json
Интересное место и фото добавлены в БД из источника: https://github.com/devmanorg/where-to-go-places/raw/master/places/Воробьёвы%20горы.json
```
