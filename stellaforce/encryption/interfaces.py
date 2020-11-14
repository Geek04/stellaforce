from abc import abstractmethod
from typing import Protocol


class EncryptorProtocol(Protocol):
    @abstractmethod
    def encrypt(self, file_path: str) -> bytes:
        raise NotImplementedError
