#!/bin/bash

rm db.sqlite3
rm -rf ./thearchiveapi/migrations
python3 manage.py migrate
python3 manage.py makemigrations thearchiveapi
python3 manage.py migrate thearchiveapi
python3 manage.py loaddata fan
python3 manage.py loaddata art
python3 manage.py loaddata tag
