import json

import jsonschema  # type: ignore
from cryptography.fernet import Fernet

from .interfaces import DecryptorProtocol


class JSONSupport:
    """
    Class for jsonschema validation support for any DecryptorProtocol realization.
    """
    schema: dict

    def _process_json(self, data: bytes) -> dict:
        jsonschema.validate(instance=data, schema=self.schema)
        json_dict = json.loads(data)
        return json_dict


class JSONFernetDecryptor(DecryptorProtocol, JSONSupport):
    """
    Realization of DecryptorProtocol.
    Uses cryptography.fernet.Fernet as a cryptographic engine
    and JSON as a file serialization standard.
    """
    fernet_instance: Fernet

    def __init__(self, fernet_instance: Fernet, schema: dict = None):
        """
        :param fernet_instance: Instance of Fernet class.
        :type fernet_instance: Fernet
        :param schema: Target JSON schema.
        :type schema: dict
        """
        self.fernet_instance = fernet_instance
        self.schema = schema or {}

    def decrypt(self, file_path: str) -> dict:
        """
        JSON/Fernet decryption method.

        :param file_path: A path to a file to be decrypted.
        :type file_path: str
        :return: Returns decrypted data in specified format.
        :rtype: dict
        """
        json_data: dict
        with open(file_path, "rb") as target_file:
            encrypted_data = target_file.read()
            decrypted_data = self.fernet_instance.decrypt(encrypted_data)
            json_data = self._process_json(decrypted_data)

        return json_data

