#  ATS Integration Microservice (Python + Serverless)

A high-performance, serverless microservice built with **Python** and the **Serverless Framework**. This service provides a unified API interface for an Applicant Tracking System (ATS), backed by **Supabase (PostgreSQL)**.

##  Features

- **Unified API**: Standardized endpoints for Jobs, Candidates, and Applications.
- **Serverless Architecture**: Optimized for AWS Lambda with low latency and automatic scaling.
- **Mock Mode**: Built-in testing mode that works instantly without external dependencies.
- **Robust Error Handling**: Clean JSON error responses for seamless frontend integration.
- **Modern Tech Stack**: Python 3.9+, Supabase (PostgreSQL), and Serverless Offline.

---

##  Tech Stack

- **Lanuage**: Python 3.9+
- **Infrastructure**: Serverless Framework (v3)
- **Database**: Supabase (PostgreSQL)
- **Deployment**: AWS Lambda (via Serverless)
- **Local Dev**: `serverless-offline`

---

##  Quick Start (Local Development)

### 1. Clone & Install Dependencies
```bash
# Install serverless plugins
npm install

# Install python dependencies
pip install -r requirements.txt
```

### 2. Configure Environment
Create a `.env` file in the root directory:
```env
SUPABASE_URL=https://your-project.supabase.co
SUPABASE_KEY=your-service-role-key
```

### 3. Database Schema (Supabase SQL Editor)
Run the following SQL in your Supabase dashboard to initialize the data structure:

```sql
-- Create Jobs table
CREATE TABLE jobs (
  id uuid DEFAULT gen_random_uuid() PRIMARY KEY,
  title text NOT NULL,
  location text DEFAULT 'Remote',
  status text CHECK (status IN ('OPEN', 'CLOSED', 'DRAFT')) DEFAULT 'DRAFT',
  external_url text,
  created_at timestamptz DEFAULT now()
);

-- Create Candidates table
CREATE TABLE candidates (
  id uuid DEFAULT gen_random_uuid() PRIMARY KEY,
  name text NOT NULL,
  email text NOT NULL,
  phone text,
  resume_url text,
  job_id uuid REFERENCES jobs(id),
  status text CHECK (status IN ('APPLIED', 'SCREENING', 'REJECTED', 'HIRED')) DEFAULT 'APPLIED',
  created_at timestamptz DEFAULT now()
);
```

### 4. Launch Service
```bash
npx serverless@3 offline
```
The API will be available at `http://localhost:3000/dev/`.

---

##  API Reference

### Jobs
`GET /jobs`
- **Description**: Retrieves a list of all open positions.
- **Response**: `200 OK`
```json
[
  {
    "id": "uuid",
    "title": "Software Engineer",
    "location": "Remote",
    "status": "OPEN",
    "external_url": "https://..."
  }
]
```

### Candidates
`POST /candidates`
- **Description**: Creates a new candidate and links them to a specific job.
- **Payload**:
```json
{
  "name": "Jane Doe",
  "email": "jane@example.com",
  "phone": "123-456-7890",
  "resume_url": "https://...",
  "job_id": "uuid"
}
```

### Applications
`GET /applications?job_id=...`
- **Description**: Lists all candidate applications for a specific job ID.
- **Response**: `200 OK`
```json
[
  {
    "id": "uuid",
    "candidate_name": "Jane Doe",
    "email": "jane@example.com",
    "status": "APPLIED"
  }
]
```

---

##  Mock Mode
If you run the service without a `.env` file, it will automatically enter **Mock Mode**. This allows developers to test the API endpoints immediately with realistic sample architecture.

---

*Certified ATS Integration Solution | 2026*
