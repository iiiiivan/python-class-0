import random
from pycat.core import Window, Sprite, KeyCode, RotationMode, Scheduler


w = Window(background_image='img/beach_03.png')

class Player(Sprite):

    def on_create(self):
        
        self.image="img/cat.png"
        self.x=600
        self.y=50
        self.rotation_mode=RotationMode.RIGHT_LEFT

    def on_update(self, dt):
        
        if w.is_key_pressed(KeyCode.RIGHT):
            self.rotation=0
            self.move_forward(100)
        if w.is_key_pressed(KeyCode.LEFT):
            self.rotation=180
            self.move_forward(100)

class Gem(Sprite):

    def on_create(self):
        
        self.image="img/gem_shiny03.png"
        self.goto_random_position()
        self.y=650
        self.scale=0.3
    
    def on_update(self, dt):
        self.y-=100
        if self.is_touching_any_sprite():
            self.delete()

        if self.y < 2:
            self.delete()
        

def create_gem():
    w.create_sprite(Gem)

Scheduler.update(create_gem, 0.0001)
w.create_sprite(Player)

w.run()