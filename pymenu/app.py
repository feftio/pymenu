from __future__ import annotations
import typing as t
from pymenu.page import Page


class PyMenu:

    def __init__(self, separator: t.Optional[str] = None, *args, **kwargs) -> None:
        self.callbacks: t.Dict[str, t.Callable] = {}
        self.separator: t.Optional[str] = separator

    def show(self, name: str) -> None:
        self.callbacks[name]()

    def page(self, name: str) -> t.Callable:
        def decorator(page_class: t.Type[Page]):
            return page_class
        return decorator

    def item(self, output: str, triggers: t.List[str]) -> t.Callable:
        def decorator(item_function: t.Callable):
            return item_function
        return decorator
