FROM python:3.8.1

RUN apt-get update -y
RUN pip install Flask


# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /app/requirements.txt

ADD . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENV PYTHONUNBUFFERED 1
EXPOSE 5000
