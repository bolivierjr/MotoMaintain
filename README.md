# MotoMaintain

[![Build Status](https://travis-ci.org/bolivierjr/MotoMaintain.svg?branch=master)](https://travis-ci.org/bolivierjr/MotoMaintain)  [![codecov](https://codecov.io/gh/bolivierjr/MotoMaintain/branch/master/graph/badge.svg)](https://codecov.io/gh/bolivierjr/MotoMaintain) [![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)


A web app that you can use to keep track of your vehicle maintenance.

## Installation for development

You will need the newest versions of docker-ce and docker-compose.

```bash
git clone https://github.com/bolivierjr/MotoMaintain.git
cd MotoMaintain
docker-compose -f docker-compose.dev.yml up
```

## Rebuild the containers
```bash
docker-compose -f docker-compose.dev.yml up --build
```

## Test the app and view the test report
```bash
make test
make test_report
```

## Use the flake8 linter
```bash
make lint
```

## Usage
Visit `http://localhost:8080`