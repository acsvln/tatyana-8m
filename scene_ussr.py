from asciimatics.scene import Scene
from asciimatics.effects import Print, Effect
from asciimatics.renderers import FigletText, StaticRenderer

from utils import *
from resources import *
def scene_ussr(screen, duration):

    effects = [
        Print(
            screen,
            StaticRenderer([ussr_world]),
            x=0,
            y=0
        )
    ]

    scene = Scene(effects, duration)

    return scene