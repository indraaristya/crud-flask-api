from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

students = [
    {
        "name" : "Indra",
        "major" : "Informatics",
        "uni" : "Telkom"
    },
    {
        "name" : "Dimdum",
        "major" : "Industrial",
        "uni" : "Telkom"
    },
    {
        "name" : "Yudha",
        "major" : "VCD",
        "uni" : "Telkom"
    }
]

class Student(Resource):
    def get(self, name):
        for student in students:
            if (name == student["name"]):
                return student, 200
        return "User not found", 404

    def post(self, name):
        parser = reqparse.RequestParser()
        parser.add_argument("major")
        parser.add_argument("uni")
        args = parser.parse_args()

        for student in students:
            if (name == student["name"]):
                return "User with name {} already exist".format(name), 400
        
        student = {
            "name" : name,
            "major" : args["major"],
            "uni" : args["uni"]
        }
        students.append(student)
        return student, 201

    def put(self, name):
        parser = reqparse.RequestParser()
        parser.add_argument("major")
        parser.add_argument("uni")
        args = parser.parse_args()

        for student in students:
            if (name == student[name]):
                student["major"] = args["major"]
                student["uni"] = args["uni"]
                return student, 200

        student = {
            "name" : name,
            "major" : args["major"],
            "uni" : args["uni"]
        }
        students.append(student)
        return student, 201

    def delete(self, name):
        global students
        students = [student for student in students if student["name"] != name]
        return "{} is deleted.".format(name), 200


api.add_resource(Student, "/stud/<string:name>")
app.run(debug=True)