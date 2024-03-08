from asciimatics.screen import Screen
from asciimatics.scene import Scene
from asciimatics.paths import Path
from asciimatics.effects import Print, Effect, Sprite
from asciimatics.renderers import FigletText, StaticRenderer

from utils import *
from resources import *

def scene_nature_birds(screen, duration):
    path = Path()
    path.jump_to(37, 15)
    path.move_straight_to(37, screen.height, 40)

    tree_x = screen.width - textBlockWidth(tree) - 15
    tree_y = screen.height - textBlockHeight(tree) - 3

    effects = [
        Print(
            screen,
            FigletText('From nature...', font='big', width=400),
            x=10,
            y=2,
            colour=Screen.COLOUR_GREEN
        ),
        Sprite(
            screen,
            renderer_dict = {
                "default" : StaticRenderer([bird2])
            },
            path=path,
            clear=True,
            colour=Screen.COLOUR_YELLOW
        ),
        Print(
            screen,
            StaticRenderer([tree]),
            x=tree_x,
            y=tree_y,
            colour=Screen.COLOUR_GREEN
        ),
        Print(
            screen,
            StaticRenderer([bird1]),
            x=tree_x - textBlockWidth(bird1) - 2,
            y=tree_y + textBlockHeight(tree) - 14,
            colour=Screen.COLOUR_YELLOW
        )
    ]

    scene = Scene(effects, duration)

    return scene