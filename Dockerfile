FROM tensorflow/tensorflow:1.15.2-gpu-py3
ENV LANG=C.UTF-8
ARG GPT2_MODEL_NAME=124M
ENV GPT2_MODEL_NAME=$GPT2_MODEL_NAME
ARG UPLOAD_FOLDER=upload
ENV UPLOAD_FOLE=$UPLOAD_FOLDER

RUN apt-get update
RUN apt-get -y install libpq-dev python-dev
ADD "https://api.github.com/repos/LockeBirdsey/thenewsoftheday/commits?per_page=1" latest_commit
RUN curl -sLO "https://github.com/LockeBirdsey/thenewsoftheday/archive/refs/heads/master.zip" && unzip master.zip


WORKDIR ./thenewsoftheday-master
RUN pip3 install -r requirements.txt
RUN pip3 install -r gpt2requirements.txt
RUN pip3 install gunicorn

#WORKDIR ./src/gpt2-server
#Get the web server running
ENTRYPOINT ["entrypoint.sh"]
#CMD ["gunicorn"  , "--bind", "0.0.0.0:8000", "server:app"]
CMD ['']