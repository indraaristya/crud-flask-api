import json

with open('test_json.json', 'r') as f:
    students = json.load(f)

for i in range(1, len(students)+1):
    print(students[str(i)]["name"])