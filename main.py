from flask import Flask, render_template, jsonify, request
from database import load_jobs_from_db, load_job_from_db

app = Flask(__name__)


@app.route("/")
def hello_world():
  jobs_list = load_jobs_from_db()
  return render_template('home.html', jobs=jobs_list)


@app.route("/api/jobs")
def hello_r_d():
  jobs_list = load_jobs_from_db()
  return jsonify(jobs_list)


@app.route("/job/<id>")
def show_job(id):
  job = load_job_from_db(id)
  if not job:
    return "Not Found 404"
  return render_template('jobpage.html', job=job)


@app.route("/job/<id>/apply", methods=['post'])
def apply_to_job(id):
  app_form = request.form
  job = load_job_from_db(id)
  # job_id = int(id)
  # print(job['id'])
  # add_application_form_to_db(job['id'], app_form)
  #print(1)
  return render_template('app_form_submitted.html', app_form=app_form, job=job)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
