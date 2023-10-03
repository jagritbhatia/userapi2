# userapi2
[![Run in Postman](https://run.pstmn.io/button.svg)](https://app.getpostman.com/run-collection/27790272-a89f93da-dcdb-45b6-80f5-199bf0541c93?action=collection%2Ffork&source=rip_markdown&collection-url=entityId%3D27790272-a89f93da-dcdb-45b6-80f5-199bf0541c93%26entityType%3Dcollection%26workspaceId%3D7383bdf0-a237-44e3-af2d-d8f4e3ff45bc)
# Getting started
First clone the repository from Github and switch to the new directory:

$ git clone git@github.com/USERNAME/{{ project_name }}.git

$ cd {{ project_name }}

Activate the virtualenv for your project.

Install project dependencies:

$ pip install -r requirements/local.txt
Then simply apply the migrations:

$ python manage.py migrate
You can now run the development server:

$ python manage.py runserver

#Run apis

http://127.0.0.1:8000/users - Returns a list of all users.

http://127.0.0.1:8000/users/1 - Returns the user with the  ID 1.

http://127.0.0.1:8000/users/create/- Creates a new user with the specified data.

http://127.0.0.1:8000/users/delete/9- Deletes the user with the  ID 9 .
