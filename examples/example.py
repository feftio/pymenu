from pymenu import PyMenu
from pymenu.page import Page
from pymenu.elements import Group, Item, Back, Hidden, Redirect
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
                triggers=('1'),
                action=lambda: menu.run('work')
            ),
            Item(
                label='2. Print history.',
                triggers=('2', 'print'),
                action=lambda: print(self.context.history)
            ),
            Redirect(
                to='work',
                triggers=()
            ),
            Hidden(
                action=lambda: print('Hidden called...'),
                triggers=()
            )
        )


@menu.page('work')
class WorkPage(Page):
    def build(self):
        return Group(
            Item(
                label='1. Write report.',
                triggers=('1', 'write', '@Ctrl + v'),
                action=lambda: menu.run('home')
            ),
            Back(
                label='2. Go back.',
            )
        )


menu.run('work')
