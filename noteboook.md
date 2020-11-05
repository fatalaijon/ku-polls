## Querying a Database

Avoid getting data you don't need from a database.
It can be very inefficient.

Inefficient. This code gets **all** questions from the database
when it only wants one.
```python
def get_question(self, id):
    """Get question with the requested id number. """
    questions = Question.objects.all()
    for q in questions:
        if q.id == id:
            return q
```

Efficient: Let Django construct a query for just the question you want.
```python
def get_question(self, question_id):
    """Get question with the requested id number. """
    question = Question.objects.get(id=question_id)
    return question
```

Inefficient. Get questions already published.
```python
from django.utils import timezone

def get_published_questions(self):
    """Get all questions published on or before the current date/time."""
    now = timezone.now
    questions = [q for q in Question.objects.all() where q.pub_date <= now]
    return questions
```

Efficient: Use Django Query language to make a question for just the questions you want.
```python
from django.utils import timezone

def get_published_questions(self):
    """Get all questions published on or before the current date/time."""
    now = timezone.now
    questions = Question.objects.filter(pub_date__lte=now)
    return questions
```

This uses Django's special syntax for queries.
You cannot write:
```
Question.objects.filter(pub_date<=now)
```
Instead use `__lte` to mean "less than or equals" as a query condition:
```
Question.objects.filter(pub_date__lte=now)
```

You can build queries using references.  Each `Choice` has a `question` attribute that refers to the question the choice is associated with (foreign key).
You can refer to this in a query as (`question`).

Get all choices for question number 2.
```python
    # write question_id to refer to question.id
    choices = Choice.objects.filter(question_id=2)
```

## What do filter and all Return?

`filter()` and `all()` return a `QuerySet`.  It's not a list.

## QuerySets are Lazy

The elements of a QuerySet are not actually retreived from the database and put into objects until something forces it to happen.

```
# QuerySet but no objects created
queryset = Question.objects.filter(question_text__contains="favorite")
# Chain QuerySet, but still no objects created
queryset = queryset.filter(pub_date__lte=now)

# Finally, retrieve the first 5 results and create objects
result = queryset[0:5]
# Result is still a QuerySet (not a list)
```

## See

[Making Queries](https://docs.djangoproject.com/en/3.1/topics/db/queries/) in the Django Documentation.

## Sorting and Reverse Sorting List of Items in a Template

In the template for poll detail, I want the list of choices sorted alphabetically.
There are 2 ways to do this:

1. In the `Choice` model class, add an inner Meta class:
   ```python
   class Choice(models.Model):
       """An answer to a polls question."""
       choice_text = models.CharField(max_length=80)

       class Meta:
           ordering = ['choice_text']
   ```
2. In the `detail.html` template, use a filter named **dictsort**:
   ```html
   {% for choice in question.choice_set.all|dictsort:"choice_text" %}
   ```
      
In the template for voting results, I want to sort the choices by (decreasing) number of votes, so the most voted choice comes first.  The best solution seems to be to use a filter in the `results.html` template. The filter is **dictsortreversed**.
   ```html
   {% for choice in question.choice_set.all|dictsortreversed:"votes" %}
   ```

## Submitting a Form

In HTML, the syntax for a form is:
```html
<form action="https://where-to-send-form/path" method="POST">
<label for="namefield">Your Name:</label> 
<input id="namefield" type="text" width=40/>
<br/>
<input type="submit">Submit</input>
</form>
```

There are many kinds of form elements, described in the
[W3Schools Forms Tutorial](https://www.w3schools.com/html/html_forms.asp).

In Django, you submit a form to a URL associated with a view.

To avoid mistakes in the URL, a form (defined in a page template)
can use Django's template language to specify the URL:
```html
<form action="{% url polls:register %}" method="POST">
  ...
</form>
```

Then in your `polls/urls.py` file you would have a **named view** for this:
```python
app_name = polls

urlpatterns = [
   path("register/", views.register, name='register'),
   ...
```

## Sending and Reading Form Data

Each form `input` element has a **name** attribute.
The *value* of the input field is assigned to attribute.
For example:
```
<form action=... method='POST'>
Name: <input type='text' name='username'/> 
<br>
Sex:
<br/>
<input type="radio" name="gender" value="male"> Male 
<input type="radio" name="gender" value="female"> Female 
<input type="radio" name="gender" value="undecided"> Not sure 
<br/>
Birthday: <input type='date' name='birthday'/>
<br/>
<input type="submit" value='Submit'/>
</form>
```

* when this form is submitted, the HTTP body will contain the POST data as key-value pairs.
* Django **parses** the post request and adds it to the HttpRequest object as a dict named POST.
```python
request.POST['username'] = value of the name field
request.POST['gender'] = value of the selected "gender" radio button 
request.POST['birthday'] = value of the birthday field
```
* Your view can get this data, since the HttpRequest is a parameter:
```python
def register(request):
    """Register a new user"""
    if request.method == 'POST':
       name = request.POST['username']
       gender = request.POST['gender']
       bday = request.POST['birthday']
       person = Person(name, gender, bday)
       person.save()
       return HttpResponseRedirect( '/polls/' )
    else:
       # if a GET request then send user the form
```
* This code is to demonstrate the underlying mechanism. A better way to handle forms is to create a subclass of `django.forms.Form`, which automates much of the work of creating a form, validating input, and parsing the form data.
* See [Working with Forms](https://docs.djangoproject.com/en/3.1/topics/forms/) in the Django Docs.

### Cross-Site Request Forging Protection

To prevent cross-site request forging (CSRF) always include `csrf_token` in a form:
```html
<form action=...>
{% csrf_token %}

</form>
```
If you omit `csrf_token`, Django will reject the POST request.


## Getting a URL using a URL name

In `urls.py` you can assign **names** to URL paths.
You can use these names in place of the actual URL string.  
This makes it easier to modify your application and avoids typing errors.

```python
# urls.py
app_name = polls

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:question_id>", views.detail, name="detail"),
    ...
    ]
```

1. Get the URL for a name **in a template**:
   ```
   <a href="{% url polls:index %}"> Back to index page</a>

   <a href="{% url polls:detail 1 %}">View Poll #1</a>
   ```

2. Get the URL for a name **in Python code**. Usually done in a `views` file to redirect the browser to a new URL.
   ```python
   from django.shortcuts import reverse
   from django.http import HttpResponseRedirect

   def vote(request, question_id):

       if question does not exist:
           index_url = reverse('polls:index')
           return HttpResponseRedirect(index_url)

       # if voting succeeds: redirect to results page
       results_url = reverse('polls:results',args=(question_id,))
       return HttpResponseRedirect(results_url)
   ```


