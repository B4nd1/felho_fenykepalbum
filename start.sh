#!/bin/bash

# Deployproba4
python manage.py migrate
gunicorn --bind "0.0.0.0:8080" felho_fenykepalbum.wsgi:application