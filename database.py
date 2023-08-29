#!/usr/bin/python
from sqlalchemy import create_engine, text

db_connect_str = "mysql+pymysql://cya4oqn277p39qxkdkcb:pscale_pw_5KLbixJYqkmcOXSEuslIOb62gxpfApxTIhgY2dlGZ3Y@aws.connect.psdb.cloud/ml_careers?charset=utf8mb4"

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
