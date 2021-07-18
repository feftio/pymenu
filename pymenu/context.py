from __future__ import annotations
import typing as t


class Context:
    def __init__(self) -> None:
        pass

    @property
    def page(self) -> str:
        return 'routemap'


class ContextManager:
    def __init__(self, context: t.Type[Context]):
        self.context: t.Type[Context] = context


if __name__ == '__main__':
    context_manager = ContextManager()
