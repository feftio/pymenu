from __future__ import annotations
import typing as t
from abc import ABC, abstractmethod
from pymenu.listener import GroupListener, Listener
from pymenu.triggers import Trigger


class ElementInterface(ABC):
    @abstractmethod
    def render(self) -> None:
        pass


class Element(ElementInterface, Listener):
    pass


class GroupElement(ElementInterface, GroupListener):
    def __init__(self, childs: t.Tuple[ElementInterface]):
        self.childs = childs


class Group(GroupElement):
    def __init__(self, *childs: t.Tuple[ElementInterface]):
        super().__init__(childs=childs)

    def render(self) -> None:
        for element in self.childs:
            element.render()


class Item(Element):
    def __init__(self, label: str = '', action: t.Optional[t.Callable] = None, triggers: t.Optional[Trigger] = None):
        self.label: str = label
        self.listener(action, triggers)

    def render(self) -> None:
        print(self.label)


class Back(Item):
    def __init__(self, label: str, triggers: t.Optional[t.Tuple[Trigger]] = None):
        super().__init__(label, self._action, triggers)

    def _action(self) -> None:
        pass


class Hidden(Element):
    def __init__(self, action: t.Optional[t.Callable] = None, triggers: t.Optional[t.Tuple[Trigger]] = None):
        self.listener(action, triggers)

    def render(self) -> None:
        pass
