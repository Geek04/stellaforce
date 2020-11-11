import json

from cryptography.fernet import Fernet
import jsonschema

from .interfaces import IDecryptor


class JSONFernetDecryptor(IDecryptor):
    fernet_instance: Fernet
    schema: dict

    def __init__(self, fernet_instance: Fernet, schema: dict = None):
        self.fernet_instance = fernet_instance
        self.schema = schema or {}

    def decrypt(self, file_path: str) -> dict:
        json_data: dict

        with open(file_path, "rb") as target_file:
            encrypted_data = target_file.read()
            decrypted_data = self.fernet_instance.decrypt(encrypted_data)
            jsonschema.validate(instance=decrypted_data, schema=self.schema)
            json_data = json.loads(decrypted_data)

        return json_data
