from __future__ import annotations
from .page import Page
import typing as t


class PyMenu:

    # Constructor
    def __init__(self, separator: t.Optional[str] = None, *args, **kwargs) -> None:
        self.callbacks: t.Dict[str, t.Callable] = {}
        self.separator: t.Optional[str] = separator

    def load(self, page_name: str) -> Page:
        self.callbacks[page_name]()

    # Used as decorator
    # def page(self, callback: t.Callable) -> t.Callable:
    #     def decorator(callback: t.Callable) -> t.Callable:
    #         self.callbacks[callback.__name__] = callback
    #         return callback
    #     return decorator

    def page(self, callback: t.Callable) -> t.Callable:
        self.callbacks[callback.__name__] = callback
        return callback
