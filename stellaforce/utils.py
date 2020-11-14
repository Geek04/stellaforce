from typing import BinaryIO
import json

import jsonschema  # type: ignore


class JSONLoader:
    """
    Context manager.
    Opens a file and validates it using specified JSON schema.
    """
    target_file: BinaryIO

    def __init__(self, file_path, schema: dict):
        """
        :param file_path: A path to a file to be opened.
        :type file_path: str
        :param schema: JSON schema to be used in validation.
        :type schema: dict
        """
        self.schema = schema
        self.target_file = open(file_path, "rb")

        self._validate_json()

    def _validate_json(self):
        """
        JSON validation method. Do not use this method outside JSONLoader class.
        """
        json_data = json.load(self.target_file)
        jsonschema.validate(instance=json_data, schema=self.schema)

        self.target_file.seek(0)

    def __enter__(self):
        return self.target_file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.target_file.close()
