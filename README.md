# miniLearn: A Description

miniLearn is video sharing app for allowing snipets of videos for programming and coding. I believe that fun and laughter are the best way to learn, here we can pass the knowledge of software engineering, by funny content.

## Setup Steps

1. [Fork and clone](https://git.generalassemb.ly/ga-wdi-boston/meta/wiki/ForkAndClone) this repository.
2. Run `pipenv shell` to enter virtual environment.
3. Run `pipenv install` to install dependencies.
4. Create a psql database for your project
- Edit settings.sql
- Type psql to get into interactive shell.
- Run CREATE DATABASE "project_db_name"; where project_db_name is the name you want for your database.
5. Open the repository in Atom with `atom .`
6. Add the database name to the `.env` file using the key `DB_NAME_DEV`.
7. Replace all instances of `django_auth_template` with your application name. **This includes the folder included in this repository.**
8. Generate a secret key using [this tool](https://djecrety.ir) and add it to the `.env` file using the key `SECRET`.

## Commands

Commands are run with the syntax `python3 manage.py <command>`:

| command | action |
|---------|--------|
| `runserver`  |  Run the server |
| `makemigrations`  | Generate migration files based on changes to models  |
| `migrate`  | Run migration files to migrate changes to db  |
| `startapp`  | Create a new app  |
## Important Links

- [GitHub API Repo](https://github.com/danny-pantoja/miniLearn-django)
- [Deployed API](https://mini-learn-django.herokuapp.com/)
- [GitHub Repo](https://github.com/danny-pantoja/miniLearn-react)
- [Deployed Client](https://danny-pantoja.github.io/miniLearn-react)

## Planning Story

- Create the API models and routes.
- Test API connections.
- Build basic front end components.
- Test front end to back end connection.
- Create styling for front end components.
- Test, debug, troubleshoot and debug.
- Reach for stretch goals

### User Stories

- As an unregistered user, I would like to sign up with email and password.
- As a registered user, I would like to sign in with email and password.
- As a signed in user, I would like to change password.
- As a signed in user, I would like to sign out.
- As an unregistered user, I would like to see all of the content.
- As a signed in user, I would like to add some content


### Reach Goal(s)
- As a signed in user, I would like to add memes and videos
- Create a feature that allows for content like
- Create a feature that allows user to message each other

### Technologies Used

- Python
- Django
- PostgreSQL
- cURL
- Psycopg2
- Gunicorn
- WhiteNoise
- Heroku

### Catalog of Routes

| Verb   | URI Pattern            | Controller#Action      |
|--------|------------------------|------------------------|
| POST   | `/sign-up`             | `users#signup`         |
| POST   | `/sign-in`             | `users#signin`         |
| DELETE | `/sign-out`            | `users#signout`        |
| PATCH  | `/change-password`     | `users#changepw`       |
| GET    | `/videos`              | `videos#index`         |
| GET    | `/videos/:id`          | `videos#show`          |
| POST   | `/videos`              | `videos#create`        |
| PATCH  | `/videos/:id`          | `videos#update`        |
| DELETE | `/videos/:id`          | `videos#delete`        |



### ERD
![ERD_for_miniLearn](https://i.imgur.com/BUdwuSM.png))
