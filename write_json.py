import json
 
def write_to_json(filename, dicts):
    with open(filename, 'w') as outfile:
        json.dump(dicts, outfile)
    return dicts

list_of_stud = [
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

students = {}
i = 1

for student in list_of_stud:
    students[i] = {}
    students[i]["name"] = student["name"]
    students[i]["major"] = student["major"]
    students[i]["uni"] = student["uni"]
    i+=1

import json

with open('test_json.json', 'w') as outfile:
    json.dump(students, outfile)
