from rich.segment import Segment
from pymenu import PyMenu
from pymenu.page import Page
from pymenu.elements import Group, Item, Back, Hidden, Redirect
import keyboard
import time
from threading import Thread

# from rich import print
# from rich.layout import Layout

# layout = Layout()
# layout.split_column(
#     Layout(name="upper"),
#     Layout(name="lower")
# )
# print(layout)

# table = Table()
# table.add_column("Row ID")
# table.add_column("Description")
# table.add_column("Level")

# with Live(table, refresh_per_second=10):  # update 4 times a second to feel fluid
#     print('hello')
#     for row in range(12):
#         time.sleep(0.4)  # arbitrary delay
#         # update the renderable internally
#         table.add_row(f"{row}", f"description {row}", "[red]ERROR")


# menu = PyMenu()


# @menu.none
# def none():
#     print('No Page')


# @menu.page('home')
# class HomePage(Page):
#     def build(self):
#         return Group(
#             Item(
#                 label='1. First.',
#                 triggers=('1'),
#                 action=lambda: menu.run('work')
#             ),
#             Item(
#                 label='2. Print history.',
#                 triggers=('2', 'print'),
#                 action=lambda: print(self.context.history)
#             ),
#             Redirect(
#                 to='work',
#                 triggers=()
#             ),
#             Hidden(
#                 action=lambda: print('Hidden called...'),
#                 triggers=()
#             )
#         )


# @menu.page('work')
# class WorkPage(Page):
#     def build(self):
#         return Group(
#             Item(
#                 label='1. Write report.',
#                 triggers=('1', 'write', '~Ctrl+v~'),
#                 action=lambda: menu.run('home')
#             ),
#             Back(
#                 label='2. Go back.',
#             )
#         )


# menu.run('work')

menu = PyMenu()

@menu.page('my')
class MyPage(Page):
    def build(self):
        return Item('1. pymenu.')

print(menu.pages)
# menu.run('my')