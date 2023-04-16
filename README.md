# Django_Blog_Binks

## Steps for running in local

```SHELL
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser # Follow the steps after this
python manage.py runserver # starts the server on localhost:8000
```

## Features completed
1. Login
2. List all posts -> authenticated
3. Delete post -> authenticated
4. Edit Post -> authenticated
5. Comment on a post -> authenticated
6. Upvote/like a post -> authenticated
7. Search for a post -> authenticated

## Features not completed due to delay still to be done
1. Replies to a query

## Basic info

All the api's can be seen and can be accessed through the UI itself.
DRF gives us a setup to do the same similar to swagger.

Post json for new user example
```JSON
{
    "username": "kbiyani",
    "password": "KeshavB12345@",
    "email": "dummy@gmail,com"
}
```
