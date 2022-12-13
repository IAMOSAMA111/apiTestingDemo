schema = {
    "$schema": "http://json-schema.org/draft-06/schema#",
    "$ref": "#/definitions/Welcome5",
    "definitions": {
        "Welcome5": {
            "type": "object",
            "additionalProperties": False,
            "properties": {
                "coord": {
                    "$ref": "#/definitions/Coord"
                },
                "list": {
                    "type": "array",
                    "items": {
                        "$ref": "#/definitions/List"
                    }
                }
            },
            "required": [
                "coord",
                "list"
            ],
            "title": "Welcome5"
        },
        "Coord": {
            "type": "object",
            "additionalProperties": False,
            "properties": {
                "lon": {
                    "type": "number"
                },
                "lat": {
                    "type": "number"
                }
            },
            "required": [
                "lat",
                "lon"
            ],
            "title": "Coord"
        },
        "List": {
            "type": "object",
            "additionalProperties": False,
            "properties": {
                "main": {
                    "$ref": "#/definitions/Main"
                },
                "components": {
                    "type": "object",
                    "additionalProperties": {
                        "type": "number"
                    }
                },
                "dt": {
                    "type": "integer"
                }
            },
            "required": [
                "components",
                "dt",
                "main"
            ],
            "title": "List"
        },
        "Main": {
            "type": "object",
            "additionalProperties": False,
            "properties": {
                "aqi": {
                    "type": "integer"
                }
            },
            "required": [
                "aqi"
            ],
            "title": "Main"
        }
    }
}
