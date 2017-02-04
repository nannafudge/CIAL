import random
import sys
import threading
import os

import requests as hammertime
from asciimatics.effects import Print, Stars
from asciimatics.exceptions import ResizeScreenError
from asciimatics.renderers import ImageFile, FigletText
from asciimatics.scene import Scene
from asciimatics.screen import Screen

def draw(microsoftpaint):
    magic_x_number = int(microsoftpaint.width / 2)  # Don't touch this is magic constant jk (^:
    magic_y_number = int(microsoftpaint.height / 2)

    text1 = FigletText("SMASH THAT", "small")
    text2 = FigletText("WWEBSITE BOI", "small")

    images = os.listdir("img")

    renderer = ImageFile("img/" + images[random.randint(0, len(images))], height=microsoftpaint.height - (text1.max_height + text2.max_height))

    # Actually kill me this is disgusting
    mayme = \
        [
            Print(microsoftpaint, renderer, magic_y_number - int(renderer.max_height / 2), magic_x_number - int(renderer.max_width / 2), colour=8, bg=Screen.COLOUR_BLACK),
            Print(microsoftpaint, text1, 0, x=magic_x_number - int(text1.max_width / 2), speed = 1),
            Print(microsoftpaint, text2, renderer.max_height + text2.max_height, x=magic_x_number - int(text2.max_width / 2), speed = 1),
            Stars(microsoftpaint, 30)
        ]

    microsoftpaint.play([Scene(mayme, 500)])


def hammer_time(url):
    hammertime.request(url)


if __name__ == "__main__":
    # Just fuck my shit up fam
    last_scene = None
    url = sys.argv[0]
    if url is None:
        print("No URL supplied to load test")
        exit(-1)
    hammerthread = threading.Thread(target=hammer_time, args=url, daemon=True)
    hammerthread.start()
    while True and hammerthread.is_alive():
        try:
            Screen.wrapper(draw, catch_interrupt=True, arguments=last_scene)
        except ResizeScreenError as e:
            last_scene = e.scene
