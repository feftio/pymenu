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


@menu.page('work')
class SomePage(Page):
    def build(self):
        self.item(label='1. Run "Exit".',
                  action=lambda: print('Running...'),
                  triggers=('1', 'Run'))
        self.item(label='2. Back.',
                  action=lambda: menu.run('home'),
                  triggers=('2'))


menu.run('work')
