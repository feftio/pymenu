from __future__ import annotations
import typing as t
from abc import ABCMeta, abstractmethod
from pymenu.context import Context


class Page(metaclass=ABCMeta):
    def __init__(self, context: t.Type[Context]):
        self.context: t.Type[Context] = context
        # if hasattr(self, 'show') and callable(getattr(self, 'show')):
        #     self.show()

    @abstractmethod
    def show(self):
        pass

# class Page:
#     def __init__(self, context: t.Type[Context]):
#         self.context: t.Type[Context] = context

#     def show(self):
#         raise NotImplementedError(
#             f'"show" method in {self.__class__.__name__} class must be overriden.')


class SelectionPage(Page):
    def show(self):
        pass
