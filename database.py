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


def load_job_from_db(id):
  with engine.connect() as conn:
    result = conn.execute(text(f"select * from jobs where id = {id}"))
    rows = result.all()
    if len(rows) == 0:
      return None
    else:
      return rows[0]._asdict()


#def add_application_form_to_db(job_id, app_form):
#  with engine.connect() as conn:
#    print(job_id, app_form['full_name'], app_form['email'])
#    print(type(job_id))
#    result = conn.execute(
 #     text(
  #      f"INSERT INTO 'randdcareers'.'applicationforms'  (job_id, full_name, email,linkedin_url,education, work_experience, reume_url) VALUES(:{job_id},:{app_form['full_name']},:{app_form['email']},:{app_form['linkedin_url']},:{app_form['education']},:{app_form['work_experience']},:{app_form['reume_url']})"
   #   ))
    #rows = result.all()
    #print(rows[0]._asdict())

    