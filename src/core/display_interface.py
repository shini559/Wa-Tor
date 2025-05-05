from abc import ABCMeta, abstractmethod


class DisplayInterface:
    def __init__(self):
        super().__init__(self)

    @abstractmethod
    def start(self):
        raise ValueError("NotImplementedException start")

    @abstractmethod
    def update(self):
        raise ValueError("NotImplementedException update")

    @abstractmethod
    def pause(self):
        raise ValueError("NotImplementedException pause")

    @abstractmethod
    def reset(self):
        raise ValueError("NotImplementedException reset")

    @abstractmethod
    def proccess(self):
        raise ValueError("NotImplementedException proccess")