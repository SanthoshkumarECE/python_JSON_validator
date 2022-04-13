import json

def validateJSON(jsonData):
    try:
        json.loads(jsonData)
    except ValueError as err:
        return False
    return True

InvalidJsonData = """{   
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
isValid = validateJSON(InvalidJsonData)

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
isValid = validateJSON(validJsonData)

print("Given JSON string is Valid", isValid)