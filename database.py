#!/usr/bin/python
from sqlalchemy import create_engine, text

db_connect_str = "mysql+pymysql://gihvbl93lxl4ymg0fgk7:pscale_pw_mN0sEtJwl1kbgppeW3Z56AcJzPTlV5FlKpPXkYWMSAU@aws.connect.psdb.cloud/ml_careers?charset=utf8mb4"

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
