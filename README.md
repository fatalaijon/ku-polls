# Web Polls for Kasetsart University

A polls application for [Individual Software Process](https://cpske.github.io/ISP) course at [Kasetsart University](https://ku.ac.th).

This application is for conducting a poll or survey, written in Python using Django. It is based on the [Django Tutorial project][django-tutorial], 
and adds additional functionality.

## Requirements

Requires Python 3.6 or newer and the packages listed in [requirements.txt](requirements.txt).

Install required packages using `pip install -r requirements.txt` or create a virtualenv.

## Running the Application

1. Edit `.env` in the project root directory and set these variables:
   ```
   SECRET_KEY=a-secret-key
   DEBUG=False   (set to True for development)
   # comma separated list of allowed hosts. May use suffixes and * as wildcard
   ALLOWED_HOSTS=
   ```
   for unit tests and using the app only on the local machine, try `ALLOWED_HOSTS=localhost, testserver`
   - any string w/o space can be used as secret key. For a truly random secret in the standard format use:   
   ```python
   from django.core.management.utils import get_random_secret_key
   print( get_random_secret_key() )
   ```
2. Start the server. Optionally, you can specify a port to listen on as extra command line argument.
   ```
   python manage.py runserver
   ```
3. Visit http://localhost:8000

TODO: Document migrations and data import (once we have some polls to import!).

## Demo User Accounts

The application has 2 demo user accounts:

* `demo` password `kansadaeng`
* `harry` password `Hackme`

## Project Documents

All project-related documents are in the [Project Wiki](../../wiki/Home)

[Vision Statement](../../wiki/Vision%20Statement)

[Requirements](../../wiki/Vision%20Statements)

Iterations
* [Iteration 1 Plan](../../wiki/Iteration%201%20Plan) and [Task Board](../../projects/1)
* [Iteration 2 Plan](../../wiki/Iteration%202%20Plan)
* [Iteration 3 Plan](../../wiki/Iteration%203%20Plan)


[django-tutorial]: https://docs.djangoproject.com/en/3.1/intro/tutorial01/

