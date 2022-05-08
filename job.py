from flask import Flask, request, jsonify,Response
from werkzeug.utils import secure_filename
from flask_cors import CORS, cross_origin
import json
from pymongo import MongoClient
from bson import json_util
from werkzeug.contrib.fixers import ProxyFix
from utils import *
from __main__ import app, db

@app.route("/job", methods = ["POST"])
def _create_job():
    try:
        job = job_info(request)
        
        dbResponse = db.jobs.insert_one(job)
        return Response(
            status=200,
            response=json.dumps({"message":"Job created successfully",
            "id": str(dbResponse.inserted_id)})
        )
    except Exception as e:
        print('********')
        print(e)
        print('********')
        return Response(
            response=json.dumps({"message":"Error creating job"}),
            status=500
        )

@app.route("/job", methods = ["GET"])
def _get_all_job():
    try:
        jobs = db.jobs.find()
        jobs = [json_util.dumps(job) for job in list(jobs)]
        return Response(
            response=json.dumps({"message":"Jobs retrieved successfully",
            "jobs":jobs}),
            status=200
        )
    except Exception as e:
        print('********')
        print(e)
        print('********')
        return Response(
            response=json.dumps({"message":"Error retrieving jobs"}),
            status=500
        )


@app.route("/job/<id>", methods = ["GET"])
def _get_job(id):
    try:    
        job = db.jobs.find_one({"jobid": id})
        return Response(
            response=json_util.dumps(job),
            status=200
        )
    except Exception as e:
        print('********')
        print(e)
        print('********')
        return Response(
            response=json.dumps({"message":"Error getting job"}),
            status=500
        )

@app.route("/job/<id>", methods = ["PUT"])
def _update_job(id):
    try:
        job = job_info(request)
        job = {u:v for u, v in job.items() if v is not False}
        dbResponse = db.jobs.update_one(
            {"jobid": id},
            {"$set": job}
        )
        return Response(
            response=json.dumps({"message":"Job updated successfully"}),
            status=500
        )
    except Exception as e:
        print('********')
        print(e)
        print('********')
        return Response(
            response=json.dumps({"message":"Error updating job"}),
            status=500
        )

@app.route("/job/<id>", methods = ["DELETE"])
def _delete_job(id):
    try:
        dbResponse = db.jobs.delete_one({"jobid": id})
        return Response(
            response=json.dumps({"message":"Job deleted successfully"}),
            status=500
        )
    except Exception as e:
        print('********')
        print(e)
        print('********')
        return Response(
            response=json.dumps({"message":"Error deleting job"}),
            status=500
        )

