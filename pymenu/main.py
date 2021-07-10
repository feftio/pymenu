from __future__ import annotations
import typing as t
from pymenu.page import Page, PageCollector
from pymenu.context import Context


class PyMenu:

    def __init__(self, separator: t.Optional[str] = None, *args, **kwargs) -> None:
        # self.context: t.Type[Context] = Context()
        self.page_collector: t.Type[PageCollector] = PageCollector()
        self.separator: t.Optional[str] = separator

    @property
    def pagenames(self):
        return self.page_collector.page_names

    def run(self, name: str) -> None:
        if not self.page_collector.has_page_name(name):
            return None
        page = self.page_collector._pages[name]
        page(Context()).show()
        return page.__class__

    def page(self, name: str) -> t.Callable:
        def decorator(page_class: t.Type[Page]):
            if not isinstance(page_class, Page.__class__):
                raise TypeError(
                    f'{page_class.__name__} must be inherited from Page class.')
            self.page_collector.add(name, page_class)
            return page_class
        return decorator

    def item(self, output: str, triggers: t.List[str]) -> t.Callable:
        def decorator(item_function: t.Callable):
            return item_function
        return decorator
