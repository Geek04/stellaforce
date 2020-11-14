from abc import abstractmethod
from typing import Protocol


class EncryptorProtocol(Protocol):
    """
    Abstract encryptor protocol. Use it in any decryptor realization.
    """
    @abstractmethod
    def encrypt(self, file_path: str) -> bytes:
        """
        Abstract encryption method.

        :param file_path: A path to a file to be encrypted.
        :type file_path: str
        :return: Returns raw encrypted data.
        :rtype: bytes
        """
        raise NotImplementedError
