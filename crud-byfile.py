from flask import Flask
from flask_restful import Api, Resource, reqparse
import json
import write_json as wj
import read_json as rj

app = Flask(__name__)
api = Api(app)

#read json file to dict
students = rj.read_from_json("test_json.json")

class Student(Resource):
    def get(self, name):
        for i in range(1, len(students)+1):
            if (name == students[str(i)]["name"]):
                return students[str(i)], 200
        return "User not found", 404
    
    def post(self, name):
        parser = reqparse.RequestParser()
        parser.add_argument("major")
        parser.add_argument("uni")
        args = parser.parse_args()

        for i in range(1, len(students)+1):
            if (name == students[str(i)]["name"]):
                return "User with name {} already exist.".format(name), 400

        next_s = str(len(students)+1)
        students[next_s] = {}
        students[next_s]["name"] = name
        students[next_s]["major"] = args["major"]
        students[next_s]["uni"] = args["uni"]
        wj.write_to_json("test_json.json", students)
        return students[next_s], 201

    def put(self, name):
        parser = reqparse.RequestParser()
        parser.add_argument("major")
        parser.add_argument("uni")
        args = parser.parse_args()

        for i in range(1, len(students)+1):
            if (name == students[str(i)]["name"]):
                students[str(i)]["major"] = args["major"]
                students[str(i)]["uni"] = args["uni"]
                return students[str(i)], 201
        
    def delete(self, name):
        for i in range(1, len(students)+1):
            if (name == students[str(i)]["name"]):
                students.pop(str(i))
                wj.write_to_json("test_json.json", students)
                return "{} is deleted.".format(name), 200
        return "No student named {}.".format(name), 404

api.add_resource(Student, "/stud/<string:name>")
app.run(debug=True)
