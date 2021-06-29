from __future__ import annotations
import typing as t
from abc import ABCMeta, abstractmethod


class Page(metaclass=ABCMeta):
    def __init__(self):
        if hasattr(self, 'show') and callable(getattr(self, 'show')):
            self.show()

    @abstractmethod
    def show(self):
        pass


class DefaultPage(Page):

    def show(self):
        raise NotImplementedError(
            f'You need to override "show" method in {self.__class__.__name__} class.')


class SelectionPage(Page):
    def __init__(self):
        super().__init__()

    def show():
        pass
