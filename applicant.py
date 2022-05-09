
from flask import Flask, request, jsonify,Response
from werkzeug.utils import secure_filename
from flask_cors import CORS, cross_origin
import json
from pymongo import MongoClient
from bson import json_util
from werkzeug.contrib.fixers import ProxyFix
from utils import *
from __main__ import app, db

@app.route("/applicant", methods = ["POST"])
def _create_user():
    try:
        applicant = applicant_info(request)
        print(applicant)
        
        dbResponse = db.users.insert_one(applicant)
        return Response(
            status=200,
            response=json.dumps({"message":"Applicant created successfully",
            "id": str(dbResponse.inserted_id)})
        )
    except Exception as e:
        print('********')
        print(e)
        print('********')
        return Response(
            response=json.dumps({"message":"Error creating applicant"}),
            status=500
        )

@app.route("/applicant_check", methods = ["POST"])
def _check_user():
    try:
        username = request.form['USERNAME']
        password = request.form['PASS']
        applicant = db.users.find_one({"USERNAME": username, "PASS": password})
        if applicant:
            return Response(
                response=json.dumps({"message":"Applicant found",
                "id": str(applicant['APPLICANTID'])}),
                status=200
            )
        else:
            return Response(
                response=json.dumps({"message":"Applicant not found",
                "id": "False"}),
                status=200
            )

    except Exception as e:
        print('********')
        print(e)
        print('********')    
        return Response(
            response=json.dumps({"message":"Error checking applicant"}),
            status=500
        )

@app.route("/applicant", methods = ["GET"])
def _get_all_applicant():
    try:
        applicants = db.users.find()
        applicants = [json_util.dumps(applicant) for applicant in list(applicants)]
        print(applicants)
        return Response(
            response=json.dumps({"message":"Applicants retrieved successfully",
            "applicants":applicants}),
            status=200
        )
    except Exception as e:
        print('********')
        print(e)
        print('********')
        return Response(
            response=json.dumps({"message":"Error retrieving applicants"}),
            status=500
        )

@app.route("/applicant/<id>", methods = ["GET"])
def _get_user(id):
    try:
        applicant = db.users.find_one({"APPLICANTID": id})
        return Response(
            response=json_util.dumps(applicant),
            status=200
        )
    except Exception as e:
        print('********')
        print(e)
        print('********')
        return Response(
            response=json.dumps({"message":"Error getting applicant"}),
            status=500
        )

@app.route("/applicant/<id>", methods = ["PUT"])
def _update_user(id):
    try:
        applicant = applicant_info(request)
        applicant = {u:v for u, v in applicant.items() if v is not False}
        print(applicant)
        dbResponse = db.users.update_one(
            {"APPLICANTID": id},
            {"$set": applicant}
        )
        return Response(
            response=json.dumps({"message":"Applicant updated successfully"}),
            status=200
        )
    except Exception as e:
        print('********')
        print(e)
        print('********')
        return Response(
            response=json.dumps({"message":"Error updating applicant"}),
            status=500
        )

@app.route("/applicant/<id>", methods = ["DELETE"])
def _delete_user(id):
    try:
        dbResponse = db.users.delete_one({"APPLICANTID": id})
        return Response(
            response=json.dumps({"message":"Applicant deleted successfully"}),
            status=200
        )
    except Exception as e:
        print('********')
        print(e)
        print('********')
        return Response(
            response=json.dumps({"message":"Error deleting applicant"}),
            status=500
        )