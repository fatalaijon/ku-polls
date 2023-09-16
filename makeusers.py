"""
Add users to the KU Polls User table.
Edit the code to create users you want.
Then run "manage.py shell" to create
a django shell.  
Import this file in the django shell.
After that you can invoke functions (if necessary)
from the shell.
"""

from django.contrib.auth.models import User

def createuser(username: str, password: str, firstname: str, lastname=""):
    """Add one user to the User table. username is the login name."""
    try:
        u = User.objects.get(username=username)
        print(f"Username {u.username} with id {u.id} already exists in User table.")
        return 0
    except User.DoesNotExist:
        pass
    u = User.objects.create_user(username=username, password=password, email=f"{username}@localhost")
    u.first_name = firstname
    u.last_name = lastname
    u.save()
    return u.id


def make_interactive():
    """Create a user interactively."""    
    username = input("username? ")
    password = input("password? ")
    name = input("Real name (First or First Last)? ")
    name = name.strip().split(" ")
    firstname = name[0]
    lastname = name[1] if len(name) > 1 else ""
    id = createuser(username, password, firstname, lastname)
    if id > 0:
        print(username, "created and saved")
    else:
        print("failed to create username", username)


def make_demo_users(start: int, count: int):
    """Create users named demo{N} with N = start, start+1, ...

    Arguments:
    start - starting demo user number (integer) 
    count - how many demo users to create
    """    
    for n in range(start, start+count):
        username = f"demo{n}"
        firstname = f"Demo-{n}"
        password = f"Hackme{n}"
        id = createuser(username, password, firstname)
        if id > 0:
            print("Created user", username, "with password", password)
        else:
            print("username", username, "already exists.")


def make_batch():
    createuser("demo", "demonstrate", "Demo", "User")
    createuser("harry", "Hackme", "Harry", "Hacker")
    createuser("sally", "Hackme2", "Sally", "Cracker")
    print("Users")
    for u in User.objects.all():
        print(f"{u.username} {u.first_name} id {u.id}")


# Any code not in a function will be executed when you import this file.
make_demo_users(1, 4)
