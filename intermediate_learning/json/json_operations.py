import json

person = {"name": "John", "age": 30, "city": "New York", "hasChildren": False, "titles": ["engineer", "programmer"]}
print(person)

person_json = json.dumps(person)
print(person_json)

person_json2 = json.dumps(person, indent=4, separators=("; ", "= "), sort_keys=True)
print(person_json2)

#Convert python object to a json file
with open("json/person.json", 'w') as output_file:
  json.dump(person, output_file, indent=4, sort_keys=True)

#Convert a json file to a python object
with open("json/example.json", "r") as input_file:
  person2 = json.load(input_file)
  print(json.dumps(person2, indent=4))

#Convert from json string to python object
person_json_string = """
{
    "age": 30, 
    "city": "New York",
    "hasChildren": false, 
    "name": "John",
    "titles": [
        "engineer",
        "programmer"
    ]
}
"""
person3 = json.loads(person_json_string)
print(person3)

### json.load/json.dump when working with files
### json.loads/json.dumps when loading from string or dumping in console