from utils import *
from __main__ import app, db

@app.route("/applicant_foreign_language", methods = ["POST"])
def _create_applicant_fl():
    try:
        applicant_fl = foreign_language_info(request)
        applicant_id = applicant_fl['APPLICANTID']
        db.users.update_one({"APPLICANTID": applicant_id}, {"$push": {"FOREIGN_LANGUAGE": applicant_fl}})
        return Response(
            status=200,
            response=json.dumps({"message":"Applicant foreign language created successfully",
            "id": str(applicant_id)})
        )
    except Exception as e:
        print('********')
        print(e)
        print('********')
        return Response(
            response=json.dumps({"message":"Error creating applicant foreign language"}),
            status=500
        )

@app.route("/applicant_foreign_language/<applicant_id>", methods = ["GET"])
def _get_applicant_fl(applicant_id):
    try:
        applicant_fl = db.users.find_one({"APPLICANTID": applicant_id}, {"FOREIGN_LANGUAGE": 1})
        applicant_fl = [json_util.dumps(fl) for fl in list(applicant_fl["FOREIGN_LANGUAGE"])]
        if applicant_fl:
            return Response(
                response=json.dumps({"message":"Applicant foreign language found",
                "applicant_fl": applicant_fl}),
                status=200
            )
        else:
            return Response(
                response=json.dumps({"message":"Applicant foreign language not found",
                "applicant_fl": "False"}),
                status=200
            )
    except Exception as e:
        print('********')
        print(e)
        print('********')
        return Response(
            response=json.dumps({"message":"Error getting applicant foreign language"}),
            status=500
        )

@app.route("/applicant_foreign_language/<fl_id>", methods = ["PUT"])
def _update_applicant_fl(fl_id):
    try:
        applicant_fl = foreign_language_info(request)
        applicant_fl = {u:v for u, v in applicant_fl.items() if v is not False}
        for k, v in applicant_fl.items():
            db.users.update_one({"FOREIGN_LANGUAGE.id": fl_id}, {"$set": {"FOREIGN_LANGUAGE.$."+k: v}})
        return Response(
            response=json.dumps({"message":"Applicant foreign language updated successfully",
            "id": str(fl_id)}),
            status=200
        )

    except Exception as e:
        print('********')
        print(e)
        print('********')
        return Response(
            response=json.dumps({"message":"Error updating applicant foreign language"}),
            status=500
        )

@app.route("/applicant_foreign_language/<fl_id>", methods = ["DELETE"])
def _delete_applicant_fl(fl_id):
    try:
        db.users.update_one({"FOREIGN_LANGUAGE.id": fl_id}, {"$pull": {"FOREIGN_LANGUAGE": {"id": fl_id}}})
        return Response(
            response=json.dumps({"message":"Applicant foreign language deleted successfully",
            "id": str(fl_id)}),
            status=200
        )
    except Exception as e:
        print('********')
        print(e)
        print('********')
        return Response(
            response=json.dumps({"message":"Error deleting applicant foreign language"}),
            status=500
        )

### LEVEL LEARN

@app.route("/applicant_level_learn", methods = ["POST"])
def _create_applicant_lv():
    try:
        applicant_lv = level_learn_info(request)
        applicant_id = applicant_lv['APPLICANTID']
        db.users.update_one({"APPLICANTID": applicant_id}, {"$push": {"LEVEL_LEARN": applicant_lv}})
        return Response(
            status=200,
            response=json.dumps({"message":"Applicant foreign language created successfully",
            "id": str(applicant_id)})
        )
    except Exception as e:
        print('********')
        print(e)
        print('********')
        return Response(
            response=json.dumps({"message":"Error creating applicant foreign language"}),
            status=500
        )

