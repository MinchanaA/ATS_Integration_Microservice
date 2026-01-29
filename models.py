def map_job(db_job):
    """
    Standardize Supabase job to task format.
    """
    return {
        "id": str(db_job.get("id")),
        "title": db_job.get("title"),
        "location": db_job.get("location", "Remote"),
        "status": db_job.get("status", "DRAFT").upper(),
        "external_url": db_job.get("external_url")
    }

def map_application(db_candidate):
    """
    Standardize Supabase candidate to application format.
    """
    return {
        "id": str(db_candidate.get("id")),
        "candidate_name": db_candidate.get("name"),
        "email": db_candidate.get("email"),
        "status": db_candidate.get("status", "APPLIED").upper()
    }
