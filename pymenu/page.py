from __future__ import annotations
import typing as t
from abc import ABCMeta, abstractmethod
from pymenu.context import Context


class Page(metaclass=ABCMeta):
    def __init__(self, context: t.Type[Context]):
        self.context: t.Type[Context] = context
        # if hasattr(self, 'show') and callable(getattr(self, 'show')):
        #     self.show()

    @abstractmethod
    def show(self):
        pass

# class Page:
#     def __init__(self, context: t.Type[Context]):
#         self.context: t.Type[Context] = context

#     def show(self):
#         raise NotImplementedError(
#             f'"show" method in {self.__class__.__name__} class must be overriden.')


class SelectionPage(Page):
    def show(self):
        pass


class PageCollector:
    """ Class which manages decorated classes inherited 
    from `~pymenu.page.Page`."""

    def __init__(self):
        # {page_name: page_class}
        self._pages: t.Dict[str, t.Type[Page]] = {}

    def add(self, page_name: str, page_class: t.Type[Page]) -> None:
        self._pages[page_name] = page_class

    def has_page_name(self, page_name: str):
        if page_name in self._pages.keys():
            return True
        return False

    def has_page_class(self, page_class: t.Type[Page]):
        if page_class in self._pages.values():
            return True
        return False

    @property
    def page_names(self) -> t.Tuple[str]:
        return tuple(self._pages.keys())

    @property
    def page_classes(self) -> t.Tuple[t.Type[Page]]:
        return tuple(self._pages.values())

    def _collect_info(self) -> None:
        pass
