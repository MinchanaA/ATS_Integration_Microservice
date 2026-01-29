import os
from supabase import create_client, Client

class SupabaseATSClient:
    def __init__(self):
        self.url = os.environ.get("SUPABASE_URL")
        self.key = os.environ.get("SUPABASE_KEY")
        self.mock_mode = not (self.url and self.key)
        
        if self.mock_mode:
            print("WARNING: No Supabase credentials found. Running in MOCK MODE.")
        else:
            self.supabase: Client = create_client(self.url, self.key)

    def fetch_jobs(self):
        if self.mock_mode:
            return [
                {"id": "1", "title": "Software Engineer", "location": "Remote", "status": "OPEN", "external_url": "http://example.com/jobs/1"},
                {"id": "2", "title": "Product Designer", "location": "New York", "status": "DRAFT", "external_url": "http://example.com/jobs/2"}
            ]
        
        response = self.supabase.table("jobs").select("*").execute()
        return response.data

    def create_candidate(self, candidate_data):
        if self.mock_mode:
            return {"id": "new-cand-123", "name": candidate_data["name"]}
        
        payload = {
            "name": candidate_data["name"],
            "email": candidate_data["email"],
            "phone": candidate_data["phone"],
            "resume_url": candidate_data["resume_url"],
            "job_id": candidate_data["job_id"]
        }
        
        response = self.supabase.table("candidates").insert(payload).execute()
        return response.data[0] if response.data else {}

    def fetch_applications(self, job_id):
        if self.mock_mode:
            return [
                {"id": "app-1", "name": "Alice Smith", "email": "alice@example.com", "status": "APPLIED"}
            ]
        
        response = self.supabase.table("candidates").select("*").eq("job_id", job_id).execute()
        return response.data
