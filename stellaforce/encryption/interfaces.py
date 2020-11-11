from abc import abstractmethod
from typing import Protocol


class IEncryptor(Protocol):
    @abstractmethod
    def encrypt(self, file_path: str) -> bytes:
        raise NotImplementedError
