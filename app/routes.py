from flask import render_template
from app import app
from app.forms import LoginForm
from flask import render_template, flash, redirect

"""
each app route describes what the server will send in response to a request including
the path specified in the arguements.
"""

# @appvar.route are decorators, which associate urls '/' and '/index' with the index() function
@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Randell'}
    posts = [
        {
            'author' : {'username':'Johnny Smells'},
            'body': 'Aint no smells in here'
        },
        {
            'author': {'username':'SusAnne'},
            'body': 'Whoops, dropped my hell pith'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)



"""
Before /templates/ was created, this is what was on this page.
    return '''
<html>
    <head>
        <title>Home Page - Microblog</title>
    </head>
    <body>
        <h1> Howdy, ''' + user['username'] + '''!</h1>
    </body>
</html>'''
"""


'''
The following is what allows the login to accept information
'''
#from flask import render_template, flash, redirect
@app.route('/login', methods=['GET', 'POST']) #set methods to accept get and post instead of just get
def login():
    form = LoginForm()

#this if statement is what stops the browser from submitting when it initially requests the web page
#if form.validate_on_submit returns true, two functions pass flash and redirect.
    if form.validate_on_submit():
        #flash function is a way to show users a message, this is temporary
        #flashed messages do not magically appear, see base.html for how to layout flashed messages
        flash('Oh? {} you are trying to login, remember_me={}'.format(form.username.data, form.remember_me.data))
        #redirect automatically instructs the client to navigate back to the specified page
        return redirect('/index')
    return render_template('login.html', title='Sign In', form=form)

'''
-------------------
This is the older login function.
-------------------
#from app.forms import LoginForm
@app.route('/login')
def login():

    form = LoginForm()
    return render_template('login.html', title='Sign In', form=form)
'''    
