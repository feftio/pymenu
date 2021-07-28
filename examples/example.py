from pymenu.context import Context
from pymenu import PyMenu
from pymenu.page import Page
import os


menu = PyMenu()


@menu.none
def none():
    print('No Page')


@menu.page('home')
class HomePage(Page):
    def build(self):
        return Group(
            Item(
                label='1. First.',
                action=lambda: self.print('First called'),
                triggers=(
                    CharsTrigger('1', 'First', 'first')
                )
            ),
            Item(
                label='2. Second.',
                triggers=(
                    CharsTrigger('2', 'Second', 'second')
                )
            ),
            Back(
                label='3. Third.',
                triggers=(
                    CharsTrigger('3', 'Third', 'third')
                )
            )
        )


# menu.run('home')