#!/bin/bash

sudo nginx
export PATH="$HOME/.local/bin:$PATH"
python manage.py migrate
gunicorn -w 2 hub.wsgi
