from pycat.base.color import Color
from pycat.core import Window
from pycat.sprite import Sprite
from random import randint

w=Window()
class Particle(Sprite):
    def on_create(self):
        self.scale=10
        self.color=Color.TEAL
        self.goto_random_position()
        self.rotation=randint(0, 360)

    def on_update(self, dt):
        self.move_forward(5)
        if self.is_touching_window_edge():
            self.rotation +=180
            self.rotation %=360


for i in range(200):
    w.create_sprite(Particle)
w.run()