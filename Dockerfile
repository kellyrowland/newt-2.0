FROM ubuntu:latest
MAINTAINER Kelly L. Rowland <kellyrowland@lbl.gov>

RUN apt-get update && \
    apt-get install -y iputils-ping git vim && \
    apt-get install -y python3-pip python3-dev && \
    cd /usr/local/bin && \
    ln -s /usr/bin/python3 python && \
    pip3 install --upgrade pip

RUN git clone -b docker https://github.com/kellyrowland/newt-2.0.git

WORKDIR /newt-2.0/

RUN pip install -r requirements.txt && \
    pip install django-404-middleware

RUN python manage.py migrate

EXPOSE 8000

ADD docker-entrypoint.sh /srv/
RUN chmod +x docker-entrypoint.sh
ENTRYPOINT ["./docker-entrypoint.sh"]
#CMD ["python", "/srv/newt-2.0/manage.py", "runserver", "0.0.0.0:8000"]
CMD ["/bin/bash"]
