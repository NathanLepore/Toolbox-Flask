import os
from flask import Flask, render_template, request, url_for, redirect
from jinja2 import Environment, FileSystemLoader
# create the application object
app = Flask(__name__)
tpldir = os.path.dirname(os.path.abspath(__file__))+'/templates/'
env = Environment(loader=FileSystemLoader(tpldir), trim_blocks=True)


@app.route('/', methods=['GET', 'POST'])
def Jquerytest():
    return render_template('MP5.html')


# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(debug=True)
