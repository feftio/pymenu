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

    def item(self, label: t.Optional[str] = None, on: t.Tuple[str] = (), trigger: t.Optional[t.Callable] = None):
        trigger = self.trigger if trigger is None else trigger
        self.printer(label)

    def printer(self, *args, **kwargs):
        print(*args, **kwargs)


class PageBuilder:
    def __init__(self):
        pass
