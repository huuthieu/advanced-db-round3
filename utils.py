from flask import Flask, request, jsonify,Response
from werkzeug.utils import secure_filename
from flask_cors import CORS, cross_origin
import json


def applicant_info(request):
    data = {
        "applicant_id": request.form.get("id", False),
        "fname": request.form.get("fname", False),
        "lname": request.form.get("lname", False),
        "mname": request.form.get("mname", False),
        "gender":request.form.get("gender", False),
        "civilstatus":request.form.get("civilstatus", False),
        "birthdate": request.form.get("birthdate", False),
        "birthplace": request.form.get("birthplace", False),
        "age": request.form.get("age", False),
        "username": request.form.get("username", False),
        "password": request.form.get("password", False),
        "career_goal": request.form.get("career_goal", False),
        "achivement": request.form.get("achivement", False),
        "emailaddress": request.form.get("emailaddress", False),
        "degree": request.form.get("degree", False),
        "photo": request.form.get("photo", False),
        "national": request.form.get("national", False),
        "file_resume": request.form.get("file_resume", False),
        "character": request.form.get("character", False),
        "date_created": request.form.get("date_created", False),
        "date_updated": request.form.get("date_updated", False),
    }
    return data
    
def company_info(request):
    data = {
        "company_id": request.form.get("id", False),
        "name": request.form.get("name", False),
        "address": request.form.get("address", False),
        "contact": request.form.get("contact", False),
        "web_page": request.form.get("web_page", False),
        "description": request.form.get("description", False),
        "email": request.form.get("email", False),
        "username": request.form.get("username", False),
        "password": request.form.get("password", False),
        "logo": request.form.get("company_logo", False),
        "date_created": request.form.get("date_created", False),
        "date_updated": request.form.get("date_updated", False),
    }
    return data

def job_info(request):
    data = {
        "job_id": request.form.get("id", False),
        "company_id": request.form.get("company_id", False),
        "title": request.form.get("title", False),
        "req_num_employee": request.form.get("req_num_employee", False),
        "salary": request.form.get("salary", False),
        "work_place": request.form.get("work_place", False),
        "duration_employment": request.form.get("duration_employment", False),
        "qualification_workexperience": request.form.get("qualification_workexperience", False),
        "job_description": request.form.get("description", False),
        "prefer_gender": request.form.get("prefer_gender", False),
        "requirements": request.form.get("requirements", False),
        "work_format": request.form.get("work_format", False),
        "benefit": request.form.get("benefit", False),
        "profile_request": request.form.get("profile_request", False),
        "job_status": request.form.get("job_status", False),
        "other_information": request.form.get("other_information", False),
        "date_created": request.form.get("date_created", False),
        "date_updated": request.form.get("date_updated", False),
    }
    return data

