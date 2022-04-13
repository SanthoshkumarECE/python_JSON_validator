import json
import jsonschema
from jsonschema import validate

employeeschema={
"$schema": "http://json-schema.org/draft-04/schema#",
    "type": "object",
    "properties": {
        "employee": {
            "type": "array",
            "items": [
                {  "type":"object",
                    "properties":{
                        "day":{
                        "type":"string",
                        "enum":["SU","MO","TU","WE","TH","FR","SA"]
                        },
                        "id": {
                            "type": "integer"
                        },
                        "name": {
                            "type": "string"
                        },"home phone": {
                            "type": "integer"
                        },"work phone": {
                            "type": "integer"
                        },
                        "cell phone": {
                            "type": "integer"
                        },
                        "govt id": {
                            "type": "integer"
                        },
                        "birth date": {
                            "type": "string"
                        }
                    },
                    "required": [
                        "id",
                        "name"
                    ],
                    "anyOf":[
                        {"required":["home phone"]},{"required":["cell phone"]},{"required":["work phone"]}
                    ],
                    "oneOf":[{"required":["birth date"]},{"required":["govt id"]}]
                }
]}}}

def validation(Data):
    try:
        validate(instance=Data,schema=employeeschema)
    except jsonschema.exceptions.ValidationError as err:
        return False
    return True

file=open('data.json')
validdata=json.load(file)
print(validation(validdata))
file.close()
file1=open('invaliddata.json')
invaliddata=json.load(file1)
print(validation(invaliddata))