FROM python:3.7-alpine
MAINTAINER Kelly L. Rowland <kellyrowland@lbl.gov>

RUN apk update && apk upgrade && \
    apk add --no-cache bash git openssh gcc musl-dev libffi-dev libressl-dev

RUN git clone https://github.com/NERSC/newt-2.0.git && \
    cd newt-2.0 && \
    git checkout py3 && \
    pip install -r requirements.txt