@app.route("/applicant_level_learn/<applicant_id>", methods = ["GET"])
def _get_applicant_lv(applicant_id):
    try:
        applicant_lv = db.users.find_one({"APPLICANTID": applicant_id}, {"LEVEL_LEARN": 1})
        applicant_lv = [json_util.dumps(lv) for lv in list(applicant_lv["LEVEL_LEARN"])]
        if applicant_lv:
            return Response(
                response=json.dumps({"message":"Applicant level learn found",
                "applicant_lv": applicant_lv}),
                status=200
            )
        else:
            return Response(
                response=json.dumps({"message":"Applicant level learn not found",
                "applicant_lv": "False"}),
                status=200
            )
    except Exception as e:
        print('********')
        print(e)
        print('********')
        return Response(
            response=json.dumps({"message":"Error getting applicant level learn"}),
            status=500
        )

@app.route("/applicant_level_learn/<lv_id>", methods = ["PUT"])
def _update_applicant_lv(lv_id):
    try:
        applicant_lv = level_learn_info(request)
        applicant_lv = {u:v for u, v in applicant_lv.items() if v is not False}
        for k, v in applicant_lv.items():
            db.users.update_one({"LEVEL_LEARN.id": lv_id}, {"$set": {"LEVEL_LEARN.$."+k: v}})
        return Response(
            response=json.dumps({"message":"Applicant level learn updated successfully",
            "id": str(lv_id)}),
            status=200
        )

    except Exception as e:
        print('********')
        print(e)
        print('********')
        return Response(
            response=json.dumps({"message":"Error updating applicant level learn"}),
            status=500
        )

@app.route("/applicant_level_learn/<lv_id>", methods = ["DELETE"])
def _delete_applicant_lv(lv_id):
    try:
        db.users.update_one({"LEVEL_LEARN.id": lv_id}, {"$pull": {"LEVEL_LEARN": {"id": lv_id}}})
        return Response(
            response=json.dumps({"message":"Applicant level learn deleted successfully",
            "id": str(lv_id)}),
            status=200
        )
    except Exception as e:
        print('********')
        print(e)
        print('********')
        return Response(
            response=json.dumps({"message":"Error deleting applicant level learn"}),
            status=500
        )


## PREFER JOB
@app.route("/applicant_prefer_job", methods = ["POST"])
def _create_applicant_pj():
    try:
        applicant_pj = prefer_job_info(request)
        applicant_id = applicant_pj['APPLICANTID']
        db.users.update_one({"APPLICANTID": applicant_id}, {"$push": {"PREFER_JOB": applicant_pj}})
        return Response(
            status=200,
            response=json.dumps({"message":"Applicant prefer job created successfully",
            "id": str(applicant_id)})
        )
    except Exception as e:
        print('********')
        print(e)
        print('********')
        return Response(
            response=json.dumps({"message":"Error creating applicant prefer job"}),
            status=500
        )

@app.route("/applicant_prefer_job/<applicant_id>", methods = ["GET"])
def _get_applicant_pj(applicant_id):
    try:
        applicant_pj = db.users.find_one({"APPLICANTID": applicant_id}, {"PREFER_JOB": 1})
        applicant_pj = [json_util.dumps(pj) for pj in list(applicant_pj["PREFER_JOB"])]
        if applicant_pj:
            return Response(
                response=json.dumps({"message":"Applicant prefer job found",
                "applicant_pj": applicant_pj}),
                status=200
            )
        else:
            return Response(
                response=json.dumps({"message":"Applicant prefer job not found",
                "applicant_pj": "False"}),
                status=200
            )
    except Exception as e:
        print('********')
        print(e)
        print('********')
        return Response(
            response=json.dumps({"message":"Error getting applicant prefer job"}),
            status=500
        )

@app.route("/applicant_prefer_job/<pj_id>", methods = ["PUT"])
def _update_applicant_pj(pj_id):
    try:
        applicant_pj = prefer_job_info(request)
        applicant_pj = {u:v for u, v in applicant_pj.items() if v is not False}
        for k, v in applicant_pj.items():
            db.users.update_one({"PREFER_JOB.id": pj_id}, {"$set": {"PREFER_JOB.$."+k: v}})
        return Response(
            response=json.dumps({"message":"Applicant prefer job updated successfully",
            "id": str(pj_id)}),
            status=200
        )

    except Exception as e:
        print('********')
        print(e)
        print('********')
        return Response(
            response=json.dumps({"message":"Error updating applicant prefer job"}),
            status=500
        )

