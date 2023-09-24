#!/usr/bin/python3
from sqlalchemy import create_engine, text

db_connect_str = "mysql+pymysql://l0atw3ej02z160cz3s5c:pscale_pw_QJkQPFgBVmSOw5FlVSmkf1GCjEEQeSd38JWuAfJwTN0@aws.connect.psdb.cloud/ml_careers?charset=utf8mb4"

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
