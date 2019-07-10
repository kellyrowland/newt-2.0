FROM python:3.7-alpine
MAINTAINER Kelly L. Rowland <kellyrowland@lbl.gov>

WORKDIR /srv

RUN apk update && apk upgrade && \
    apk add --no-cache bash git openssh gcc musl-dev libffi-dev && \
    apk add --no-cache libressl-dev libmagic

RUN git clone -b py3 https://github.com/NERSC/newt-2.0.git && \
    cd newt-2.0 && \
    pip install -r requirements.txt && \
    python manage.py migrate

ADD docker-entrypoint.sh /srv/
RUN chmod +x docker-entrypoint.sh
ENTRYPOINT ["./docker-entrypoint.sh"]
CMD ["python", "/srv/newt-2.0/manage.py", "runserver"]