from sqlalchemy import create_engine,text
import os
db_connection_string = os.environ['DB_CONNECTION_STRING']
engine = create_engine(db_connection_string,connect_args={"ssl":{"ssl_ca": "/etc/ssl/cert.pem"}})


def load_jobs_from_db():
    with engine.connect() as conn:
        result = conn.execute(text("select * from joviancareers.jobs" ))
    
    result_all = result.all()
    columns = result.keys()
    jobs = []
    for row in result_all:
        jobs.append(dict(zip(columns, row)))
    return jobs