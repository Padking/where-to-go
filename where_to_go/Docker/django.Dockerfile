FROM python:3.8.3-alpine

ENV USR_LOCAL_BIN=/usr/local/bin/  \
    PROJECT_ROOT=/application

ENV PYTHONFAULTHANDLER=1 \
  PYTHONUNBUFFERED=1 \
  PYTHONHASHSEED=random \
  PIP_NO_CACHE_DIR=off \
  PIP_DISABLE_PIP_VERSION_CHECK=on \
  PIP_DEFAULT_TIMEOUT=100

# Пакеты для установки зависимостей
ENV BUILD_PACKAGES \
    # Зависимости общие
    gcc \
    # Зависимости для uWSGI
    build-base \
    pcre-dev \
    linux-headers \
    # Зависимости для psycopg2
    musl-dev \
    postgresql-dev \
    python3-dev \
    # Зависимости для Pillow
    jpeg-dev \
    zlib-dev \
    libjpeg

RUN mkdir $PROJECT_ROOT/ && \
    mkdir $PROJECT_ROOT/run && \
    mkdir $PROJECT_ROOT/wsgi && \
    mkdir $PROJECT_ROOT/logs && \
    mkdir $PROJECT_ROOT/static && \
    mkdir $PROJECT_ROOT/media

WORKDIR $PROJECT_ROOT

RUN pip install --upgrade pip && \
    apk update && \
    apk add $BUILD_PACKAGES

COPY ./requirements_prod.txt $PROJECT_ROOT/
RUN pip install -r requirements_prod.txt

# Копирование исходных файлов проекта
COPY . $PROJECT_ROOT/

COPY ./Docker/scripts/*.sh $USR_LOCAL_BIN/

RUN for i in $USR_LOCAL_BIN/*.sh; do \
    sed -i 's/\r//' $i; \
    chmod +x $i; \
    done

COPY ./Docker/uwsgi.ini $PROJECT_ROOT/wsgi

ENV COLUMNS 80

EXPOSE 8000

ENTRYPOINT ["entrypoint.sh"]

CMD ["start_uwsgi.sh"]
