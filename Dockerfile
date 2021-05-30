FROM tensorflow/tensorflow:1.15.2-gpu-py3
ENV LANG=C.UTF-8
ARG GPT2_MODEL_NAME=124M
ENV GPT2_MODEL_NAME=$GPT2_MODEL_NAME
ARG UPLOAD_FOLDER=upload
ENV UPLOAD_FOLDER=$UPLOAD_FOLDER
RUN pwd

RUN apt-get update
RUN apt-get -y install libpq-dev python-dev #This can go eventually
ADD "https://api.github.com/repos/LockeBirdsey/thenewsoftheday/commits?per_page=1" latest_commit
RUN curl -sLO "https://github.com/LockeBirdsey/thenewsoftheday/archive/refs/heads/master.zip" && unzip master.zip

WORKDIR ./thenewsoftheday-master
RUN pwd
RUN chmod +x entrypoint.sh
RUN pip3 install -r requirements.txt
RUN pip3 install -r gpt2requirements.txt
RUN pip3 install gunicorn

#WORKDIR ./src/gpt2-server
#Get the web server running
ENTRYPOINT ["~/thenewsoftheday-master/entrypoint.sh"]
CMD ['']
#CMD ["gunicorn"  , "--bind", "0.0.0.0:8000", "server:app"]