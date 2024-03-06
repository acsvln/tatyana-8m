from asciimatics.scene import Scene
from asciimatics.paths import Path
from asciimatics.effects import Print, Effect, Sprite
from asciimatics.renderers import FigletText, StaticRenderer

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
        self.screen.draw(self.x2, self.y2, '~', )

    def reset(self):
        pass

    def stop_frame(self):
        pass

def scene_nature_birds(screen, duration):
    path = Path()
    path.jump_to(37, 15)
    path.move_straight_to(37, screen.height, 40)

    effects = [
        Print(
            screen,
            FigletText('From nature...', font='big', width=400),
            x=12,
            y=3
        ),
        Sprite(
            screen,
            renderer_dict = {
                "default" : StaticRenderer([bird2])
            },
            path=path,
            clear=True
        ),
        Print(
            screen,
            StaticRenderer([tree]),
            x=100,
            y=30
        ),
        Print(
            screen,
            StaticRenderer([bird1]),
            x=91,
            y=47
        )
    ]

    scene = Scene(effects, duration)

    return scene