from enum import Enum


class Color(Enum):
    RED = 0
    GREEN = 1
    BLUE = 2
    BLACK = 3


def print_color(color: Color):
    match color:
        case Color.RED:
            print("It's red!")
        case Color.GREEN | Color.BLUE:
            print("It's either green or blue")
        case _:
            print("It's something else")


print_color(Color.RED)
print_color(Color.BLUE)
print_color(Color.BLACK)
