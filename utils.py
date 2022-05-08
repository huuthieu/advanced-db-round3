from flask import Flask, request, jsonify,Response
from werkzeug.utils import secure_filename
from flask_cors import CORS, cross_origin
import json


def applicant_info(request):
    data = {
        "applicantid": request.form.get("APPLICANTID", False),
        "FNAME": request.form.get("FNAME", False),
        "LNAME": request.form.get("LNAME", False),
        "MNAME": request.form.get("MNAME", False),
        "ADDRESS": request.form.get("ADDRESS", False),
        "SEX":request.form.get("SEX", False),
        "CIVILSTATUS":request.form.get("CIVILSTATUS", False),
        "BIRTHDATE": request.form.get("BIRTHDATE", False),
        "BIRTHPLACE": request.form.get("BIRTHPLACE", False),
        "AGE": request.form.get("AGE", False),
        "USERNAME": request.form.get("USERNAME", False),
        "PASS": request.form.get("PASS", False),
        "CareerGoals": request.form.get("CareerGoals", False),
        "Achievement": request.form.get("Achievement", False),
        "EMAILADDRESS": request.form.get("EMAILADDRESS", False),
        "CONTACTNO": request.form.get("CONTACTNO", False),
        "DEGREE": request.form.get("DEGREE", False),
        "APPLICANTPHOTO": request.form.get("APPLICANTPHOTO", False),
        "NATIONALID": request.form.get("NATIONALID", False),
        "FILE_RESUME": request.form.get("FILE_RESUME", False),
        "APP_CHARACTER": request.form.get("APP_CHARACTER", False),
        "DATE_CREATE": request.form.get("DATE_CREATE", False),
        "DATE_UPDATE": request.form.get("DATE_UPDATE", False),
    }
    return data
    
def company_info(request):
    data = {
        "COMPANYID": request.form.get("COMPANYID", False),
        "COMPANYNAME": request.form.get("COMPANYNAME", False),
        "COMPANYADDRESS": request.form.get("COMPANYADDRESS", False),
        "COMPANYCONTACTNO": request.form.get("COMPANYCONTACTNO", False),
        "COMPANYLINKWEB": request.form.get("COMPANYLINKWEB", False),
        "COMPANYDESCRIPTION": request.form.get("COMPANYDESCRIPTION", False),
        "email": request.form.get("email", False),
        "USERNAME": request.form.get("USERNAME", False),
        "PASS": request.form.get("PASS", False),
        "logo": request.form.get("logo", False),
        "DATECREATE": request.form.get("DATECREATE", False),
        "DATEUPDATE": request.form.get("DATEUPDATE", False),
    }
    return data

def job_info(request):
    data = {
        "JOBID": request.form.get("JOBID", False),
        "COMPANYID": request.form.get("COMPANYID", False),
        "CATEGORY": request.form.get("CATEGORY", False),
        "OCCUPATIONTITLE": request.form.get("OCCUPATIONTITLE", False),
        "Job_Region": request.form.get("Job_Region", False),
        "REQ_NO_EMPLOYEES": request.form.get("REQ_NO_EMPLOYEES", False),
        "SALARIES": request.form.get("SALARIES", False),
        "AddressWork": request.form.get("AddressWork", False),
        "DURATION_EMPLOYEMENT": request.form.get("DURATION_EMPLOYEMENT", False),
        "QUALIFICATION_WORKEXPERIENCE": request.form.get("QUALIFICATION_WORKEXPERIENCE", False),
        "JOBDESCRIPTION": request.form.get("JOBDESCRIPTION", False),
        "PREFEREDSEX": request.form.get("PREFEREDSEX", False),
        "VACANCY_REQUIRE": request.form.get("VACANCY_REQUIRE", False),
        "WORKFORMAT": request.form.get("WORKFORMAT", False),
        "BENEFIT": request.form.get("BENEFIT", False),
        "PROFILE_REQUEST": request.form.get("PROFILE_REQUEST", False),
        "JOBSTATUS": request.form.get("JOBSTATUS", False),
        "OtherInformation": request.form.get("OtherInformation", False),
        "DATE_posted": request.form.get("DATE_posted", False),
        "Date_update": request.form.get("Date_update", False),
    }
    return data

