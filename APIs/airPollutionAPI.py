import json
from Utils import schemaValidator
from Utils.dataValidator import validateJsonData
import requests as requests
from API_Schema.airPollution_Schema import schema
from API_Response_Data.airPollution_data import dataAPI
from config import *

uri = "/2.5/air_pollution?lat=33.684&lon=73.047&appid="
url = baseURL + uri + apiKey
print(url)


def Air_Pollution_API():
    response = requests.get(url)
    res = json.dumps(response.json(), indent=4)
    res = str(res)
    res = json.loads(res)
    print("Response Body : ", res)

    isValidateSchema = schemaValidator.validateJson(res, schema)
    print("Schema Validation : ", isValidateSchema)

    isValidateSchemaData = validateJsonData(res, dataAPI)
    assert isValidateSchema and isValidateSchemaData == True