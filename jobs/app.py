from flask import render_template, Flask


@route('/')
@route('/jobs')
def jobs():
    render_template('index.html')


app = Flask(__name__)

