from abc import abstractmethod, ABC


class RegexConstructorInterface(ABC):

    @abstractmethod
    def create_regex(self):
        pass





