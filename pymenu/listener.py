from __future__ import annotations
import typing as t
from pymenu.triggers import Trigger


class Listener:
    def listener(self, action: t.Callable, triggers: t.Tuple[Trigger]) -> None:
        self.action: t.Callable = action
        self.triggers: t.Tuple[Trigger] = triggers

    def listen(self, trigger: Trigger) -> None:
        pass
