# Start virtualenv
`source ./env/bin/activate`

# Start server
`python manage.py runserver`

http://localhost:8000/

# Migration
`python manage.py migrate`

# Create new app
`python manage.py startapp <app-name>`

# Make new migration
`python manage.py makemigrations polls`

# Create superuser to access /admin/
`python manage.py createsuperuser`