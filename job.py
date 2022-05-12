from calendar import c
from utils import *
from __main__ import app, db

@app.route("/job", methods = ["POST"])
def _create_job():
    try:
        job = job_info(request)
        job["DATE_posted"] = datetime.utcnow()
        company_id = job["COMPANYID"]
        
        dbResponse = db.companies.update_one({"COMPANYID": company_id}, {"$push": {"JOB": job}})
        return Response(
            status=200,
            response=json.dumps({"message":"Job created successfully"}
        ))
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
    # if True:
        jobs_list = []
        companies = db.companies.find()
        # companies = [json_util.dumps(company) for company in list(companies)]
        # print(companies)
        jobs = [job for job in companies if job.get("JOB") != [] and job.get("JOB") != None]
        for job in jobs:
            j_list = []
            for j in job["JOB"]:
                j["COMPANYNAME"] = job["COMPANYNAME"]
                j_list.append(j)
            jobs_list.append(j_list)
        # print(jobs_list)
        jobs_list = [json_util.dumps(job) for job in list(jobs_list)]
        return Response(
            response=json.dumps({"message":"Jobs retrieved successfully",
            "jobs":jobs_list}),
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
        print(id)
        job = db.companies.find_one({"JOB.JOBID": id},{"JOB.$":1})
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
        job["Date_update"] = datetime.utcnow()
        for k,v in job.items():
            db.companies.update_one({"JOB.JOBID": id}, {"$set": {"JOB.$."+k: v}})
        return Response(
            status=200,
            response=json.dumps({"message":"Job updated successfully"})
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
        db.companies.update_one({"JOB.JOBID": id}, {"$pull": {"JOB": {"JOBID": id}}})
        return Response(
            status=200,
            response=json.dumps({"message":"Job deleted successfully"})
        )
    except Exception as e:
        print('********')
        print(e)
        print('********')
        return Response(
            response=json.dumps({"message":"Error deleting job"}),
            status=500
        )

