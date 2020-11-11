from typing import BinaryIO
import json

import jsonschema  # type: ignore


class JSONLoader:
    target_file: BinaryIO

    def __init__(self, filepath, schema: dict):
        self.schema = schema
        self.target_file = open(filepath, "rb")

        self.validate_json()

    def validate_json(self):
        json_data = json.load(self.target_file)
        jsonschema.validate(instance=json_data, schema=self.schema)

        self.target_file.seek(0)

    def __enter__(self):
        return self.target_file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.target_file.close()
