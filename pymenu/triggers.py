from __future__ import annotations
import typing as t


class Trigger:
    def __init__(self, content: str):
        self.content: str = content


class CharsTrigger(Trigger):
    pass


class KeysTrigger(Trigger):
    pass


class MouseTrigger(Trigger):
    pass
