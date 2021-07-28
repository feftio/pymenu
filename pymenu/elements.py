from __future__ import annotations
from pymenu.triggers import Trigger
import typing as t
from pymenu.listener import Listener


class Element(Listener):
    def render(self) -> None:
        raise NotImplementedError(
            f'You need to override "render" method in {self.__class__.__name__} class.')


class Item(Element):
    def __init__(self, label: str, action: t.Callable, triggers: t.Tuple[Trigger]):
        self.label: t.Optional[str] = label
        self.listener(action, triggers)

    def render(self) -> None:
        print(self.label)


class Group(Element):
    def __init__(self, *elements: Element):
        self.elements: t.Tuple[Element] = elements

    def render(self) -> None:
        for element in self.elements:
            element.render()


class Back(Item):
    def __init__(self, label: str, triggers: t.Tuple[Trigger]):
        super().__init__(label, self._action, triggers)

    def _action(self) -> None:
        pass


class Hidden(Element):
    def __init__(self, action: t.Callable, triggers: t.Tuple[Trigger]):
        self.listener(action, triggers)

    def render(self) -> None:
        pass
