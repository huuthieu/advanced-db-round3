from flask import Flask, request, jsonify,Response
from werkzeug.utils import secure_filename
from flask_cors import CORS, cross_origin
import json


def applicant_info(request):
    data = {
        "applicantid": request.form.get("applicantid", False),
        "fname": request.form.get("fname", False),
        "lname": request.form.get("lname", False),
        "mname": request.form.get("mname", False),
        "sex":request.form.get("sex", False),
        "civilstatus":request.form.get("civilstatus", False),
        "birthdate": request.form.get("birthdate", False),
        "birthplace": request.form.get("birthplace", False),
        "age": request.form.get("age", False),
        "username": request.form.get("username", False),
        "password": request.form.get("password", False),
        "careergoal": request.form.get("careergoal", False),
        "achivement": request.form.get("achivement", False),
        "emailaddress": request.form.get("emailaddress", False),
        "degree": request.form.get("degree", False),
        "applicantphoto": request.form.get("applicantphoto", False),
        "nationalid": request.form.get("nationalid", False),
        "file_resume": request.form.get("file_resume", False),
        "character": request.form.get("character", False),
        "date_created": request.form.get("date_created", False),
        "date_updated": request.form.get("date_updated", False),
    }
    return data
    
def company_info(request):
    data = {
        "companyid": request.form.get("companyid", False),
        "companyname": request.form.get("companyname", False),
        "companyaddress": request.form.get("companyaddress", False),
        "companycontactno": request.form.get("companycontactno", False),
        "companylinkweb": request.form.get("companylinkweb", False),
        "email": request.form.get("email", False),
        "username": request.form.get("username", False),
        "password": request.form.get("password", False),
        "logo": request.form.get("logo", False),
        "date_created": request.form.get("date_created", False),
        "date_updated": request.form.get("date_updated", False),
    }
    return data

def job_info(request):
    data = {
        "jobid": request.form.get("jobid", False),
        "companyid": request.form.get("companyid", False),
        "category": request.form.get("category", False),
        "occupationtitle": request.form.get("occupationtitle", False),
        "jobregion": request.form.get("jobregion", False),
        "req_no_employees": request.form.get("req_no_employees", False),
        "salaries": request.form.get("salaries", False),
        "addresswork": request.form.get("addresswork", False),
        "duration_employment": request.form.get("duration_employment", False),
        "qualification_workexperience": request.form.get("qualification_workexperience", False),
        "jobdescription": request.form.get("jobdescription", False),
        "preferedsex": request.form.get("preferedsex", False),
        "vacancy_require": request.form.get("vacancy_require", False),
        "workformat": request.form.get("workformat", False),
        "benefit": request.form.get("benefit", False),
        "profile_request": request.form.get("profile_request", False),
        "jobstatus": request.form.get("jobstatus", False),
        "otherinformation": request.form.get("otherinformation", False),
        "date_posted": request.form.get("date_posted", False),
        "date_updated": request.form.get("date_updated", False),
    }
    return data

