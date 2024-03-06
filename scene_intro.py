from asciimatics.scene import Scene
from asciimatics.effects import Print, Effect
from asciimatics.renderers import FigletText, StaticRenderer

from utils import *
from resources import *


class DrawLine(Effect):
    def __init__(self, screen, x1, y1, x2, y2):
        super().__init__(screen)
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        # self.screen = screen

    def _update(self, frame_no):
        self.screen.move(self.x1, self.y1)
        self.screen.draw(self.x2, self.y2, '0', )

    def reset(self):
        pass

    def stop_frame(self):
        pass


def scene_intro(screen, duration):
    xv_t = screen.width // 2 - textBlockWidth(tatyana) // 2
    yv_t = 2

    xv_f = screen.width  // 2 - textBlockWidth(flower) // 2
    yv_f = textBlockHeight(tatyana) + 1

    xv_8m = screen.width // 2 - 38
    xv_8m1 = screen.width // 2 - 44
    yv_8m = ( yv_f + textBlockHeight(flower) ) - 10
    yv_8m1 = (yv_f + textBlockHeight(flower)) - 15

    outline_base_x=64
    outline_base_y=36

    effects = [
        Print(
            screen,
            StaticRenderer([tatyana]),
            x=xv_t,
            y=yv_t
        ),
        Print(
            screen,
            StaticRenderer([flower]),
            x=xv_f,
            y=yv_f
        ),
        Print(
            screen,
            FigletText('8', font='doh'),
            x=xv_8m1,
            y=yv_8m1
        ),
        Print(
            screen,
            FigletText('8 march', font='isometric4'),
            x=xv_8m,
            y=yv_8m,
            transparent=True,
            clear=True
        ),
        DrawLine(
            screen,
            x1=outline_base_x,
            y1=outline_base_y,
            x2=outline_base_x,
            y2=outline_base_y + 2
        ),
        DrawLine(
            screen,
            x1=outline_base_x,
            y1=outline_base_y + 2,
            x2=outline_base_x + 2,
            y2=outline_base_y + 2
        )
    ]

    scene = Scene(effects, duration)

    return scene
