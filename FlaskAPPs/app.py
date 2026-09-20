from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import select


app = Flask(__name__)

## Database configuration ##
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'

db = SQLAlchemy(app)

# students = [
#     {"name": "Alice", "age": 22, "major": "Computer Science"},
#     {"name": "Bob", "age": 24, "major": "Mathematics"},
#     {"name": "Charlie", "age": 21, "major": "Physics"}
# ]


## Models --> Define the database tables

class Student(db.Model):

    __tablename__ = 'students'

    id = db.Column(db.Integer, primary_key=True)   ## auto Increment 1,2,3,4...
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    major = db.Column(db.String(100), nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "age": self.age,
            "major": self.major
        }
    
class User(db.Model): 
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)   ## auto Increment 1,2,3,4...
    username = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email
        }

with app.app_context():
    db.create_all()  ## Create the tables in the database

## Home Route
@app.route('/')
def home():
    return "Welcome to the Technogeeks Flask App!"

@app.route('/Hello')
def hello():
    return "Hello, World!"

# @app.route('/user')
# def user():
#     user_info = {
#         "name": "John Doe",
#         "age": 30,
#         "email": "john.doe@example.com"
#     }
#     return jsonify(user_info)


## Student Crud Routes

# @app.route('/students', methods=['GET'] )
# def get_students():
#     return jsonify(students)

@app.route('/students', methods=['GET'])
def get_students():
    students = db.session.execute(select(Student)).scalars().all()
    return jsonify([s.to_dict() for s in students])

# @app.route('/students/<string:name>', methods=['GET'])
# def get_student(name):
#     for student in students:
#         if student['name'] == name:
#             return jsonify(student)
        
#     return jsonify({"error": "Not Found"}), 404

@app.route('/students/<int>:id', methods=['GET'])
def get_student(id):
    student = db.session.get(Student, id)
    if not student:
        return jsonify({"error": "Student Not Found"}), 404
    return jsonify(student.to_dict())


# @app.route('/students', methods=['POST'])
# def add_student():
#     data = request.get_json()

#     students.append(data)

#     return jsonify({
#         "message": "Student added successfully",
#         "student": data
#     }), 201

@app.route('/students', methods=['POST'])
def add_student():
    data = request.get_json()
    if not data or not all(k in data for k in ('name', 'age', 'major')):
        return jsonify({"error": "name, age and major are required"}), 400
    
    new_student = Student(
        id=data['id'],
        name=data['name'],
        age=data['age'],
        major=data['major']
    )

    db.session.add(new_student)
    db.session.commit()
    return jsonify(new_student.to_dict()), 201


# @app.route('/students/<string:name>', methods=['PUT'])
# def update_student(name):
#     data = request.get_json()

#     for student in students:
#         if student["name"] == name:
#             student["name"] = data["name"]

#             return jsonify(student)
        
#     return jsonify({"Error": "Not Found"}), 404

@app.route('/students/<int:id>', methods=['PUT'])
def update_student(id):
    student = db.session.get(Student, id)
    if not student:
        return jsonify({"error: Student not found"}), 404
    
    data = request.get_json()
    student.name = data.get('name', student.name)
    student.age = data.get('age', student.age)
    student.major = data.get('major', student.major)

    db.session.commit()
    return jsonify(student.to_dict())



# @app.route('/students/<string:name>', methods=['DELETE'])
# def delete_student(name):
#     for student in students:
#         if student["name"] == name:
#             students.remove(student)

#             return jsonify({
#                 "Message": "Deleted"
#             })
#     return jsonify({"Error": "Not Found"}), 404

@app.route('/students/<int:id>', methods=['DELETE'])
def delete_students(id):
    student = db.session.get(Student, id)
    if not student:
        return jsonify({"error: Student not found"}), 404
    
    db.session.delete(student)
    db.session.commit()

    return jsonify({"Message": f"{student.name} deleted successully"})
                   

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)