FROM python:3.7-alpine
MAINTAINER Dan the man

# don't allow Python to buffer the outputs
ENV PYTHONUNBUFFERED 1

# install dependencies via requirements.txt
COPY ./requirements.txt /requirements.txt
# using no-cache here to minimize amount of extra dependencies
# that will be installed
RUN apk add --update --no-cache postgresql-client
# install temporary packages that will be removed after requirements
# are met and needed packages are installed
# virtual flag setups up an alias for this installation (temporary build dependencies)
RUN apk add --update --no-cache --virtual .tmp-build-deps \
    gcc libc-dev linux-headers postgresql-dev
RUN pip install -r /requirements.txt
# now run command to delete temp deps
RUN apk del .tmp-build-deps

# creates empty directory and sets it as default
RUN mkdir /app
WORKDIR /app
# copy local app directory to image app directory
COPY ./app /app

# creates a user to own and run the applicaton,
# prevents root user from being used
RUN adduser -D user
USER user