@app.route("/applicant_prefer_job/<pj_id>", methods = ["DELETE"])
def _delete_applicant_pj(pj_id):
    try:
        db.users.update_one({"PREFER_JOB.id": pj_id}, {"$pull": {"PREFER_JOB": {"id": pj_id}}})    
        return Response(
            response=json.dumps({"message":"Applicant prefer job deleted successfully",
            "id": str(pj_id)}),
            status=200
        )
    except Exception as e:
        print('********')
        print(e)
        print('********')
        return Response(
            response=json.dumps({"message":"Error deleting applicant prefer job"}),
            status=500
        )

## CV
@app.route("/applicant_cv", methods = ["POST"])
def _create_applicant_cv():
    try:
        applicant_cv = cv_info(request)
        applicant_id = applicant_cv['APPLICANTID']
        db.users.update_one({"APPLICANTID": applicant_id}, {"$push": {"CV": applicant_cv}})
        return Response(
            status=200,
            response=json.dumps({"message":"Applicant cv created successfully",
            "id": str(applicant_id)})
        )
    except Exception as e:
        print('********')
        print(e)
        print('********')
        return Response(
            response=json.dumps({"message":"Error creating applicant cv"}),
            status=500
        )

@app.route("/applicant_cv/<applicant_id>", methods = ["GET"])
def _get_applicant_cv(applicant_id):
    try:
        applicant_cv = db.users.find_one({"APPLICANTID": applicant_id}, {"CV": 1})
        applicant_cv = [json_util.dumps(cv) for cv in list(applicant_cv["CV"])]
        if applicant_cv:
            return Response(
                response=json.dumps({"message":"Applicant cv found",
                "applicant_cv": applicant_cv}),
                status=200
            )
        else:
            return Response(
                response=json.dumps({"message":"Applicant cv not found",
                "applicant_cv": "False"}),
                status=200
            )

    except Exception as e:
        print('********')
        print(e)
        print('********')
        return Response(
            response=json.dumps({"message":"Error getting applicant cv"}),
            status=500
        )

@app.route("/applicant_cv/<cv_id>", methods = ["PUT"])
def _update_applicant_cv(cv_id):
    try:
        applicant_cv = cv_info(request)
        applicant_cv = {u:v for u, v in applicant_cv.items() if v is not False}
        for k, v in applicant_cv.items():
            db.users.update_one({"CV.id": cv_id}, {"$set": {"CV.$."+k: v}})
        return Response(
            response=json.dumps({"message":"Applicant cv updated successfully",
            "id": str(cv_id)}),
            status=200
        )

    except Exception as e:
        print('********')
        print(e)
        print('********')
        return Response(
            response=json.dumps({"message":"Error updating applicant cv"}),
            status=500
        )

@app.route("/applicant_cv/<cv_id>", methods = ["DELETE"])
def _delete_applicant_cv(cv_id):
    try:
        db.users.update_one({"CV.id": cv_id}, {"$pull": {"CV": {"id": cv_id}}})    
        return Response(
            response=json.dumps({"message":"Applicant cv deleted successfully",
            "id": str(cv_id)}),
            status=200
        )
    except Exception as e:
        print('********')
        print(e)
        print('********')
        return Response(
            response=json.dumps({"message":"Error deleting applicant cv"}),
            status=500
        )

## ATTACHMENTFILE
@app.route("/applicant_attachmentfile", methods = ["POST"])
def _create_applicant_attachmentfile():
    try:
        applicant_attachmentfile = attachmentfile_info(request)
        applicant_id = applicant_attachmentfile['APPLICANTID']
        db.users.update_one({"APPLICANTID": applicant_id}, {"$push": {"ATTACHMENTFILE": applicant_attachmentfile}})
        return Response(
            status=200,
            response=json.dumps({"message":"Applicant attachmentfile created successfully",
            "id": str(applicant_id)})
        )
    except Exception as e:
        print('********')
        print(e)
        print('********')
        return Response(
            response=json.dumps({"message":"Error creating applicant attachmentfile"}),
            status=500
        )

