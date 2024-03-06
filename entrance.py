from asciimatics.screen import ManagedScreen, Screen

from scene_intro import *
from scene_nature import *
from scene_nature_birds import *
from scene_commie import *

@ManagedScreen
def run_the_show(screen=None):
    screen.play( [
        scene_intro(screen, 80),
        scene_nature(screen, 80),
        scene_nature_birds( screen, 80 ),
        scene_commie(screen, 80)
    ], stop_on_resize=False )
    screen.move(16, 23)
    screen.draw(23, 23, '+')

if __name__ == "__main__":
    run_the_show()