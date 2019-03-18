import json

def read_from_json(filename):
    with open(filename, 'r') as f:
        dicts = json.load(f)
    return dicts

with open('test_json.json', 'r') as f:
    students = json.load(f)

# for i in range(1, len(students)+1):
#     print(students[str(i)]["name"])