@app.route("/applicant_attachmentfile/<applicant_id>", methods = ["GET"])
def _get_applicant_attachmentfile(applicant_id):
    try:
        applicant_attachmentfile = db.users.find_one({"APPLICANTID": applicant_id}, {"ATTACHMENTFILE": 1})
        applicant_attachmentfile = [json_util.dumps(attachmentfile) for attachmentfile in list(applicant_attachmentfile["ATTACHMENTFILE"])]
        if applicant_attachmentfile:
            return Response(
                response=json.dumps({"message":"Applicant attachmentfile found",
                "applicant_attachmentfile": applicant_attachmentfile}),
                status=200
            )
        else:
            return Response(
                response=json.dumps({"message":"Applicant attachmentfile not found",
                "applicant_attachmentfile": "False"}),
                status=200
            )

    except Exception as e:
        print('********')
        print(e)
        print('********')
        return Response(
            response=json.dumps({"message":"Error getting applicant attachmentfile"}),
            status=500
        )

@app.route("/applicant_attachmentfile/<attachmentfile_id>", methods = ["PUT"])
def _update_applicant_attachmentfile(attachmentfile_id):
    try:
        applicant_attachmentfile = attachmentfile_info(request)
        applicant_attachmentfile = {u:v for u, v in applicant_attachmentfile.items() if v is not False}
        for k, v in applicant_attachmentfile.items():
            db.users.update_one({"ATTACHMENTFILE.id": attachmentfile_id}, {"$set": {"ATTACHMENTFILE.$."+k: v}})
        return Response(
            response=json.dumps({"message":"Applicant attachmentfile updated successfully",
            "id": str(attachmentfile_id)}),
            status=200
        )

    except Exception as e:
        print('********')
        print(e)
        print('********')
        return Response(
            response=json.dumps({"message":"Error updating applicant attachmentfile"}),
            status=500
        )

@app.route("/applicant_attachmentfile/<attachmentfile_id>", methods = ["DELETE"])
def _delete_applicant_attachmentfile(attachmentfile_id):
    try:
        db.users.update_one({"ATTACHMENTFILE.id": attachmentfile_id}, {"$pull": {"ATTACHMENTFILE": {"id": attachmentfile_id}}})    
        return Response(
            response=json.dumps({"message":"Applicant attachmentfile deleted successfully",
            "id": str(attachmentfile_id)}),
            status=200
        )
    except Exception as e:
        print('********')
        print(e)
        print('********')
        return Response(
            response=json.dumps({"message":"Error deleting applicant attachmentfile"}),
            status=500
        )

## CATEGORY
@app.route("/category", methods = ["POST"])
def _create_category():
    try:
        category = category_info(request)
        db.users.update_one({"CATEGORY": category["CATEGORY"]}, {"$set": {"CATEGORY": category}})
        return Response(
            status=200,
            response=json.dumps({"message":"Category created successfully",
            "category": category["CATEGORY"]})
        )
    except Exception as e:
        print('********')
        print(e)
        print('********')
        return Response(
            response=json.dumps({"message":"Error creating category"}),
            status=500
        )

@app.route("/category/<applicant_id>", methods = ["GET"])
def _get_category(applicant_id):
    try:
        category = db.users.find_one({"APPLICANTID": applicant_id}, {"CATEGORY": 1})
        category = [json_util.dumps(category) for category in list(category["CATEGORY"])]
        if category:    
            return Response(
                response=json.dumps({"message":"Category found",
                "category": category}),
                status=200
            )
        else:
            return Response(
                response=json.dumps({"message":"Category not found",
                "category": "False"}),
                status=200
            )
    except Exception as e:
        print('********')
        print(e)
        print('********')
        return Response(
            response=json.dumps({"message":"Error getting category"}),
            status=500
        )

@app.route("/category/<category_id>", methods = ["PUT"])
def _update_category(category_id):
    try:
        category = category_info(request)
        category = {u:v for u, v in category.items() if v is not False}
        for k, v in category.items():
            db.users.update_one({"CATEGORY": category_id}, {"$set": {"CATEGORY.$."+k: v}})
        return Response(
            response=json.dumps({"message":"Category updated successfully",
            "id": str(category_id)}),
            status=200
        )
    except Exception as e:
        print('********')
        print(e)
        print('********')
        return Response(
            response=json.dumps({"message":"Error updating category"}),
            status=500
        )

