FROM aduchi/py3-uwsgi
WORKDIR /opt/movietoday
EXPOSE 8000 9090
COPY ./requirements.txt /opt/movietoday/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt && rm -rf ~/.cache
COPY ./manage.py /opt/movietoday/
COPY ./movietoday/ /opt/movietoday/movietoday/
COPY ./cinema/ /opt/movietoday/cinema/
COPY ./start.sh /opt/movietoday/
COPY ./uwsgi.ini /opt/movietoday/
CMD ./start.sh
