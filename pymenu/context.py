from __future__ import annotations
from pymenu.holder import Holder
import typing as t


class Context:
    def __init__(self) -> None:
        pass

    @property
    def page(self) -> str:
        return 'routemap'


class ContextThrower:
    def __init__(self, context: t.Type[Context]):
        self.context: t.Type[Context] = context

    def throw(self, holder: t.Type[Holder]) -> None:
        pass


if __name__ == '__main__':
    context_manager = ContextThrower().throw()
