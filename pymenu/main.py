from __future__ import annotations
from pymenu.holder import Holder
import typing as t
from pymenu.page import Page, PageBuilder
from pymenu.context import Context


class PyMenu:

    def __init__(self, separator: t.Optional[str] = None, looped: bool = False, printer: t.Callable = lambda *args, **kwargs: print(*args, **kwargs)):
        self.pagebuilder: PageBuilder = PageBuilder()
        self.pageholder: Holder = Holder()  # {pagename: pageclass}
        self.separator: t.Optional[str] = separator
        self.printer: t.Callable = printer
        self.looped: bool = looped  # TODO: make it work.

    @property
    def pages(self):
        return tuple(self.pageholder.items())

    def run(self, pagename: str, *args, **kwargs) -> t.Optional[str]:
        if not self.pageholder.haskey(pagename):
            return None
        pageclass = self.pageholder[pagename]
        self.pagebuilder.build(pagename, pageclass)
        return pageclass.__name__

    def page(self, page: t.Union[Page, str]) -> t.Callable:
        if isinstance(page, str):
            def decorator(pageclass: Page):
                pagename = page
                if not isinstance(pageclass, Page.__class__):
                    raise TypeError(
                        f'{pageclass.__name__} must be inherited from Page class.')
                self.pageholder.add(pagename, pageclass)
                return pageclass
            return decorator
        pagename, pageclass = page.__name__, page
        self.pageholder.add(pagename, pageclass)
        return pageclass

    # TODO: if calling page is not in holder, execute user's method.
    def none(self, f: t.Callable) -> t.Callable:
        def decorator():
            return f
        return decorator
