# Web Polls for Kasetsart University
[![Django Tests](https://github.com/fatalaijon/ku-polls/actions/workflows/django.yml/badge.svg)](https://github.com/fatalaijon/ku-polls/actions/workflows/django.yml)

### ISP STUDENTS: You can copy the STRUCTURE of this file but not the actual TEXT

A polls application for [Individual Software Process](https://cpske.github.io/ISP) course at [Kasetsart University](https://ku.ac.th).

This application is for conducting a poll or survey, written in Python using Django. It is based on the [Django Tutorial project][django-tutorial], 
and adds additional functionality.

## Requirements

Requires Python 3.8 or newer.  Required Python packages are listed in [requirements.txt](./requirements.txt). 

## Configure the Application

See [Installation](../../wiki/Installation) in the project wiki.

Brief Instructions:

1. Copy `sample.env` to `.env` and edit the settings.
2. Create a virtualenv: `python -m venv env`
   - Or create it using the virtualenv extension: `virtualenv env`
3. Activate the virtualenv and run `pip install -r requirements.txt`
4. Perform migrations and create a database: `python manage.my migrate`
5. Add polls and users to the database: `python manage.py loaddata polls users`

## Running the Application

1. Start the server in the virtual env. 
   ```
   # Activate the virtual env on Linux and MacOS
   source env/bin/activate
   # Or, on MS Windows:
   env\Scripts\activate

   # run the django server
   python3 manage.py runserver
   ```
   This starts a web server listening on port 8000.

2. You should see this message printed in the terminal window:
   ```
   Starting development server at http://127.0.0.1:8000/
   Quit the server with CONTROL-C.
   ```
   If you get a message that the port is unavailable, then run the server on a different port (1024 thru 65535). For example:
   ```
   python3 manage.py runserver 12345
   ```

3. In a web browser, navigate to <http://localhost:8000>

4. To stop the server, press CTRL-C in the terminal window. Then exit the virtualenv by closing the window or typing:
   ```
   deactivate
   ```

## Demo User Accounts

Sample polls and users data are included. There are 4 demo accounts:

* `demo1` password `Hackme1`
* `demo2` password `Hackme2`
* `demo3` password `Hackme3`
* `demo4` password `Hackme4`

You can create more user accounts using the script `makeusers.py`. See instructions in the script.

## Project Documents

All project-related documents are in the [Project Wiki](../../wiki/Home)

[Vision Statement](../../wiki/Vision%20Statement)

[Requirements](../../wiki/Requirements)

Iterations

* [Iteration 1 Plan](../../wiki/Iteration%201%20Plan) and [Task Board](../../projects/1)
* [Iteration 2 Plan](../../wiki/Iteration%202%20Plan) and [Task Board](../../projects/2)
* [Iteration 3 Plan](../../wiki/Iteration%203%20Plan)


[django-tutorial]: https://docs.djangoproject.com/en/3.1/intro/tutorial01/

