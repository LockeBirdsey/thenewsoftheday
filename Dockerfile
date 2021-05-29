FROM tensorflow/tensorflow:1.15.2-gpu-py3
ENV LANG=C.UTF-8
ARG GPT2_MODEL_NAME=124M
ENV GPT2_MODEL_NAME=$GPT2_MODEL_NAME
RUN apt-get update
RUN apt-get -y install git
RUN apt-get -y install libpq-dev python-dev
RUN git clone https://github.com/LockeBirdsey/thenewsoftheday.git
WORKDIR ./thenewsoftheday
RUN pip3 install -r requirements.txt
RUN pip3 install -r gpt2requirements.txt
RUN pip3 install gunicorn

#RUN python startup.py #TODO enable after web-server is okay
WORKDIR ./src/gpt2-server
#Get the web server running
CMD ["pwd"]
CMD ["gunicorn"  , "--bind", "0.0.0.0:8000", "server:app"]