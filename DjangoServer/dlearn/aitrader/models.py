from abc import abstractmethod, ABCMeta

class AitradeBase(mataclass=ABCMeta):
    @abstractmethod
    def split_sy5(self, **kwargs): pass

    @abstractmethod
    def create(self): pass