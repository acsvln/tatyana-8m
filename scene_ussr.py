from asciimatics.screen import Screen
from asciimatics.scene import Scene
from asciimatics.effects import Print, Effect
from asciimatics.renderers import FigletText, StaticRenderer

from utils import *
from resources import *

class DrawLine(Effect):
    def __init__(self, screen, x1, y1, x2, y2, colour):
        super().__init__(screen)
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        self.colour=colour
        # self.screen = screen

    def _update(self, frame_no):
        self.screen.move(self.x1, self.y1)
        self.screen.draw(self.x2, self.y2, '⣿', colour = self.colour )

    def reset(self):
        pass

    def stop_frame(self):
        pass

class SimplePrint(Effect):
    def __init__(self, screen, x, y, text, colour):
        super().__init__(screen)
        self.text = text
        self.x = x
        self.y = y
        self.colour=colour

    def _update(self, frame_no):
        self.screen.print_at( self.text, self.x, self.y, colour=self.colour, attr=0, bg=0, transparent=False)

    def reset(self):
        pass

    def stop_frame(self):
        pass


def scene_ussr(screen, duration):

    yy = screen.height // 2 - textBlockHeight(ussr_world) // 2
    xx = screen.width // 2 - textBlockWidth(ussr_world) // 2

    effects = [
        Print(
            screen,
            StaticRenderer([ussr_world]),
            x= xx,
            y= yy,
            colour= Screen.COLOUR_RED
        ),
        SimplePrint(
            screen,
            screen.width // 2 - 17,
            yy,
            "my congratulations to Τατιανα",
            Screen.COLOUR_CYAN
        ),
        DrawLine(
            screen,
            xx,
            yy,
            xx,
            yy-1,
            colour=Screen.COLOUR_RED
        ),
        DrawLine(
            screen,
            xx,
            yy - 1,
            xx + textBlockWidth(ussr_world),
            yy - 1,
            colour=Screen.COLOUR_RED
        ),
        DrawLine(
            screen,
            xx + textBlockWidth(ussr_world) - 1,
            yy - 1,
            xx + textBlockWidth(ussr_world) - 1,
            yy + 1,
            colour=Screen.COLOUR_RED
        )
    ]

    scene = Scene(effects, duration)

    return scene