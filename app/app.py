# initialize and start python server

# import Flask module
from flask import Flask 
app = Flask(__name__)

# register view function for given URL /
@app.route('/')
def hello_world():
    return 'Hello, World!'

# initializes python flask server
# note: do not use this run method in production, use UWSGI or CGI instead
if __name__ == '__main__':
    app.run(host='0.0.0.0')
