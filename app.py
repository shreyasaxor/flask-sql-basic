from flask import Flask, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
SQLALCHEMY_TRACK_MODIFICATIONS = False

db = SQLAlchemy(app)


class students(db.Model):
   id = db.Column('student_id', db.Integer, primary_key = True)
   name = db.Column(db.String(100))
   city = db.Column(db.String(50))
   addr = db.Column(db.String(200))
   pin = db.Column(db.String(10))

def __init__(self, name, city, addr,pin):
   self.name = name
   self.city = city
   self.addr = addr
   self.pin = pin

@app.route('/shreyas')
def hello_world():
   # try:
   #    student = students(name = 'shreyas',city = 'banglore',addr='rajajinagar',pin='4443')
   #    db.session.add(student)
   #    db.session.commit()
   # except:
   #    import sys
   #    print(sys.exc_info())
   add =[]

   for x in students.query.all():
      y= x.__dict__
      del y['_sa_instance_state']
      add.append(y)


   print(add)

   return make_response(jsonify({'tasks': add}), 200)







if __name__ == '__main__':
   app.run(debug=True)
