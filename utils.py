from dataclasses import dataclass
from this import d
from flask import Flask, request, jsonify,Response
from werkzeug.utils import secure_filename
from flask_cors import CORS, cross_origin
import json
from datetime import datetime
import time
from pymongo import MongoClient
from bson import json_util
from werkzeug.contrib.fixers import ProxyFix


def applicant_info(request):
    data = {
        "APPLICANTID": request.form.get("APPLICANTID", False),
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

def foreign_language_info(request):
    data = {
        "id": request.form.get("id", False),
        "APPLICANTID": request.form.get("APPLICANTID", False),
        "Foreign_lan": request.form.get("Foreign_lan", False),
        "score": request.form.get("score", False),
        "date_issue": request.form.get("date_issue", False)
    }
    return data


def level_learn_info(request):
    data = {
        id: request.form.get("id", False),
        "APPLICANTID": request.form.get("APPLICANTID", False),
        "DEGREE": request.form.get("DEGREE", False),
        "Start_date": request.form.get("Start_date", False),
        "End_date": request.form.get("End_date", False),
        "specialized": request.form.get("specialized", False),
        "classification": request.form.get("classification", False),
        "SCHOOL": request.form.get("SCHOOL", False)
    }
    return data

def prefer_job_info(request):
    data = {
        "id": request.form.get("id", False),
        "APPLICANTID": request.form.get("APPLICANTID", False),
        "JOB": request.form.get("JOB", False),
        "DEGREE": request.form.get("DEGREE", False),
        "CATEGORY": request.form.get("CATEGORY", False),
        "LOCATION": request.form.get("LOCATION", False),
        "SALARY": request.form.get("SALARY", False),
        "WORK_FORMAT": request.form.get("WORK_FORMAT", False),
        "EXPERIENCE": request.form.get("EXPERIENCE", False)
    }
    return data

def cv_info(request):
    data = {
        "id": request.form.get("id", False),
        "APPLICANTID": request.form.get("APPLICANTID", False),
        "CV_NAME": request.form.get("CV_NAME", False),
        "DATE_POST": request.form.get("DATE_POST", False)
    }
    return data

def attachmentfile_info(request):
    data = {
        "FIELDID": request.form.get("FIELDID", False),
        "JOBID": request.form.get("JOBID", False),
        "FILE_NAME": request.form.get("FILE_NAME", False),
        "FILE_LOCATION": request.form.get("FILE_LOCATION", False),
        "USERATTACHMENTID": request.form.get("USERATTACHMENTID", False)
    }
    return data

def category_info(request):
    data = {
        "CATEGORYID": request.form.get("CATEGORYID", False),
        "CATEGORY": request.form.get("CATEGORY", False),
    }  
    return data

def jobregistration_info(request):
    data = {
        "REGISTRATIONID": request.form.get("REGISTRATIONID", False),
        "COMPANYID": request.form.get("COMPANYID", False),
        "JOBID": request.form.get("JOBID", False),
        "APPLICANTID": request.form.get("APPLICANTID", False),
        "REGISTRATIONDATE": request.form.get("REGISTRATIONDATE", False),
        "REMARKS": request.form.get("REMARKS", False),
        "FILEID": request.form.get("FILEID", False),
        "PENDINGAPPLICATION": request.form.get("PENDINGAPPLICATION", False),
        "HVIEW": request.form.get("HVIEW", False),
        "applied_status": request.form.get("applied_status", False),
        "CONTENT": request.form.get("CONTENT", False),
        "Start_at": request.form.get("Start_at", False),
        "End_at": request.form.get("End_at", False),
        "Start_time": request.form.get("Start_time", False),
        "End_time": request.form.get("End_time", False),
        "DATETIMEAPPROVED": request.form.get("DATETIMEAPPROVED", False)
    }
    return data

def user_info(request):
    data = {
        "USERID": request.form.get("USERID", False),
        "FULLNAME": request.form.get("FULLNAME", False),
        "USERNAME": request.form.get("USERNAME", False),
        "PASS": request.form.get("PASS", False),
        "ROLE": request.form.get("ROLE", False),
        "PICLOCATION": request.form.get("PICLOCATION", False)
    }
    return data

def skill_info(request):
    data = {
        "id": request.form.get("id", False),
        "APPLICANTID": request.form.get("APPLICANTID", False),
        "Skill": request.form.get("Skill", False),
        "desc_skill": request.form.get("desc_skill", False),
        "level": request.form.get("level", False)
    }
    return data
    
def work_experience_info(request):
    data = {
        "id": request.form.get("id", False),
        "APPLICANTID": request.form.get("APPLICANTID", False),
        "TITLE": request.form.get("TITLE", False),
        "COMPANY": request.form.get("COMPANY", False),
        "STARTDATE": request.form.get("STARTDATE", False),
        "ENDDATE": request.form.get("ENDDATE", False),
        "JOBDESCRIPTION": request.form.get("JOBDESCRIPTION", False)
    }
    return data