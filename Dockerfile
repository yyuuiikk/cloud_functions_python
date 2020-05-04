FROM python:3.7-slim
WORKDIR /src
COPY . /src

RUN apt-get update
RUN apt-get -y install locales && \
    localedef -f UTF-8 -i ja_JP ja_JP.UTF-8
ENV LANG ja_JP.UTF-8
ENV LANGUAGE ja_JP:ja
ENV LC_ALL ja_JP.UTF-8
ENV TZ JST-9
ENV TERM xterm

RUN apt-get install -y vim less curl
RUN pip install --upgrade pip
RUN pip install --upgrade setuptools
RUN pip install requests
RUN pip install pyyaml
RUN pip install flask
# google cloud
RUN pip install google-cloud
RUN pip install functions-framework
