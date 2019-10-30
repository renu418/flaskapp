from flask import Flask, request
import json
import requests
from db import MongoHandler
from mail import send_mail
from bson.json_util import dumps

def decodeBinary(binaryData):
    return json.loads(binaryData.decode('utf-8'))

app = Flask(__name__)
@app.route("/register", methods=["POST"])
def signup():
    username = request.json['username']
    email = request.json['email']
    print("------------------", username, email)
    passwd = send_mail.send_mail(username, email)
    parser = {
        "username": str(username),
        "password": str(passwd),
        "email": str(email)
    }
    print(parser)
    db = "app"
    collection = "user_details"
    mongo.insert(db, collection, parser)
    return str(parser)

if __name__ == '__main__':
    mongo = MongoHandler.MongoHandler()
    app.run(debug=True, host="0.0.0.0", port="5004")
