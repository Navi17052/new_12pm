import json

# Python data (dictionary)
data = {
    "name": "Naveen",
    "age": 25,
    "is_student": False,
    "subjects": ["Math", "Science"]
}
json_data = json.dumps(data)

print(json_data)