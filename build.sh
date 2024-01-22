#!/bin/bash

# Build the project
echo "Building the project..."
python3 -m pip install --upgrade pip
python3 -m pip install pymongo[srv]
python3 -m pip install -r requirements.txt

# # Make migrations
# echo "Making migrations..."
# python3 manage.py makemigrations blog

# # Migrate the database
# echo "Migrating..."
# python3 manage.py migrate

# # Collect static files
# echo "Collecting static files..."
# python3 manage.py collectstatic --noinput