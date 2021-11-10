#!/bin/sh

set -o errexit
set -o nounset

/usr/local/bin/uwsgi --ini /application/wsgi/uwsgi.ini
