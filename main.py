# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask, request
import pdb

# Flask constructor takes the name of
# current module (__name__) as argument.
app = Flask(__name__)


# The route() function of the Flask class is a decorator,
# which tells the application which URL should call
# the associated function.
# ‘/’ URL is bound with hello_world() function.
@app.route('/', methods=["POST"])
def hello_world():
    if 'first' in request.args and 'second' in request.args and 'symbol' in request.args:
        if request.args.get('symbol') in ['+', '-', '/', '*']:
            st = request.args.get('first') + request.args.get('symbol') + request.args.get('second')
        else:
            st = 'invalid symbol'
    else:
        st = 'invalid arguments'
    return st


# main driver function
if __name__ == '__main__':
    # run() method of Flask class runs the application
    # on the local development server.
    app.run()