@app.route("/category/<category_id>", methods = ["DELETE"])
def _delete_category(category_id):
    try:
        db.users.update_one({"CATEGORY": category_id}, {"$pull": {"CATEGORY": {"id": category_id}}})
        return Response(
            response=json.dumps({"message":"Category deleted successfully",
            "id": str(category_id)}),
            status=200
        )
    except Exception as e:
        print('********')
        print(e)
        print('********')
        return Response(
            response=json.dumps({"message":"Error deleting category"}),
            status=500
        )

## jobregistration
@app.route("/jobregistration", methods = ["POST"])
def _create_jobregistration():
    try:
        jobregistration = jobregistration_info(request)
        db.users.update_one({"JOBREGISTRATION": jobregistration["JOBREGISTRATION"]}, {"$set": {"JOBREGISTRATION": jobregistration}})
        return Response(
            status=200,
            response=json.dumps({"message":"Jobregistration created successfully",
            "jobregistration": jobregistration["JOBREGISTRATION"]})
        )
    except Exception as e:
        print('********')
        print(e)
        print('********')
        return Response(
            response=json.dumps({"message":"Error creating jobregistration"}),
            status=500
        )

@app.route("/jobregistration/<applicant_id>", methods = ["GET"])
def _get_jobregistration(applicant_id):
    try:
        jobregistration = db.users.find_one({"APPLICANTID": applicant_id}, {"JOBREGISTRATION": 1})
        jobregistration = [json_util.dumps(jobregistration) for jobregistration in list(jobregistration["JOBREGISTRATION"])]
        if jobregistration:
            return Response(
                response=json.dumps({"message":"Jobregistration found",
                "jobregistration": jobregistration}),
                status=200
            )
        else:
            return Response(
                response=json.dumps({"message":"Jobregistration not found",
                "jobregistration": "False"}),
                status=200
            )
    except Exception as e:
        print('********')
        print(e)
        print('********')
        return Response(
            response=json.dumps({"message":"Error getting jobregistration"}),
            status=500
        )

@app.route("/jobregistration/<jobregistration_id>", methods = ["PUT"])
def _update_jobregistration(jobregistration_id):
    try:
        jobregistration = jobregistration_info(request)
        jobregistration = {u:v for u, v in jobregistration.items() if v is not False}
        for k, v in jobregistration.items():
            db.users.update_one({"JOBREGISTRATION": jobregistration_id}, {"$set": {"JOBREGISTRATION.$."+k: v}})
        return Response(
            response=json.dumps({"message":"Jobregistration updated successfully",
            "id": str(jobregistration_id)}),
            status=200
        )
    except Exception as e:
        print('********')
        print(e)
        print('********')
        return Response(
            response=json.dumps({"message":"Error updating jobregistration"}),
            status=500
        )

@app.route("/jobregistration/<jobregistration_id>", methods = ["DELETE"])
def _delete_jobregistration(jobregistration_id):
    try:
        db.users.update_one({"JOBREGISTRATION": jobregistration_id}, {"$pull": {"JOBREGISTRATION": {"id": jobregistration_id}}})
        return Response(
            response=json.dumps({"message":"Jobregistration deleted successfully",
            "id": str(jobregistration_id)}),
            status=200
        )
    except Exception as e:
        print('********')
        print(e)
        print('********')
        return Response(
            response=json.dumps({"message":"Error deleting jobregistration"}),
            status=500
        )

## users
@app.route("/users", methods = ["POST"])
def _create_appl_user():
    try:
        user = user_info(request)
        db.users.update_one({"USER": user["USER"]}, {"$set": {"USER": user}})
        return Response(
            status=200,
            response=json.dumps({"message":"User created successfully",
            "user": user["USER"]})
        )
    except Exception as e:
        print('********')
        print(e)
        print('********')
        return Response(
            response=json.dumps({"message":"Error creating user"}),
            status=500
        )

