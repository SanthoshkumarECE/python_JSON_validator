import jsonschema
from jsonschema import validate

employeeschema={
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
                            "type": "string"
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

def validation(jsonData):
    try:
        validate(instance=jsonData,schema=employeeschema)
    except jsonschema.exceptions.ValidationError as err:
        return False
    return True

InvalidJsonData = """
    "employee":
           [
		   {"id":1,
		   "name":"kumar",
		   "cell phone":1233455554,
		   "birth date":"16/02/2003",
            "leave taken":"MO"
           }{"id":2,
		   "name":"santhosh",
		   "home phone":1233765554,
		   "birth date":"15/01/2001",
			"leave taken":
             }
            ]
}"""
isValid = validation(InvalidJsonData)

print("Given JSON string is Valid", isValid)

validJsonData = """{   
    "employee":
           [
		   {"id":1,
		   "name":"kumar",
		   "cell phone":1233455554,
		   "birth date":"16/02/2003",
            "leave taken":"MO"
           },{"id":2,
		   "name":"santhosh",
		   "home phone":1233765554,
		   "birth date":"15/01/2001",
			"leave taken":"SO"
             }
            ]
}"""
isValid = validation(validJsonData)

print("Given JSON string is Valid", isValid)