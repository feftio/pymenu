# pymenu

## Used libraries

- [**rich**](https://github.com/willmcgugan/rich) to rich text and formatting output data;
- [**keyboard**](https://github.com/boppreh/keyboard) to take control of a keyboard.

## Using

```python
import pymenu

menu = pymenu.PyMenu()

@menu.page('my')
class MyPage(Page):
    def build(self):
        return Item('1. pymenu.')

menu.run('my')
```

## Future usage

Install the package using `pip`:

    pip install pymenu

or clone this repository:

    git clone https://github.com/feftio/pymenu

## Prompt design

Make a prompt using [patorjk](http://patorjk.com/software/taag/#p=display&f=Stop&t=pymenu).
