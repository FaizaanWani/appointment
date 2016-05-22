#!/bin/bash
apt-get install build-essential
apt-get install libsqlite3-dev
apt-get install sqlite3
apt-get install bzip2 libbz2-dev
apt-get install python3.4
apt-get install python3-pip
pip3 install Django==1.8.5
pip3 install django-datetime-widget
python3 manage.py runserver 0.0.0.0:80
