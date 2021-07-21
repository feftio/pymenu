from __future__ import annotations
from pymenu.holder import Holder
import typing as t
from pymenu.page import Page
from pymenu.context import Context


class PyMenu:

    def __init__(self, separator: t.Optional[str] = None, printer: t.Callable = lambda *args, **kwargs: print(*args, **kwargs)):
        self.context: t.Type[Context] = Context()
        self.pageholder: t.Type[Holder] = Holder()  # {pagename: pageclass}
        self.separator: t.Optional[str] = separator
        self.printer: t.Callable = printer

    @property
    def pages(self):
        return tuple(map(lambda item: (item[0], item[1].__name__), self.pageholder.items()))

    def run(self, pagename: str, *args, **kwargs) -> t.Optional[str]:
        if not self.pageholder.haskey(pagename):
            return None
        page = self.pageholder[pagename]
        page(Context()).build(*args, **kwargs)
        return page.__name__

    def page(self, pagename: str) -> t.Callable:
        def decorator(pageclass: t.Type[Page]):
            if not isinstance(pageclass, Page.__class__):
                raise TypeError(
                    f'{pageclass.__name__} must be inherited from Page class.')
            self.pageholder.add(pagename, pageclass)
            return pageclass
        return decorator
