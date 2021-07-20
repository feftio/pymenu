from __future__ import annotations
import typing as t
from abc import ABCMeta, abstractmethod
from pymenu.context import Context


class Page(metaclass=ABCMeta):
    def __init__(self, context: t.Type[Context]):
        self.context: t.Type[Context] = context

    @abstractmethod
    def show(self):
        pass

    def trigger(self):
        pass

    def item(self):
        pass

    def printer(self, label):
        print(label)
