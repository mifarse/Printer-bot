from flask import Flask
from flask import request
import sys
import requests
import json

app = Flask(__name__)

access_token = "ee948c02249d2fd3d447d43e5bb7482d908edcd071701aca63bdec709430ba9928acf54497359dcb61e33"


def send_message(user_id):
    message_payload = {'access_token': access_token, 'message': 'Hello, friend.', 'user_id': user_id}
    r = requests.get("https://api.vk.com/method/users.get", params={'user_ids': user_id})
    user_info = json.loads(r.text)
    message_payload['message'] = "Привет! Я бот, написан на Python (Flask). А тебя зовут: {}, это я посмотрел.".format(user_info['response'][0]['first_name'])
    r = requests.get("https://api.vk.com/method/messages.send", params=message_payload)
    print(r.text)


def f(x):
    return {
        'message_new': send_message(x['object']['user_id']),
        'b': 2,
    }[x['type']]


@app.route('/', methods=['GET', 'POST'])
def hello_world():
    print(request.json)
    print(request.json['type'])
    if (request.json['type']) == "confirmation":
        return "c1c43722"
    else:
        f(request.json)
        return "ok"


if __name__ == '__main__':
    print(sys.argv)
    if len(sys.argv) > 1:
        app.run(host=sys.argv[1], port=3000)
    else:
        app.run(host="localhost", port=3000)
