# Blog (Backend)

This repository contains the source code of the backend for a blog implemented ***Django Rest Framework.*** It provides an API to manage blog resources such as posts, comments, nested comments, likes, dislikes, and user management.



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
4. activate the environment
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

Once the server is running, you can access the blog API through the URL http://localhost:8000/