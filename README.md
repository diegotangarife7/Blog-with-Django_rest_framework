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

##### Lists all users
you can list all users `/users/list-all/` but remember that you must send the token in the headers:
- Authorization Token 68559867f990bd329698316d81946414a30c0dea 

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





##### Create a Category
you can create a category as follows `/posts/categories/` but you have to be administrator users

```
[POST]   http://127.0.0.1:8000/posts/categories/
```

##### List a category
you can list a category using the `id` 
```
[GET]   http://127.0.0.1:8000/posts/categories/<id>/
```

##### Delete a category
you can delete a category using the `id`
```
[DELETE]   http://127.0.0.1:8000/posts/category/delete/<id>/
```

##### Search category by keyword
you can search a category by keyword `/posts/categories/search/?kword=`
```
[GET]   http://127.0.0.1:8000/posts/categories/search/?kword="here your search"
```

##### Update a category
You can update a category using its `id`
```
[PUT]   http://127.0.0.1:8000/posts/category/update/<id>/
```

##### List all categories
you can list all the categories even those that have their status in false, that is to say the eliminated ones  `/posts/categories/`
```
[GET]   http://127.0.0.1:8000/posts/categories/
```





##### Create a post
so you can create a post `/posts/create/` don't forget the token
```
[POST]  http://127.0.0.1:8000/posts/create/
```

##### Post detail
you can see the detail of a post using its slug based on the title
```
[GET]   http://127.0.0.1:8000/posts/detail/<slug>
```

##### Update a post
you can update a post using its `id`
```
[PUT]  http://127.0.0.1:8000/posts/update/<id>/
```

##### Deleta a post
you can delete a post using its `id`
```
[DELETE]  http://127.0.0.1:8000/posts/delete/<id>/
```

##### Search post
you can search a post by keyword and/or author
with the parameters `?kword` and/or `?author`
```
[GET]  http://127.0.0.1:8000/posts/search/?kword="your word here"&author="author name here"
```

##### See my post
you can see all your posts `posts/see/all/` and if you want you can filter by published `?published=true` or `?un_published=false`
```
[GET]  http://127.0.0.1:8000/posts/see/all/
```

##### All published posts 
you can see all the published posts of all users `/posts/list/all/` and pagination every 10 results `/posts/list/all/?page=2`
```
[GET]  http://127.0.0.1:8000/posts/list/all/
```





##### Comment on a post
you can comment on posts using the `id` of the post
```
[POST]  http://127.0.0.1:8000/posts/comment/create/<id>/
```

##### Delete comment
you can delete the comment using its `id`
```
[DELETE]  http://127.0.0.1:8000/posts/comment/delete/<id>/
```




##### Comment a comment
You can comment on a comment using its `id`
```
[POST]  http://127.0.0.1:8000/posts/comment/on/the/comment/create/<id>/
```

##### Delete comment a comment
you can remove the comment from the comment using its `id`
```
[DELETE]  http://127.0.0.1:8000/posts/comment/on/the/comment/delete/<id>/
```




##### Like
you can like a post using its `id`
```
[POST]  http://127.0.0.1:8000/posts/like/<id>/
```

##### Delete like
you can remove the like with his `id`
```
[DELETE]  http://127.0.0.1:8000/posts/like/delete/<id>/
```



##### DisLike
you can dislike a post using its `id`
```
[POST]   http://127.0.0.1:8000/posts/dislike/<id>/
```

##### Delete dislike
you can delete the dislike using his `id`
```
[DELETE]   http://127.0.0.1:8000/posts/dislike/delete/<id>/
```

