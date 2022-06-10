from enum import Enum


class Color(Enum):
    RED = 'red'
    GREEN = 'green'
    BLUE = 'blue'


color = Color(input("Enter your colour choice of red, green or blue: "))

def printColourChoice(color):
    match(color):
        case Color.RED:
            print("I see red!")
        case Color.GREEN:
            print("I see green")
        case Color.BLUE:
            print("I see blue!!")
        case _:
            print("That's not a color")

printColourChoice(color)