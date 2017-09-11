#!/bin/ash

cd ..
yarn install

cd blog

python manage.py compress
python manage.py collectstatic --noinput
python manage.py migrate

uwsgi --ini /code/conf/uwsgi.ini