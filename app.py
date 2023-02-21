from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello, World!"

@app.route("/rasengan")
def rasengan1():
    data=request.args.get('x')
    return "ths is my {}".format(data)
if __name__=="__main__":
    app.run(host="0.0.0.0")
