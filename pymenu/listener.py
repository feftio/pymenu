from __future__ import annotations
import typing as t


class Listener:
    def __init__(self, on: t.Tuple[str], action: t.Callable):
        self.on: t.Tuple[t.Any] = on
        self.action: t.Callable = action

    def some(self, on: t.Tuple[str]) -> t.Any:
        for event in on:
            if event in self.on:
                return self.action()

    def each(self, on: t.Tuple[str]) -> t.List[t.Any]:
        action_results = []
        for event in on:
            if event in self.on:
                action_results.append(self.action())
        return action_results
