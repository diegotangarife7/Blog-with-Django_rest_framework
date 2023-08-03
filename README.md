# Blog (Backend)

This repository contains the source code of the backend for a blog implemented ***Django Rest Framework.*** It provides an API to manage blog resources such as posts, comments, nested comments, likes, dislikes, and user management.

---------------

## Installation

1. Clone this repository to your local machine using the following command: 
    ```bash
    git clone git@github.com:diegotangarife7/Blog-with-Django_rest_framework.git
    ```
2. Navigate to the project directory:
    ```bash
    cd Blog-with-Django_rest_framework
    ```
3. Create and activate a virtual environment (optional but recommended): 
    ```bash
    python -m venv env
    ```
4. Activate the environment:
    ```bash
    windows:  .\env\Scripts\activate 
    linux:    source env/bin/activate
    ```
5. Install the project dependencies by running:
    ```bash
    pip install -r requirements.txt
    ```
6. Apply the database migrations using the command:
    ```bash
    python manage.py migrate
    ```
7. Start the development server by running:
    ```bash
    python manage.py runserver
    ```

Once the server is running, you can access the blog API through the URL `http://localhost:8000/`

---------------

## Endpoints 


##### Create a User

You can register by sending the following `/users/register/`
```
[POST]  http://127.0.0.1:8000/users/register/
```

##### Get token
you can get the auth token `/api-token-auth/`
```
[POST]  http://127.0.0.1:8000/api-token-auth/
```

##### lists all users
you can list all users `/users/list-all/` but remember that you must send the token in the headers:
- (Authorization Token 68559867f990bd329698316d81946414a30c0dea) 

and you must be an administrator user
```
[GET]  http://127.0.0.1:8000/users/list-all/
```

##### Update User
you can update the user by adding the `id` as a parameter `/users/update/<id>/`, remember to send the correct token
```
[PUT]   http://127.0.0.1:8000/users/update/<id>/
```

##### Delete User
you can delete the user by adding the `id` as a parameter `/users/delete/<id>/`, remember to send the correct token
```
[DELETE]   http://127.0.0.1:8000/users/delete/<id>/
```

##### Detail User
You can see the details of the user by adding the `id` as a parameter `/users/detail/<id>/`, remember to send the correct token
```
[GET]   http://127.0.0.1:8000/users/detail/<id>/
```

##### Update User Password
you can update your password by adding the `id` as a parameter `/users/password/update/<id>/`, remember the token
```
[PUT]   http://127.0.0.1:8000/users/password/update/<id>/
```
