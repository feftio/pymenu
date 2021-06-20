import typing as t


class PyMenu:
    actions_list: list = []

    # Constructor
    def __init__(self, *args, **kwargs):
        pass

    # Used as decorator
    def route(self, rule : str) -> t.Callable:
        def decorator(action: t.Callable) -> t.Callable:
            self.actions_list.append(action.__name__)
            return action
        return decorator
