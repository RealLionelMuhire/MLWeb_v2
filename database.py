#!/usr/bin/python
from sqlalchemy import create_engine, text

db_connect_str = "mysql+pymysql://w369rwsxniwcadtxgpt7:pscale_pw_LxqtZbLagHT4GcTy8fr6tjQcHkKi4EJPBQ7sHOl1xeu@aws.connect.psdb.cloud/ml_careers?charset=utf8mb4"

engine = create_engine(
    db_connect_str,
    connect_args={
        "ssl": {
            "ssl_ca": "/etc/ssl/cert.pem"
        }
    }
)


def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    jobs = []
    for row in result.all():
      jobs.append({column: getattr(row, column) for column in result.keys()})
    return jobs



jobs = load_jobs_from_db()
print(jobs)
