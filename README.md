# Web Polls for Kasetsart University

A polls application for [Individual Software Process](https://cpske.github.io/ISP) course at [Kasetsart University](https://ku.ac.th).

This application is for conducting a poll or survey, written in Python using Django. It is based on the [Django Tutorial project][django-tutorial], 
and adds additional functionality.

## Requirements

Requires Python 3.6 and the Python packages listed in [requirements.txt](requirements.txt).

Install required packages using `pip install -r requirements.txt`.

## Running the Application

1. Edit `.env` in the projet base directory and set these variables:
   ```
   SECRET_KEY=a-secret-key
   DEBUG=False   (set to True for development)
   ```
   - any string w/o space can be used as secret key. For a truly random secret that's in a format used by django use:   
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

## Project Documents

All project-related documents are in the [Project Wiki](../../wiki/Home)

[Vision Statement](../../wiki/Vision%20Statement)

[Requirements](../../wiki/Vision%20Statements)

Iterations
* [Iteration 1 Plan](../../wiki/Iteration%201%20Plan) and [Task Board](../../projects/1)

## Licensing

Contact @fatalaijon to license.

[django-tutorial]: https://docs.djangoproject.com/en/3.1/intro/tutorial01/

