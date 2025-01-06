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

            return dict(rows[0])
    '''print("type(result):", type(result))    
    result_all = result.mappings().all()
    print("type(result.mappings().all()):", type(result_all))
    
    first_result = result_all[0]
    print("type(first_result):", type(first_result))
    
    first_result_dict = dict(first_result)
    print("type(first_result_dict):", type(first_result_dict))
    print(first_result_dict)'''
    #result = conn.execute(text("SELECT * FROM Computer_Science_Jobss;"))
    #print(result.all())
