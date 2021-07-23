from __future__ import annotations
import typing as t
from abc import ABCMeta, abstractmethod
from pymenu.context import Context
from pymenu.helpers import protect
from pymenu.console import Console
from pymenu.listener import Listener


class Page:

    __metaclass__ = protect('print', 'item', 'back')

    def __init__(self, context: t.Type[Context]):
        self.context: t.Type[Context] = context
        self.items: t.List[t.Type[Item]] = []

    def build(self):
        raise NotImplementedError(
            f'You need to override "build" method in {self.__class__.__name__} class.')

    def listen(self, inputdata: str):
        pass  # TODO: make a listener class with "on" list

    def item(self, label: t.Optional[str] = None, on: t.Tuple[str] = (), action: t.Optional[t.Callable] = None):
        action = self.action if action is None else action
        self.print(label)

    def back(self, label: t.Optional[str] = None, on: t.Tuple[str] = ()) -> None:
        def _back():
            pass
        self.item(label, on, action=_back())

    def printer(self, *args, **kwargs) -> None:
        print(*args, **kwargs)

    def print(self, *args, **kwargs) -> None:
        self.printer(*args, **kwargs)


class PageBuilder:
    def __init__(self, pageclass: t.Type[Page], context: t.Type[Context]):
        self.pageclass: t.Type[Page] = pageclass
        self.context: t.Type[Context] = context

    def build(self):
        Console.clear()
        page = self.pageclass(self.context)
        page.build()
        page.listen(Console.listen())


class Item(Listener):
    def __init__(self, label: t.Optional[str] = None, on: t.Tuple[str] = (), action: t.Optional[t.Callable] = None):
        super().__init__(on, action)
        self.label: t.Optional[str] = label