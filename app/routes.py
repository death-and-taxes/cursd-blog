from flask import render_template
from app import app

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