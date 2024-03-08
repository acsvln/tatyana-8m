from asciimatics.screen import Screen
from asciimatics.scene import Scene
from asciimatics.effects import Print, Effect
from asciimatics.renderers import FigletText, StaticRenderer

from utils import *
from resources import *

def scene_intro(screen, duration):
    screen_center = screen.width // 2

    x_t = screen_center - textBlockWidth(tatyana) // 2
    y_t = 2

    x_f = screen_center - textBlockWidth(flower) // 2
    y_f = y_t + textBlockHeight(tatyana) - 6

    x_8m = screen_center - 34
    y_8m = y_f + textBlockHeight(flower) - 10
    
    x_8m8 = screen_center - 44
    y_8m8 = y_f + textBlockHeight(flower) - 15

    effects = [
        Print(
            screen,
            StaticRenderer([flower]),
            x=x_f,
            y=y_f,
            colour=Screen.COLOUR_RED
        ),
        Print(
            screen,
            StaticRenderer([tatyana]),
            x=x_t,
            y=y_t,
            clear=True,
            transparent=False,
            colour=Screen.COLOUR_GREEN
        ),
        Print(
            screen,
            FigletText('8', font='doh'),
            x=x_8m8,
            y=y_8m8,
            colour=Screen.COLOUR_BLUE
        ),
        Print(
            screen,
            FigletText('march', font='isometric4'),
            x=x_8m,
            y=y_8m,
            transparent=True,
            clear=True,
            colour=Screen.COLOUR_CYAN
        )
    ]

    scene = Scene(effects, duration)

    return scene
