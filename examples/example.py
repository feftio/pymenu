from pymenu import PyMenu
from pymenu.page import DefaultPage, SelectionPage
import os


menu = PyMenu()


@menu.page(name='home')
class HomeSelectionPage(SelectionPage):

    @menu.item(output='1. Home.', triggers=['1'])
    def home(self):
        pass

    @menu.item(output='2. Other.', triggers=['2'])
    def other(self):
        pass

    @menu.item(output='3. Exit.', triggers=['3'])
    def exit(self):
        os.system('exit')


@menu.page(name='other')
class OtherPage(DefaultPage):

    def show(self):
        print("Other Page is showing...")


menu.show('home')
