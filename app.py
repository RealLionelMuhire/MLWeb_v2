#!/usr/bin/python3
from flask import Flask, render_template

app = Flask(__name__)
JOBS = [
{
  'id': 1,
  'title': 'Data Analyst',
  'location': 'Kigali, Gasabo',
  'salary': 'RWF 450,000'
},
  {
  'id': 2,
  'title': 'IT Helpdesk',
  'location': 'Kigali, Kicukiro',
  'salary': 'RWF 510,000'
},
  {
  'id': 3,
  'title': 'Front end',
  'location': 'Remote',
  'salary': 'RWF 450,000'
},
{
  'id': 4,
  'title': 'DevOps Engineer',
  'location': 'Remote',
}
]
@app.route("/")
def hello_world():
  return render_template('home.html', jobs=JOBS, company_name = "ML Careers (Learning Purpose version)")


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
