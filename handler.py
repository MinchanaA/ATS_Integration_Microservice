import json
import os
from ats_client import SupabaseATSClient
from models import map_job, map_application

client = SupabaseATSClient()

def get_jobs(event, context):
    try:
        raw_jobs = client.fetch_jobs()
        standardized_jobs = [map_job(j) for j in raw_jobs]
        return {
            "statusCode": 200,
            "body": json.dumps(standardized_jobs)
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }

def create_candidate(event, context):
    try:
        body = json.loads(event.get("body", "{}"))
        required = ["name", "email", "phone", "resume_url", "job_id"]
        if not all(k in body for k in required):
            return {
                "statusCode": 400,
                "body": json.dumps({"error": "Missing required fields"})
            }
        
        candidate = client.create_candidate(body)
        return {
            "statusCode": 201,
            "body": json.dumps(candidate)
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }

def get_applications(event, context):
    try:
        params = event.get("queryStringParameters") or {}
        job_id = params.get("job_id")
        if not job_id:
            return {
                "statusCode": 400,
                "body": json.dumps({"error": "Missing job_id parameter"})
            }
        
        raw_apps = client.fetch_applications(job_id)
        standardized_apps = [map_application(a) for a in raw_apps]
        return {
            "statusCode": 200,
            "body": json.dumps(standardized_apps)
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }
