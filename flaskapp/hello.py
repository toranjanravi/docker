from flask import Flask
myapp = Flask(__name__)

@myapp.route("/<string:name>/")
def index(name):
    return 'Hello! %s , Hope you are good.' % name

if __name__ == "__main__":
    myapp.run()
