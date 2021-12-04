from pycat.base.color import Color
from pycat.core import Window
from pycat.sprite import Sprite
from random import randint


w=Window()


class Button(Sprite):
    def on_create(self):
        self.scale=100
        self.y=150
    
    def on_left_click(self):
       
        for i in range(5):
            w.create_sprite(Particle)
        
        


class Particle(Sprite):
    def on_create(self):
        self.scale=10
        self.y=50
        self.color=Color.TEAL
        self.x=w.center.x
        self.rotation=randint(80, 100)
        self.add_tag('particle')
        self.time=0

    def on_update(self, dt):
        self.time+=dt
        self.move_forward(10)
        if self.time>0.5:
            self.delete()
            for r in range(36):
                p=w.create_sprite(SubParticle)
                p.position=self.position
                p.rotation=r*10

class SubParticle(Sprite):
    def on_create(self):
        self.scale=4
        self.color=Color.TEAL
        self.time=0

    def on_update(self, dt):
        self.move_forward(5)
        self.opacity-=3
        if self.opacity<5:
            self.delete()



w.create_sprite(Button, x=100, color=Color.GREEN) 
   
w.run()