# WafflePancake-Studios

This [Django](https://www.djangoproject.com/) project is meant to create
an online photo gallery, accessible and updatable by multiple people at once.

# Presentation slides

Our presentation slides can be viewed [here](https://docs.google.com/presentation/d/1IsiYmbJbYmKJiYRWW7-MgvjkK-OR6qQI1rg7Hsb6ftU/edit?usp=sharing)

# Developpment environment setup

## Windows

1. Using [Anaconda](https://www.continuum.io/downloads), create a virtual
   environment with command `conda create --name myenv python=3.6.0 django`.
2. You can then activate this virtual environment using `activate myenv`
   command.
3. Run `pip install -r requirements.txt` to install depedencies in your virtual
   environment.
4. Copy the _ShinyWaffle/.env.example_ into a _.env_ file and modify
   the variables accordingly to your database configuration.

You're now ready to develop features for this projet!

## Dependencies

If you had to install a new python package to implement a new feature, update
the depedencies by running command `pip freeze > requirements.txt` to update
the requirements file.

## Environment setup

Before running the server, copy and paste the _env.example_ file to a _.env_
file. Then, run the following command to tell Django to load the _.env_ file.

Add the following line to the _.env_ file and adapt it with your database settings:

```
DATABASE_URL="postgres://<pg_user_name>:<pg_user_password>@127.0.0.1:<pg_port>/<pg_database_name>"
```

For windows: `set DJANGO_READ_DOT_ENV_FILE=1`.
For Linux: `export DJANGO_READ_DOT_ENV_FILE=1`.

__This variable is set for the active console. You will have to reset it if you
want to run the server from an other terminal.__

If you want to avoid launhing this command every time you open a new terminal,
you can put the preceding command into the _postactivate_ of your virtual
environement's bin directory (*$VIRTUAL_ENV/bin/postactivate*).
It might be _postactivate.bat_ if you're using Windows.

If you are using anaconda and wish to set this variable at environment
activation automatically, have a look at this link:
[https://conda.io/docs/using/envs.html#saved-environment-variables](https://conda.io/docs/using/envs.html#saved-environment-variables)

## Run dev server

Run the `python manage.py runserver` to run the server.

# Deployment with NginX

For further deployment on production server, see [this link](http://uwsgi-docs.readthedocs.io/en/latest/tutorials/Django_and_nginx.html).

# Project's must-have

The project will implement the following features:
* Upload / download pictures on a board, a gallery.
* Board is sharable with other users.
* Authentification is necessary for sharing photos.

# Further features

The project might implement following features :
* Responsive design.
* Appreciations and comments on photos and/or galleries.
* Tag users on photos.
* Modify photos on the fly (crop, resize, draw on it, filters, advanced edge detection, face recognition, whatever...).
* Infinite left - right - up - down scrolling on a board, sharing photos as on an infinite table.
* Add funny widgets to the infinite-scrollable-area.
* Entire universe accurate physical (on all scales) simulation, to find the answer to the universe, the life, and everything.
