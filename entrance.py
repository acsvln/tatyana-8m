from asciimatics.screen import ManagedScreen

from scene_intro import *
from scene_nature_fish import *
from scene_nature_birds import *
from scene_commie import *
from scene_ussr import *


@ManagedScreen
def run_the_show(screen=None):
    screen.play([
        scene_intro(screen, 80),
        scene_nature_fish(screen, 80),
        scene_nature_birds(screen, 80),
        scene_commie(screen, 80),
        scene_ussr(screen, 80)
    ], stop_on_resize=False)


if __name__ == "__main__":
    run_the_show()
