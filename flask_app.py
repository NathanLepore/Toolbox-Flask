"""
Put your Flask app code here.
"""
import os
from flask import Flask, render_template, request, url_for, redirect
from jinja2 import Environment, FileSystemLoader
# create the application object
app = Flask(__name__)
tpldir = os.path.dirname(os.path.abspath(__file__))+'/templates/'
env = Environment(loader=FileSystemLoader(tpldir), trim_blocks=True)


# route for handling the login page logic
@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
            name = request.form.get('username')
            age = request.form.get('age')
            ninja = request.form.get('ninja')
            if name and age and ninja:
                output = env.get_template('postlogin.html').render(
                    ninja='Patrick Huston', age=age, name=name)
                return output
            else:
                return redirect(url_for('error'))
    return render_template('login.html')


@app.route('/error', methods=['GET', 'POST'])
def error():
    if request.method == 'POST':
        return redirect(url_for('login'))
    return render_template('error.html')


# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(debug=True)
