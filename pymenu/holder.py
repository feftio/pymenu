from __future__ import annotations
import typing as t


class Holder(dict):
    def has(self, object: t.Any) -> bool:
        if object in (*self.keys(), *self.values(),):
            return True
        return False

    def haskey(self, key: t.Any) -> bool:
        if key in self.keys():
            return True
        return False

    def hasvalue(self, value: t.Any) -> bool:
        if value in self.values():
            return True
        return False 