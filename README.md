# Fastapi starter

## Getting Started

1. clone the repo & cd into it.
2. Create a virtual environment for installing dependencies:
   <br/><nbsp/>`python3 -m venv project_name_venv`
3. Source the virtual environment:
   <br/><nbsp/>`source project_name_venv/bin/activate`
4. Install the dependencies in the virtual environment:
   <br/><nbsp/>`pip install -r requirements.txt`

## Setting up DB

1. create the .env file in the project root directory and set the values:
   ```shell
    PROJECT_NAME=Gateway

    DATABASE_PORT=
    POSTGRES_PASSWORD=
    POSTGRES_USER=user
    POSTGRES_DB=
    POSTGRES_HOST=
    POSTGRES_HOSTNAME=
    
    ACCESS_TOKEN_EXPIRES_IN=
    REFRESH_TOKEN_EXPIRES_IN=
    SECRET_KEY=
    SECRET_KEY_REFRESH=
   ```

2. Run migrations
   ```shell
   alembic revision --autogenerate -m "..."
   alembic upgrade head
   ```

## Running the Server

```shell
$ uvicorn main:app --reload
```

## View api documentation

- Visit `http://127.0.0.1:8000/docs`
