from flask import Flask, request, jsonify,Response
from werkzeug.utils import secure_filename
from flask_cors import CORS, cross_origin
import json
from pymongo import MongoClient
from bson import json_util
from werkzeug.contrib.fixers import ProxyFix
# from utils import *

# Init Flask app
app = Flask(__name__)
cors = CORS(app)

app.config['CORS_HEADER'] = 'Content-Type'

## connect to mongoDB
try:
    client = MongoClient('localhost', 27017, serverSelectionTimeoutMS=1000)
    client.server_info()
    db = client.mydatabase
except:
    print("Could not connect to MongoDB")

## import routes
import applicant
import company 
import job   
import tblapplicant_more


# define get method
@app.route("/", methods=["GET"])
def _hello_world():
    return "MongoDB"


app.wsgi_app = ProxyFix(app.wsgi_app)  

if __name__ == "__main__":
    ### Run app
    app.run(debug=True, host='0.0.0.0', port=9001, threaded=True, processes=1)