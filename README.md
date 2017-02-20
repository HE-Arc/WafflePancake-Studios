# WafflePancake-Studios

This [Django](https://www.djangoproject.com/) project is meant to create
an online photo gallery, accessible and updatable by multiple people at once.

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

## Run dev server

Run the `ShinyWaffle/manage.py` with the following command : `python manage.py runserver`.

# Delpoyement with NginX

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
