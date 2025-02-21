# cursd-blog
cursed-blog


How to open for testing:
1.Open virtual environment, only necessary once per session
$ source venv/bin/activate

NO LONGER NECESSARY 
after the addition of .flaskenv, this step isn't required.
2. export flask
$ export FLASK_APP=cursd-blog.py

3. run flask
$ flask run


Notes:
Forms run on Flask-WTF(see chapter 3 of miguel grinberg's microblog tutorial)


Info:
Flask
Python 
Flask-SQLAlchemy (Flask friendly for the SQLAlchemy package Object Relational Mapper)




Process for adding new features so far:

1. create class in /app to describe the information/behavior ex. forms.py
2-Describe how content is arranged in app/templates/ ex. login.html
3-add route configuration in routes.py
4-add content to base.html

