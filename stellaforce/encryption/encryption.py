from cryptography.fernet import Fernet

from stellaforce.utils import JSONLoader
from .interfaces import EncryptorProtocol


class JSONFernetEncryptor(EncryptorProtocol):
    """
    Realization of EncryptorProtocol.
    Uses cryptography.fernet.Fernet as a cryptographic engine
    and JSON as a file serialization standard.
    """
    fernet_instance: Fernet
    schema: dict

    def __init__(self, fernet_instance: Fernet, schema: dict = None):
        """
        :param fernet_instance: Instance of Fernet class.
        :type fernet_instance: Fernet
        :param schema: Target JSON schema.
        :type schema: dict
        """
        self.fernet_instance = fernet_instance
        self.schema = schema or {}

    def encrypt(self, file_path: str) -> bytes:
        """
        JSON/Fernet encryption method.

        :param file_path: A path to a file to be encrypted.
        :type file_path: str
        :return: Returns raw encrypted data.
        :rtype: bytes
        """
        token: bytes
        with JSONLoader(file_path, self.schema) as target_file:
            raw_data = target_file.read()
            token = self.fernet_instance.encrypt(raw_data)

        return token
