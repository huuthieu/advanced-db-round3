from flask import Flask, request, jsonify,Response
from werkzeug.utils import secure_filename
from flask_cors import CORS, cross_origin
import json
from pymongo import MongoClient
from bson import json_util
from werkzeug.contrib.fixers import ProxyFix
from utils import *
from __main__ import app, db

@app.route("/company", methods = ["POST"])
def _create():
    try:
        company = company_info(request)
        print(company)
        
        dbResponse = db.users.insert_one(company)
        return Response(
            status=200,
            response=json.dumps({"message":"Company created successfully",
            "id": str(dbResponse.inserted_id)})
        )
    except Exception as e:
        print('********')
        print(e)
        print('********')
        return Response(
            response=json.dumps({"message":"Error creating company"}),
            status=500
        )
    
@app.route("/company/<id>", methods = ["GET"])
def _get(id):
    try:    
        company = db.users.find_one({"company_id": id})
        return Response(
            response=json_util.dumps(company),
            status=200
        )
    except Exception as e:
        print('********')
        print(e)
        print('********')
        return Response(
            response=json.dumps({"message":"Error getting company"}),
            status=500
        )

@app.route("/company/<id>", methods = ["PUT"])
def _update(id):
    try:
        company = company_info(request)
        company = {u:v for u, v in company.items() if v is not False}
        dbResponse = db.users.update_one(
            {"company_id": id},
            {"$set": company}
        )
        return Response(
            response=json.dumps({"message":"Company updated successfully"}),
            status=500
        )
    except Exception as e:
        print('********')
        print(e)
        print('********')
        return Response(
            response=json.dumps({"message":"Error updating company"}),
            status=500
        )

@app.route("/company/<id>", methods = ["DELETE"])
def _delete(id):
    try:
        dbResponse = db.users.delete_one({"company_id": id})
        return Response(
            response=json.dumps({"message":"Company deleted successfully"}),
            status=200
        )
    except Exception as e:
        print('********')
        print(e)
        print('********')
        return Response(
            response=json.dumps({"message":"Error deleting company"}),
            status=500
        )