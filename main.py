from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
  {
    'id': 1 ,
    'title': "FrondEnd Engineer",
    'location': "Melbourne, VIC",
    'salary': "$ 100,000",
  },
  {
    'id': 2,
    'title': "BackEnd Engineer",
    'location': "Brisbane, QLD",
    
  },
  {
    'id': 3,
    'title': "Data Analyst",
    'location': "Sydney, NSW",
    'salary': "$ 150,000",
  },
  {
    'id': 4,
    'title': "Data Scientist",
    'location': "Remote",
    'salary': "$ 180,000",
  }
]

@app.route("/")
def hello_world():
  return render_template('home.html', jobs = JOBS, company_name = 'R&D')

@app.route("/api/jobs")
def hello_r_d():
  return jsonify(JOBS)

#print(__name__)

if __name__ == "__main__" :
    app.run(host='0.0.0.0', debug=True)
#print("Hello World!!")