#!/usr/bin/python3
import os

db_connect_str = os.environ.get("DB_CONNECTION_STRING")
if db_connect_str:
    print("DB_CONNECTION_STRING is set:", db_connect_str)
else:
    print("DB_CONNECTION_STRING is not set or is set to None.")

