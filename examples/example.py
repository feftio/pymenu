import pymenu

menu = pymenu.PyMenu()

@menu.route('/')
def home():
    pass

print(menu.actions_list)