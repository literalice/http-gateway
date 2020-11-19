FROM registry.access.redhat.com/ubi8/python-38

COPY ./requirements.txt ./

RUN pip3 install -r requirements.txt

COPY ./ ./

EXPOSE 5000

CMD exec gunicorn app:app -c gunicorn_settings.py

