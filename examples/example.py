from pymenu.context import Context
from pymenu import PyMenu
from pymenu.page import Page
import os


menu = PyMenu()


@menu.page('home')
class HomePage(Page):
    def build(self):
        self.item(label='1. Choose algorithm.')
        self.item(label='2. Help.')


@menu.page('some')
class SomePage(Page):
    def build(self):
        self.item(
            label='1. Run "Exit".',
            action=lambda: print('Running...'),
            triggers=('1', 'Run', 'run')
        )
        self.item(
            label='2. Show items.',
            action=lambda: self.print(self.items),
            triggers=('2', 'Items', 'items')
        )
        self.item(
            label='3. Go to "home".',
            action=lambda: self.redirect('home'),
            triggers=('3', 'Home', 'home')
        )
        self.item(
            label='4. Empty item.',
            action=lambda: menu.run('some'),
            triggers=('4', 'Some', 'some', '')
        )


menu.run('some')
