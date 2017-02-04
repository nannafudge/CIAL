import sys
import requests as hammertime
from asciimatics.effects import Print, Stars
from asciimatics.renderers import ImageFile, FigletText
from asciimatics.scene import Scene
from asciimatics.screen import Screen

def hammer_time(microsoftpaint):
    magic_x_number = int(microsoftpaint.width / 2)  # Don't touch this is magic constant jk (^:
    magic_y_number = int(microsoftpaint.height / 2)

    text1 = FigletText("SMASH THAT", "small")
    text2 = FigletText("WWEBSITE BOI", "small")

    renderer = ImageFile("img/mchammer.gif", height=microsoftpaint.height - (text1.max_height + text2.max_height))
    mayme = \
        [
            Print(microsoftpaint, renderer, magic_y_number - int(renderer.max_height / 2), magic_x_number - int(renderer.max_width / 2), colour=8, bg=Screen.COLOUR_BLACK),
            Print(microsoftpaint, text1, 0, x=magic_x_number - int(text1.max_width / 2), speed = 1),
            Print(microsoftpaint, text2, renderer.max_height + text2.max_height, x=magic_x_number - int(text2.max_width / 2), speed = 1),
            Stars(microsoftpaint, 30)
        ]

    microsoftpaint.play([Scene(mayme, 500)])


if __name__ == "__main__":
    # Just fuck my shit up fam
    url = sys.argv[0]
    if url is not None:
        Screen.wrapper(hammer_time)
    else:
        print("No URL supplied to load test")
