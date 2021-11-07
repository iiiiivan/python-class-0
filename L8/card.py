from re import S
from pycat.base import image
from pycat.core import Window
from pycat.sprite import Sprite
from random import shuffle

from pyglet.window.key import C


img_list = 4*['media/1.png', 'media/2.png', 'media/3.png', 'media/4.png']
shuffle(img_list)

w=Window(draw_sprite_rects=True)
card_list=[]
class Checkbutton(Sprite):
    def on_create(self):
        self.image='media/button.png'
        self.x=900
        self.y=350
        self.scale=0.5
    
    def on_left_click(self):
        if len(card_list) == 2:
            c0=card_list[0]
            c1=card_list[1]
            if c0.image==c1.image:
                c0.delete()
                c1.delete()
            else:
                c0.is_visible=False



class Card(Sprite):

    def on_create(self):
        self.image='media/1.png'
        self.is_visible=False
    
    def on_left_click(self):
        if len(card_list)<2:
            card_list.append(self)
            self.is_visible=True

w.create_sprite(Checkbutton)
for i in range(4):
    for j in range(4):
        s = w.create_sprite(Card, x=100 + j*100, y=500 - i*100)
        s.image = img_list.pop()
w.run()