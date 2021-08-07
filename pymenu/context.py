from __future__ import annotations
import typing as t


class Context:
    def __init__(self) -> None:
        self.history: t.List[str] = []

    @property
    def page(self) -> str:
        return 'routemap'
