# land-avilability-voa
VOA service for Land Availability Tool

# Continuous integration status

[![Travis-CI Status](https://secure.travis-ci.org/alphagov/land-availability-voa.png?branch=master)](http://travis-ci.org/#!/alphagov/land-availability-voa)

# PostgreSQL Setup

Make sure you have **PostgreSQL** (tested with 9.6) installed.

It's strongly suggested to use Postgres.app on OSX and to install all the other
tools and dependencies using **brew**.

## Create DB

```
createdb landavailability-voa
```

# Project Configuration

Make sure you have this environment variable set:

```
DATABASE_URL=postgres://USERNAME:PASSWORD@HOST:PORT/DBNAME
```

example:

```
DATABASE_URL=postgres://andreagrandi@localhost:5432/landavailability-voa
```

If you are using a Python virtual environment, you can save these values in
$venv_folder/bin/postactivate script:

```
export DATABASE_URL=postgres://andreagrandi@localhost:5432/landavailability-voa
```

# Python

The project is being developed and tested with **Python >= 3.5.x**
