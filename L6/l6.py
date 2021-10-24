from pycat.core import Window, Sprite, RotationMode, Scheduler
from random import randint


w=Window(background_image='media/underwater_04.png')


label=w.create_label()
label.text='Score = 0'

class Ship(Sprite):

    def on_create(self):
        self.image="media/saucer.png"
        self.x=100
        self.y=550
        self.scale=0.3
        self.score=0
        self.rotation_mode=RotationMode.NO_ROTATION

    def on_update(self, dt):
        self.move_forward(7)
        if self.is_touching_window_edge():
            self.rotation += 180
       

class Alien(Sprite):

    def on_create(self):
        self.image="media/1.png"
        self.scale=0.3
        self.goto_random_position()
        self.y=50
        self.is_click=False

    def on_update(self, dt):
        if self.is_click:
           self.y += 10
        if self.is_touching_sprite(ship):
            self.delete()
            ship.score+=1
            label.text='Score='+str(ship.score)
        if self.y > 620:
            self.delete()

    def on_left_click(self):
        self.is_click=True
        
     



def create_alien():
    w.create_sprite(Alien)

Scheduler.update(create_alien, 0.01)

ship = w.create_sprite(Ship)
w.create_sprite(Alien)
w.run()