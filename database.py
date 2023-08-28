#!/usr/bin/python
from sqlalchemy import create_engine, text

db_connect_str = "mysql+pymysql://u46f7jz7673tgk7ejewi:pscale_pw_meb5CG2GCsHJH8spxW1PYxV9AWXnQcJJQ5KiZ5IAKGq@aws.connect.psdb.cloud/ml_career?charset=utf8mb4"

engine = create_engine(
    db_connect_str,
    connect_args={
        "ssl": {
            "ssl_ca": "/etc/ssl/cert.pem"
        }
    }
)

print("DB Connection String:", db_connect_str)