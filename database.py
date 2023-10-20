#!/usr/bin/python3
from sqlalchemy import create_engine, text
import os

db_connect_str = os.environ.get("DB_CONNECTION_STRING")

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
