import jsonschema
from jsonschema import *


def validateJson(jsonData, schemaType):
    try:
        validate(instance=jsonData, schema=schemaType)
    except jsonschema.exceptions.ValidationError as err:
        print(err)
        return False
    return True
