#!/usr/bin/env sh
[ -d run ] || mkdir run && \
python3 ./manage.py migrate --noinput && \
chown -R www-data:www-data run && \
python3 ./manage.py collectstatic --noinput && \
uwsgi -i uwsgi.ini
