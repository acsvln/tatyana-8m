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

def scene_nature(screen, duration):
    path = Path()
    path.jump_to(screen.width, 10)
    path.move_straight_to(0, 10, 40)

    path_fish_r1 = Path()
    path_fish_r1.jump_to(screen.width, 20)
    path_fish_r1.move_straight_to(0, 20, 40)

    path_fish_r2 = Path()
    path_fish_r2.jump_to(screen.width, 45)
    path_fish_r2.move_straight_to(0, 45, 80)

    path_fish_r3 = Path()
    path_fish_r3.jump_to(screen.width, 54)
    path_fish_r3.move_straight_to(0, 54, 30)

    path_fish_l1 = Path()
    path_fish_l1.jump_to(0, 30)
    path_fish_l1.move_straight_to(screen.width, 30, 20)

    path_fish_l2 = Path()
    path_fish_l2.jump_to(0, 35)
    path_fish_l2.move_straight_to(screen.width, 35, 35)

    effects = [
        Print(
            screen,
            FigletText('From nature...', font='big', width=400),
            x=12,
            y=3
        ),
        DrawLine(
            screen,
            x1=0,
            y1=12,
            x2=screen.width,
            y2=12
        ),
        Sprite(
            screen,
            renderer_dict = {
                "default" : StaticRenderer([kit])
            },
            path=path,
            clear=True #,
            # colour=Colour
        ),
        Sprite(
            screen,
            renderer_dict={
                "default": StaticRenderer([fish1])
            },
            path=path_fish_r1,
            clear=True  # ,
            # colour=Colour
        ),
        Sprite(
            screen,
            renderer_dict={
                "default": StaticRenderer([fish1])
            },
            path=path_fish_r2,
            clear=True  # ,
            # colour=Colour
        ),
        Sprite(
            screen,
            renderer_dict={
                "default": StaticRenderer([fish1])
            },
            path=path_fish_r3,
            clear=True  # ,
            # colour=Colour
        ),
        Sprite(
            screen,
            renderer_dict={
                "default": StaticRenderer([fish2])
            },
            path=path_fish_l1,
            clear=True  # ,
            # colour=Colour
        ),
        Sprite(
            screen,
            renderer_dict={
                "default": StaticRenderer([fish2])
            },
            path=path_fish_l2,
            clear=True  # ,
            # colour=Colour
        )
    ]

    scene = Scene(effects, duration)

    return scene