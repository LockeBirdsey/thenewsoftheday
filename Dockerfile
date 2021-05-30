#FROM python:3.8.10-alpine3.13
FROM python:3.6.4-alpine3.7
ENV LANG=C.UTF-8
ARG UPLOAD_FOLDER=upload
ENV UPLOAD_FOLDER=$UPLOAD_FOLDER
RUN \
 apk add --no-cache postgresql-libs && \
 apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev && \
 apk add --no-cache curl && \
 apk --purge del .build-deps

ADD "https://api.github.com/repos/LockeBirdsey/thenewsoftheday/commits?per_page=1" latest_commit

RUN curl -sLO "https://github.com/LockeBirdsey/thenewsoftheday/archive/refs/heads/master.zip" && unzip master.zip

WORKDIR thenewsoftheday-master
RUN python3 -m pip install -r requirements.txt --no-cache-dir && \
 pip3 install gunicorn

CMD ["gunicorn"  , "server:app"]