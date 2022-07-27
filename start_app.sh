#!/bin/bash

source venv/bin/activate
PYTHONDONTWRITEBYTECODE=1 python -m app
# PYTHONDONTWRITEBYTECODE=1 python -m flask run