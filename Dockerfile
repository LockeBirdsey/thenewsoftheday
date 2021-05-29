FROM tensorflow/tensorflow:1.15.2-gpu-py3
ENV LANG=C.UTF-8
RUN apt-get -y install git
RUN git clone
WORKDIR /gpt-2-simple
RUN pip3 install -r requirements.txt
