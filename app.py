from re import DEBUG
from flask import Flask,render_template

app = Flask(__name__)

JOBS = [
  {
  'id' : 1,
  'title' : "Data Analyst",
  'Location' : "Bengaluru",
  'Salary' : "10,00,000"  
},
{
  'id' : 2,
  'title' : "Data Scientist",
  'Location' : "Bengaluru ,Pune",
  'Salary' : "10,50,000"
},
{
  'id' : 3,
  'title' : "Data Analyst intern",
  'Location' : "Remote",
  'Salary' : "10,000"
},
{
  'id' : 4,
  'title' : "Machine Learning Engineer",
  'Location' : "Pune",
  'Salary' : "13,00,000"
}
]

@app.route('/')
def hello_world():
  return render_template('home.html', jobs = JOBS)

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug= True)

