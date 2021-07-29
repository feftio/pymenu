from __future__ import annotations
import typing as t
from pymenu.context import Context
from pymenu.console import Console
from pymenu.elements import Element
from pymenu.triggers import Trigger


class Page:
    def __init__(self, context: Context):
        self.context: Context = context

    def build(self) -> Element:
        raise NotImplementedError(
            f'You need to override "build" method in {self.__class__.__name__} class.')


class PageBuilder:
    def __init__(self):
        self.context: Context = Context()

    def build(self, pageclass: Page):
        Console.clear()
        page = pageclass(self.context)
        es = ElementSystem(page.build())
        es.render()
        es.listen(Console.read())


class ElementSystem:
    def __init__(self, root: Element):
        self.root: Element = root

    def render(self) -> None:
        self.root.render()

    def listen(self, trigger: Trigger) -> None:
        self.root.listen(trigger)
