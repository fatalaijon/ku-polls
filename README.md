# Web Polls for Kasetsart University

A polls application for [Individual Software Process](https://cpske.github.io/ISP) course at [Kasetsart University](https://ku.ac.th).

This application is for conducting a poll or survey, written in Python using Django. It is based on the [Django Tutorial project][django-tutorial], 
and adds additional functionality.

## ISP STUDENTS: DON'T COPY THIS TEXT

This file contains an example but you must write 100% of your own README.

You can copy the *structure* but none of the text.

## Requirements

Requires Python 3.6 or newer, pip, and virtualenv. 

## Configure the Application

Download the code to a local directory using either `git clone` or a ZIP file provided by Github. Do the following once in the directory where you placed the project files.

`python3` refers to the Python 3 command. It may be `python` on some hosts.

1. Update your Python `pip` to the current version.
   ```
   python3 -m pip install --upgrade pip
   ```

2. Install virtualenv
   ```
   python3 -m pip install virtualenv
   ```

3. Create a virtualenv subdirectory named `env` and activate it. 
   ```
   cmd> virtualenv env
   # Activate the virtualenv on Linux and MacOS
   cmd> source env/bin/activate
   # On MS Windows use
   cmd> env\Scripts\activate
   (env)cmd>
   ```
   Notice that the prompt changes when virtualenv is active.

4. Install required packages inside the virtualenv. This will download the packages using the Internet, so a network connection is required.  Will down approximately 60MB of Python packages and install them in the `env/lib` directory, not in your system's Python library.
   ```
   # install required packages
   (env)cmd> python3 -m pip install -r requirements.txt
   ```

5. In the project root directory, copy `sample.env` to `.env` (file name begins with "."). Then edit `.env`  and set values of these variables as desired.  
   ```
   SECRET_KEY=any-random-string-will-work
   # set DEBUG to True for testing and local development
   DEBUG=False   
   # comma separated list of allowed hosts. May use suffixes and * as wildcard
   ALLOWED_HOSTS=localhost, testserver
   TIME_ZONE=Asia/Bangkok
   ```
   - Leave ALLOWED\_HOSTS set to nothing or `*` to allow all hosts.
   - For a truly random secret in the standard format run this code at a Python command prompt:   
   ```python
   from django.core.management.utils import get_random_secret_key
   print( get_random_secret_key() )
   ```

6. Run migrations to initialize the database:
   ```
   python3 manage.py migrate
   ```

7. Import data for some initial polls and users:
   ```
   python3 manage.py loaddata polls users
   ```

8. Exit the virtualenv (or stay in virtualenv and skip down to [running the application](#running-the-application)):
   ```
   (env)cmd> deactivate   
   ```

## Running the Application

1. Start the server in the virtualenv. 
   ```
   # activate the virtualenv on Linux and MacOS
   source env/bin/activate
   # on MS Windows, use:
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
   If you get a message that the port is unavailable, then run the server on a different port (1024 thru 65535) using
   ```
   python3 manage.py runserver 12345
   ```

3. In a web browser, navigate to [http://localhost:8000](http://localhost:8000)

4. To stop the server, press CTRL-C in the terminal window. Then exit the virtualenv by closing the window or typing:
   ```
   deactivate
   ```

## Demo User Accounts

Sample polls and users data included with the application. It has 4 demo user accounts:

* `demo1` password `Hackme1`
* `demo2` password `Hackme2`
* `demo3` password `Hackme3`
* `demo4` password `Hackme4`

You can create more user accounts using the script `makeusers.py`. See instructions in the script.

## Project Documents

All project-related documents are in the [Project Wiki](../../wiki/Home)

[Vision Statement](../../wiki/Vision%20Statement)

[Requirements](../../wiki/Vision%20Statements)

Iterations

* [Iteration 1 Plan](../../wiki/Iteration%201%20Plan) and [Task Board](../../projects/1)
* [Iteration 2 Plan](../../wiki/Iteration%202%20Plan)
* [Iteration 3 Plan](../../wiki/Iteration%203%20Plan)


[django-tutorial]: https://docs.djangoproject.com/en/3.1/intro/tutorial01/

