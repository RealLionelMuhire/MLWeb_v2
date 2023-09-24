#!/usr/bin/python3
from sqlalchemy import create_engine, text

db_connect_str = "mysql+pymysql://kc1ukk07u0o5x67iaq1z:pscale_pw_iIaSOoDo6MPlSM84SkmJBMhP6zKQldATXdN4Agsi31N@aws.connect.psdb.cloud/ml_careers?charset=utf8mb4"

engine = create_engine(
    db_connect_str,
    connect_args={
        "ssl": {
            "ssl_ca": "/etc/ssl/cert.pem"
        }
    }
)

with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    print(result.all())
