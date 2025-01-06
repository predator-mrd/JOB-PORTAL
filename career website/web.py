from flask import Flask, render_template, jsonify, request
from sqlalchemy import create_engine, text

db_connection_string = "mysql+pymysql://root:Dev%401234@127.0.0.1:3306/CS_JOBS?charset=utf8mb4"

engine = create_engine(
    db_connection_string,
    connect_args={
        "ssl": {
            "ssl_ca": "/etc/ssl/cert.pem"
        }
    }
)

def load_jobs_from_db():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM Computer_Science_Jobss"))
        jobs = []
        for row in result.mappings().all():
            jobs.append(dict(row))
        return jobs

def load_job_from_db(JobID):
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM Computer_Science_Jobss WHERE JobID = :job_id"), {"job_id": JobID})
        job = result.mappings().first()
        if job:
            return dict(job)
        else:
            return None

app = Flask(__name__)

@app.route("/")
def home():
    jobs = load_jobs_from_db()
    message = "Welcome to the Job Portal!"
    return render_template("home.html", message=message, jobs=jobs)

@app.route("/jobs/<JobID>")
def show_job(JobID):
    job = load_job_from_db(JobID)
    if job:
        return render_template("jobpage.html", job=job)
    else:
        return jsonify({"error": "Job not found"}), 404

@app.route("/jobs/<JobID>/apply", methods=['POST'])
def apply_to_job(JobID):
    data = request.form
    # Process the application data if needed
    return render_template('application_submitted.html', application=data)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)













