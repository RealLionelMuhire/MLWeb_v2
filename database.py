#!/usr/bin/python
from sqlalchemy import create_engine

db_connect_str = "mysql+pymysql://w9947rumlo8lkhsvho06:pscale_pw_iddkxaScHFdWZTCzPeRHCJNtOJHhNq2zUZ6CoAuPWfP@aws.connect.psdb.cloud/ml_career?charset=utf8mb4"

engine = create_engine(
    db_connect_str,
    connect_args={
        "ssl": {
            "ssl_ca": "/etc/ssl/cert.pem"
        }
    }
)
