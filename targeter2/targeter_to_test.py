"""
Randomly point a target in a picture.

Usage:
    targeter.py PICTURE_FILE


Press enter to add a new target, backspace to remove the last target from the picture, and escape
to quit. You can also press 'r' to do both, the removing of the last target and the adding of a
new one (typical use: "last target wasn't good, re-roll!")

Also, you can use the zoom controls of the picture to zoom in into the targets, and keys will keep
working as intended. Try it out! :)
"""
import random
import sys
from pathlib import Path

from docopt import docopt
from matplotlib import pyplot as plt
from matplotlib.patches import Rectangle
from PIL import Image


class Targeter:
    def __init__(self, picture):
        self.TARGET_FACTOR = 0.05
        self.targets = []
        self.keep_targetting = True
        self.picture = picture
        self.max_width, self.max_height = picture.size
        self.target_size = min(
            (self.max_width * self.TARGET_FACTOR, self.max_height * self.TARGET_FACTOR)
        )

    def add_target(self):
        new_target = random.randint(0, self.max_width), random.randint(0, self.max_height)
        self.targets.append(new_target)
        print('New target:', new_target)

    def remove_target(self):
        if self.targets:
            print('Remove last target')
            self.targets.pop()
        else:
            print('No targets to remove')

    def draw_target(self, position, color, fig):
        x, y = position
        vertical_line = Rectangle((x, y - self.target_size / 2), 0, self.target_size,
                                  linewidth=3, edgecolor=color, facecolor='none')
        horizontal_line = Rectangle((x - self.target_size / 2, y), self.target_size, 0,
                                    linewidth=3, edgecolor=color, facecolor='none')
        selection = fig.add_subplot(111)
        selection.add_patch(vertical_line)
        selection.add_patch(horizontal_line)

    def on_key(self, event):
        if event.key == 'escape':
            # stop targetting
            print('Have a nice day :)')
            self.keep_targetting = False
            plt.close('all')
        elif event.key == 'enter':
            self.add_target()
            plt.close('all')
        elif event.key == 'backspace':
            self.remove_target()
            plt.close('all')
        elif event.key == 'r':
            self.remove_target()
            self.add_target()
            plt.close('all')

    def run(self):
        while self.keep_targetting:
            ax = plt.imshow(self.picture)

            fig = ax.get_figure()
            fig.canvas.set_window_title("Random targets!!")

            fig.canvas.mpl_connect('key_press_event', self.on_key)

            mng = plt.get_current_fig_manager()
            mng.resize(*mng.window.maxsize())

            plt.axis('off')

            last_target = len(self.targets) - 1
            for target_number, target in enumerate(self.targets):
                if target_number == last_target:
                    color = (0.5, 1, 0, 0.7)
                else:
                    color = 'r'
                self.draw_target(target, color, fig)

            plt.show(block=True)


if __name__ == '__main__':
    opts = docopt(__doc__)
    picture_path = Path(opts['PICTURE_FILE'])

    if not picture_path.exists():
        print("No picture found in the specified path")
        sys.exit(1)

    picture = Image.open(picture_path)

    targeter = Targeter(picture)
    targeter.run()
