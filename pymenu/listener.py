from __future__ import annotations
import typing as t


class Listener:
    def __init__(self, triggers: t.Tuple[str], action: t.Callable):
        self.triggers: t.Tuple[t.Any] = triggers
        self.action: t.Callable = action

    def listen(self, trigger: str):
        if trigger in self.triggers:
            return self.action()
