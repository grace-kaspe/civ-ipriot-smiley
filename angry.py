import time
from smiley import Smiley


class Angry(Smiley):
    """
   Provides a Smiley with a happy expression
    """

    def __init__(self):
        super().__init__(complexion=self.RED)

        self.draw_mouth()
        self.draw_eyes()

    def draw_mouth(self):
        """
       Renders a mouth by blanking the pixels that form that object.
        """
        mouth = [42, 43, 44,45, 50, 53]
        for pixel in mouth:
            self.pixels[pixel] = self.BLANK

    def draw_eyes(self, wide_open=True):
        """
       Draws the eyes (open or closed) on the standard smiley.
        :param wide_open (bool): eyes open or closed.
        """
        eyes = [9, 14, 18, 21 ]
        for pixel in eyes:
            if wide_open:
                eyes = self.BLANK
            else:
                eyes = Smiley.complexion(self)
            self.pixels[pixel] = eyes

    def blink(self, delay=0.25):
        """
       Blinks the smiley's eyes once

        :param delay: Delay between blinks (in seconds)
        """
        self.draw_eyes(wide_open=False)
        self.show()
        time.sleep(delay)
        self.draw_eyes(wide_open=True)
        self.show()
