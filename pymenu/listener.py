from __future__ import annotations
import typing as t
from pymenu.triggers import Trigger


class Listener:
    def listener(self, action: t.Optional[t.Callable] = None, triggers: t.Optional[t.Tuple[Trigger]] = None) -> None:
        self.action: t.Optional[t.Callable] = action
        self.triggers: t.Optional[t.Tuple[Trigger]] = triggers

    def listen(self, trigger: Trigger) -> None:
        if ((not hasattr(self, 'action'))
                or (not hasattr(self, 'triggers'))
                or (getattr(self, 'action') is None)
                or (getattr(self, 'triggers') is None)
                ):
            return
        # TODO: if trigger in triggers, execute action.


class GroupListener(Listener):
    def _notify(self, trigger: Trigger) -> None:
        """ Must be inherated with class which consist childs fields. """
        for element in self.childs:
            element.listen(trigger)

    def listen(self, trigger: Trigger) -> None:
        super().listen(trigger)
        self._notify(trigger)
