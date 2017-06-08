# land-availability-voa
VOA service for Land Availability Tool

# Continuous integration status

[![Travis-CI Status](https://secure.travis-ci.org/alphagov/land-availability-voa.png?branch=master)](http://travis-ci.org/#!/alphagov/land-availability-voa)
[![codecov](https://codecov.io/gh/alphagov/land-availability-voa/branch/master/graph/badge.svg)](https://codecov.io/gh/alphagov/land-availability-voa)

# PostgreSQL Setup

Make sure you have **PostgreSQL** (tested with 9.6) installed.

It's strongly suggested to use Postgres.app on OSX and to install all the other
tools and dependencies using **brew**.

## Create DB

```
createdb landavailability-voa
```

# Project Configuration

Make sure you have these environment variables set:

```
SECRET_KEY=
DATABASE_URL=postgres://USERNAME:PASSWORD@HOST:PORT/DBNAME
OPBEAT_ORGANIZATION_ID=
OPBEAT_APP_ID=
OPBEAT_SECRET_TOKEN=
OPBEAT_DISABLE_SEND=
```

If you are using a Python virtual environment, you can save these values in
$venv_folder/bin/postactivate script:

```
export SECRET_KEY=abcd1234
export DATABASE_URL=postgres://andreagrandi@localhost:5432/landavailability-voa
export OPBEAT_ORGANIZATION_ID=abcd1234
export OPBEAT_APP_ID=abcd1234
export OPBEAT_SECRET_TOKEN=abcd1234
export OPBEAT_DISABLE_SEND=true
```

# Django setup

    workon landavailability-voa
    cd land-availability-voa/landavailability
    pip install -r ../requirements.txt
    ./manage.py migrate

# Importing data

## User and token

To import VOA data you need a user and token. First open a shell:

    workon landavailability-voa
    cd land-availability-voa/landavailability
    ./manage.py shell

In the shell:

```
# check if there is already an admin user
from django.contrib.auth.models import User
from django.db.models import Q
User.objects.filter(Q(is_superuser=True)).distinct()

# create admin user
user = User.objects.create_user('admin', password='pass', is_staff=True)
user.save()

# check if a token exists for this user
from rest_framework.authtoken.models import Token
Token.objects.filter(Q(user=user))

# create token
token = Token.objects.create(user=user)
print(token.key)
```

This prints the hex token e.g. `8f3f29c458d38a1b073992421965a15e90bd8db9`

## Get VOA data

The data is listed at: TBA

Download:

    cd ~/Downloads
    # wget <TBA>.csv.zip
    unzip uk-englandwales-ndr-2017-summaryvaluations-proposed-epoch-0001-baseline-csv.zip

## Run VOA

    workon landavailability-voa
    cd land-availability-voa/landavailability
    ./manage.py runserver localhost:8002

## Run import script

(while VOA runs in another shell)

    git clone https://github.com/alphagov/land-availability-import
    cd land-availability-import
    python import_voa.py --help
    python import_voa.py --filename ~/Downloads/uk-englandwales-ndr-2017-summaryvaluations-proposed-epoch-0001-baseline-csv.csv --encoding utf-8-sig --apiurl http://localhost:8002/api/voa/ --apitoken <token>
