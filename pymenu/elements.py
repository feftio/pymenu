from __future__ import annotations
import typing as t
from abc import ABC, abstractmethod
from pymenu.listener import GroupListener, Listener, ListenerInterface
from pymenu.triggers import Trigger


class ElementInterface(ListenerInterface, ABC):
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
        super().__init__(childs)

    def render(self) -> None:
        for element in self.childs:
            element.render()


class Item(Element):
    # TODO: make "label" optional.
    def __init__(self, label: t.Optional[str] = None, action: t.Optional[t.Callable] = None, triggers: t.Optional[Trigger] = None):
        self.label: t.Optional[str] = label
        self.listener(action, triggers)

    def render(self) -> None:
        if self.label is None:
            return
        print(self.label)


class Hidden(Element):
    def __init__(self, action: t.Optional[t.Callable] = None, triggers: t.Optional[t.Tuple[Trigger]] = None):
        self.listener(action, triggers)

    def render(self) -> None:
        pass


class Redirect(Item):
    def __init__(self, to: str, label: t.Optional[str] = None, triggers: t.Optional[t.Tuple[Trigger]] = None):
        super().__init__(label, self._action, triggers)
        self.to = to

    def _action(self) -> None:
        pass


class Back(Item):
    def __init__(self, label: t.Optional[str] = None, triggers: t.Optional[t.Tuple[Trigger]] = None):
        super().__init__(label, self._action, triggers)

    def _action(self) -> None:
        pass
