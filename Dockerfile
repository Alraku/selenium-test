FROM jenkins/jenkins:latest

# Docker install

USER root

RUN apt-get update && apt-get install -y \
       apt-transport-https \
       ca-certificates \
       curl \
       gnupg2 \
       software-properties-common

RUN curl -fsSL https://download.docker.com/linux/debian/gpg | apt-key add -
RUN apt-key fingerprint 0EBFCD88

RUN add-apt-repository \
       "deb [arch=amd64] https://download.docker.com/linux/debian \
       $(lsb_release -cs) \
       stable"

RUN apt-get update && apt-get install -y docker.io

# Python pip and virtual environment install

RUN apt-get -y install python3-pip python3-venv

# For chromium based browsers

RUN apt-get -y install libglib2.0-0 libnss3-dev libgdk-pixbuf2.0-dev libgtk-3-dev libxss-dev

USER Jenkins
