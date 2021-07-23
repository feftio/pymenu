from __future__ import annotations
import typing as t
import os


class Console:
    def __init__(self):
        pass

    @staticmethod
    def read() -> None:
        return input()

    @staticmethod
    def clear():
        os.system('cls' if os.name == 'nt' else 'clear')
