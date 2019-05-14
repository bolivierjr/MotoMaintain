FROM mhart/alpine-node

WORKDIR /code

# RUN psql -U docker -c "DROP DATABASE IF EXISTS flask_api" \
#     && psql -U docker -c "CREATE DATABASE flask_api"

RUN apk update \
    && apk add --no-cache \
    python3 \
    python3-dev \
    build-base \
    make \
    postgresql-contrib \
    postgresql \
    postgresql-dev \
    musl-dev \
    openssl \
    bash \
    wget

RUN wget -P /tmp https://bootstrap.pypa.io/get-pip.py \
    && python3 /tmp/get-pip.py \
    && rm /tmp/get-pip.py

COPY backend/requirements.txt .
RUN pip3 install -r requirements.txt

# COPY frontend/package.json frontend/
# RUN cd frontend && npm install

# COPY . .

# RUN cd frontend && npm build

WORKDIR /code/backend
CMD flask run --host=0.0.0.0