@app.route("/users/<applicant_id>", methods = ["GET"])
def _get_appl_user(applicant_id):
    try:
        user = db.users.find_one({"APPLICANTID": applicant_id}, {"USER": 1})
        user = [json_util.dumps(user) for user in list(user["USER"])]
        if user:
            return Response(
                response=json.dumps({"message":"User found",
                "user": user}),
                status=200
            )
        else:
            return Response(
                response=json.dumps({"message":"User not found",
                "user": "False"}),
                status=200
            )
    except Exception as e:
        print('********')
        print(e)
        print('********')
        return Response(
            response=json.dumps({"message":"Error getting user"}),
            status=500
        )

@app.route("/users/<user_id>", methods = ["PUT"])
def _update_appl_user(user_id):
    try:
        user = user_info(request)
        user = {u:v for u, v in user.items() if v is not False}
        for k, v in user.items():
            db.users.update_one({"USER": user_id}, {"$set": {"USER.$."+k: v}})
        return Response(
            response=json.dumps({"message":"User updated successfully",
            "id": str(user_id)}),
            status=200
        )
    except Exception as e:
        print('********')
        print(e)
        print('********')
        return Response(
            response=json.dumps({"message":"Error updating user"}),
            status=500
        )

@app.route("/users/<user_id>", methods = ["DELETE"])
def _delete_appl_user(user_id):
    try:
        db.users.update_one({"USER": user_id}, {"$pull": {"USER": {"id": user_id}}})
        return Response(
            response=json.dumps({"message":"User deleted successfully",
            "id": str(user_id)}),
            status=200
        )
    except Exception as e:
        print('********')
        print(e)
        print('********')
        return Response(
            response=json.dumps({"message":"Error deleting user"}),
            status=500
        )

#skill
@app.route("/skills", methods = ["POST"])
def _create_skill():
    try:
        skill = skill_info(request)
        db.users.update_one({"SKILL": skill["SKILL"]}, {"$set": {"SKILL": skill}})
        return Response(
            status=200,
            response=json.dumps({"message":"Skill created successfully",
            "skill": skill["SKILL"]})
        )
    except Exception as e:
        print('********')
        print(e)
        print('********')
        return Response(
            response=json.dumps({"message":"Error creating skill"}),
            status=500
        )

@app.route("/skills/<applicant_id>", methods = ["GET"])
def _get_skill(applicant_id):
    try:
        skill = db.users.find_one({"APPLICANTID": applicant_id}, {"SKILL": 1})
        skill = [json_util.dumps(skill) for skill in list(skill["SKILL"])]
        if skill:
            return Response(
                response=json.dumps({"message":"Skill found",
                "skill": skill}),
                status=200
            )
        else:
            return Response(
                response=json.dumps({"message":"Skill not found",
                "skill": "False"}),
                status=200
            )
    except Exception as e:
        print('********')
        print(e)
        print('********')
        return Response(
            response=json.dumps({"message":"Error getting skill"}),
            status=500
        )

@app.route("/skills/<skill_id>", methods = ["PUT"])
def _update_skill(skill_id):
    try:
        skill = skill_info(request)

        skill = {u:v for u, v in skill.items() if v is not False}
        for k, v in skill.items():
            db.users.update_one({"SKILL": skill_id}, {"$set": {"SKILL.$."+k: v}})
        return Response(
            response=json.dumps({"message":"Skill updated successfully",
            "id": str(skill_id)}),
            status=200
        )
    except Exception as e:
        print('********')
        print(e)
        print('********')
        return Response(
            response=json.dumps({"message":"Error updating skill"}),
            status=500
        )

@app.route("/skills/<skill_id>", methods = ["DELETE"])
def _delete_skill(skill_id):
    try:
        db.users.update_one({"SKILL": skill_id}, {"$pull": {"SKILL": {"id": skill_id}}})
        return Response(
            response=json.dumps({"message":"Skill deleted successfully",
            "id": str(skill_id)}),
            status=200
        )
    except Exception as e:
        print('********')
        print(e)
        print('********')
        return Response(
            response=json.dumps({"message":"Error deleting skill"}),
            status=500
        )


