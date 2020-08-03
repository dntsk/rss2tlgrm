FROM python:3.7-alpine

ADD requirements.txt /opt/requirements.txt
ADD fetchfeeds /etc/periodic/15min/fetchfeeds

RUN set -ex \
    && apk add --no-cache --virtual .build-deps postgresql-dev build-base \
    jpeg-dev zlib-dev libjpeg libxml2-dev libxslt-dev \
    && python -m venv /env \
    && /env/bin/pip install --upgrade pip \
    && /env/bin/pip install --no-cache-dir -r /opt/requirements.txt \
    && runDeps="$(scanelf --needed --nobanner --recursive /env \
        | awk '{ gsub(/,/, "\nso:", $2); print "so:" $2 }' \
        | sort -u \
        | xargs -r apk info --installed \
        | sort -u)" \
    && apk add --virtual rundeps $runDeps \
    && apk del .build-deps

ENV VIRTUAL_ENV /env
ENV PATH /env/bin:$PATH
WORKDIR /opt

EXPOSE 8000
CMD ["./start.sh"]

ADD . /opt
RUN mkdir /opt/static