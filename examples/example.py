from pymenu import PyMenu
from pymenu.page import Page
from pymenu.elements import Group, Item, Back, Hidden
from pymenu.triggers import CharsTrigger, KeysTrigger


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
            ),
            Item(
                label='2. Second.',
            ),
            Back(
                label='3. Third.',
            ),
            Hidden(
                action=lambda: print('Hidden called...'),
                triggers=()
            )
        )


menu.run('home')
