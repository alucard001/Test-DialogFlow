import json
import os

from flask import Flask
from flask import request
from flask import make_response

app = Flask(__name__)

@app.route('webhook', methods=["POST"])

def webhook():
    req = request.get_json(slient=True, force=True)
    print(json.dumps(req, indent=4))

    res = make_response(req)
    res = json.dumps(res, indent=4)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r