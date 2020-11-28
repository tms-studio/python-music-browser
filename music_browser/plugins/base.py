import abc
from typing import Set


class Plugin(abc.ABC):
    @abc.abstractproperty
    def known_fields(self) -> Set[str]:
        raise NotImplementedError("You must implement known_fields property of your Plugin")

    @abc.abstractmethod
    def query(self, query_params, query_fields) -> dict:
        raise NotImplementedError("You must implement query method of your Plugin")
