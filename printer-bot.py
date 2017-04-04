from flask import Flask
import sys
import json

app = Flask(__name__)


@app.route('/')
def hello_world():
    return "c1c43722"


if __name__ == '__main__':
    print(sys.argv)
    if len(sys.argv) > 1:
        app.run(host=sys.argv[1], port=3000)
    else:
        app.run(host="localhost", port=3000)
