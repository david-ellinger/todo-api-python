FROM python:3.8

WORKDIR /usr/src/app

# pyenv installer
RUN curl https://pyenv.run | bash
RUN exec $SHELL

RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt

COPY . /usr/src/app

EXPOSE 5000
