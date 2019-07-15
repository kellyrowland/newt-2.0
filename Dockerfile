FROM ubuntu:latest
MAINTAINER Kelly L. Rowland <kellyrowland@lbl.gov>

WORKDIR /srv

RUN apt-get update && \
    apt-get install -y openssh-server iputils-ping git vim && \
    apt-get install -y python3-pip python3-dev && \
    cd /usr/local/bin && \
    ln -s /usr/bin/python3 python && \
    pip3 install --upgrade pip

RUN git clone -b docker https://github.com/NERSC/newt-2.0.git && \
    cd newt-2.0 && \
    pip install -r requirements.txt && \
    pip install django-404-middleware

RUN python /srv/newt-2.0/manage.py migrate

EXPOSE 8000

RUN /etc/init.d/ssh start

ADD docker-entrypoint.sh /srv/
RUN chmod +x docker-entrypoint.sh
ENTRYPOINT ["./docker-entrypoint.sh"]
CMD ["python", "/srv/newt-2.0/manage.py", "runserver", "0.0.0.0:8000"]
#CMD ["/bin/bash"]
