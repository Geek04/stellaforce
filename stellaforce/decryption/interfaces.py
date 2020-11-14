from abc import abstractmethod
from typing import Protocol


class DecryptorProtocol(Protocol):
    """
    Abstract decryptor protocol. Use it in any decryptor realization.
    """
    @abstractmethod
    def decrypt(self, file_path: str) -> dict:
        """
        Abstract decryption method.

        :param file_path: A path to a file to be decrypted.
        :type file_path: str
        :return: Returns decrypted data in specified format.
        :rtype: dict
        """
        raise NotImplementedError

