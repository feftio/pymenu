from pymenu.context import Context
from pymenu import PyMenu
from pymenu.page import Page
import os


menu = PyMenu()


# @menu.page(name='home')
# class HomeSelectionPage(SelectionPage):
#     @menu.item(output='1. Home.', triggers=['1'])
#     def home(self):
#         pass

#     @menu.item(output='2. Other.', triggers=['2'])
#     def other(self):
#         pass

#     @menu.item(output='3. Exit.', triggers=['3'])
#     def exit(self):
#         os.system('exit')


# @menu.page('about')
# class AboutPage(Page):
#     def show(self):
#         print('About Page is showing...')


# @menu.page('other')
# class OtherPage(Page):
#     def show(self):
#         pass

@menu.page('some')
class SomePage(Page):
    def choose_algorithm(self):
        pass

    def helper(self):
        pass

    def show(self):
        self.item(label='1. Choose algorithm.', trigger=self.choose_algorithm, on=['1'])
        self.item(label='2. Help.', trigger=self.helper)

menu.run('some')