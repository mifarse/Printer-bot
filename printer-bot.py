from flask import Flask
from flask import request
import sys
import json

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def hello_world():
    print(request.json)
    print(request.json['type'])
    if (request.json['type']) == "confirmation":
        return "c1c43722"
    else:
        return "ok"


if __name__ == '__main__':
    print(sys.argv)
    if len(sys.argv) > 1:
        app.run(host=sys.argv[1], port=3000)
    else:
        app.run(host="localhost", port=3000)
