import json

import jsonschema
from cryptography.fernet import Fernet

from .interfaces import DecryptorProtocol


class JSONSupport:
    schema: dict

    def _process_json(self, data: bytes) -> dict:
        jsonschema.validate(instance=data, schema=self.schema)
        json_dict = json.loads(data)
        return json_dict


class JSONFernetDecryptor(DecryptorProtocol, JSONSupport):
    fernet_instance: Fernet

    def __init__(self, fernet_instance: Fernet, schema: dict = None):
        self.fernet_instance = fernet_instance
        self.schema = schema or {}

    def decrypt(self, file_path: str) -> dict:
        json_data: dict
        with open(file_path, "rb") as target_file:
            encrypted_data = target_file.read()
            decrypted_data = self.fernet_instance.decrypt(encrypted_data)
            json_data = self._process_json(decrypted_data)

        return json_data

