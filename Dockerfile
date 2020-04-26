# The first instruction is what image we want to base our container on
# We Use an official Python runtime as a parent image
FROM python:3.7

# The enviroment variable ensures that the python output is set straight
# to the terminal with out buffering it first
ENV PYTHONUNBUFFERED 1
ENV DJANGO_ENV dev


#RUN pip3 install psycopg2~=2.6
# create root directory for our project in the container
# set working directory
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# add requirements (to leverage Docker cache)
ADD requirements.txt /usr/src/app/requirements.txt

# install requirements
RUN pip install -r requirements.txt


# add app
ADD ./ /usr/src/app

EXPOSE 8000


CMD gunicorn phone_book.wsgi --bind 0.0.0.0:8000 --workers=5