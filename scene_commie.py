from asciimatics.screen import Screen
from asciimatics.scene import Scene
from asciimatics.paths import Path
from asciimatics.effects import Print, Effect, Sprite
from asciimatics.renderers import FigletText, StaticRenderer

from utils import *
from resources import *


def scene_commie(screen, duration):
    path = Path()
    path.jump_to(37, 15)
    path.move_straight_to(37, screen.height, 40)

    caption_x = screen.width - 86
    caption_y = screen.height - 10

    delta = 9

    effects = [
        Print(
            screen,
            FigletText('To communism...', font='big', width=400),
            x=caption_x,
            y=caption_y,
            colour=Screen.COLOUR_RED
        ),
        Print(
            screen,
            StaticRenderer([commie1]),
            x=10 + delta,
            y=2 + delta,
            colour=Screen.COLOUR_RED
        ),
        Print(
            screen,
            StaticRenderer([lenin]),
            x=screen.width - textBlockWidth(lenin) - 3 * delta,
            y=4,
            colour=Screen.COLOUR_YELLOW
        ),
        Print(
            screen,
            StaticRenderer([cat]),
            x=screen.width - textBlockWidth(cat) - 8 * delta,
            y= caption_y - textBlockHeight(cat) + 5 - delta,
            colour=Screen.COLOUR_YELLOW
        ),
    ]

    scene = Scene(effects, duration)

    return scene