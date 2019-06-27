FROM python:3.7-alpine
MAINTAINER Dan the man

# don't allow Python to buffer the outputs
ENV PYTHONUNBUFFERED 1

# install dependencies via requirements.txt
COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

# creates empty directory and sets it as default
RUN mkdir /app
WORKDIR /app
# copy local app directory to image app directory
COPY ./app /app

# creates a user to run the account from
# prevents root user from being used
RUN adduser -D user
USER user
