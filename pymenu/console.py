from __future__ import annotations
import typing as t
import os


class Console:
    def __init__(self):
        pass

    @staticmethod
    def write(*args, **kwargs) -> None:
        print(*args, **kwargs)

    @staticmethod
    def read(prompt: t.Any = '') -> str:
        return input(prompt)

    @staticmethod
    def clear() -> None:
        os.system('cls' if os.name == 'nt' else 'clear')
