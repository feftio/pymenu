from __future__ import annotations
import typing as t
from pymenu.context import Context
from pymenu.console import Console
from pymenu.elements import Element, ElementInterface
from pymenu.triggers import CharsTrigger, Trigger
from rich import print


class Page:
    def __init__(self, context: Context):
        self.context: Context = context

    def print(self, *args, **kwargs) -> None:
        print(*args, **kwargs)

    def build(self) -> Element:
        raise NotImplementedError(
            f'You need to override "build" method in {self.__class__.__name__} class.')


class PageBuilder:
    def __init__(self):
        self.context: Context = Context()

    def save(self, pagename: str) -> None:
        self.context.history.append(pagename)

    def build(self, pagename: str, pageclass: Page) -> None:
        self.save(pagename)
        Console.clear()
        page = pageclass(self.context)
        es = ElementSystem(page.build())
        es.render()
        es.listen(CharsTrigger(Console.read()))


class ElementSystem:
    def __init__(self, root: ElementInterface):
        self.root: ElementInterface = root

    def render(self) -> None:
        self.root.render()

    def listen(self, trigger: Trigger) -> None:
        self.root.listen(trigger)
