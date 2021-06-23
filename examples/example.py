import pymenu

menu = pymenu.PyMenu()

class HomePage(pymenu.Page):
    pass

class OtherPage(pymenu.Page):
    pass

@menu.page
def home():
    print('It\'s home page.')
    return HomePage()


@menu.page
def other():
    print('It\'s other page.')
    return OtherPage()


menu.load('other')