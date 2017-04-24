"""
Simple "Hello, World" application using Flask
"""
from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['firstname'],
                       request.form['lastname']):
            return log_the_user_in(request.form['username'])
        else:
            error = 'Invalid username/password'
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    return render_template('WebAppTest.html', error=error)


if __name__ == '__main__':
    app.run()
