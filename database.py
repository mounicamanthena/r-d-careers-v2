from sqlalchemy import create_engine, text
import os

database_connection_string = os.environ['DB_CONNECTION_STR']

engine = create_engine(database_connection_string,
                       connect_args={"ssl": {
                         "ssl_ca": "/etc/ssl/cert.pem",
                       }})


def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    jobs_list = []
    for row in result.all():
      jobs_list.append(row._asdict())
    return jobs_list
