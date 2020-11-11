from cryptography.fernet import Fernet

from stellaforce.utils import JSONLoader
from .interfaces import IEncryptor


class JSONFernetEncryptor(IEncryptor):
    fernet_instance: Fernet
    schema: dict

    def __init__(self, fernet_instance: Fernet, schema: dict = None):
        self.fernet_instance = fernet_instance
        self.schema = schema or {}

    def encrypt(self, file_path: str) -> bytes:
        token: bytes
        with JSONLoader(file_path, self.schema) as target_file:
            raw_data = target_file.read()
            token = self.fernet_instance.encrypt(raw_data)

        return token
