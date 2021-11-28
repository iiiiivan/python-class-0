from pycat.core import Window, AudioLoop, Player
from pycat.geometry import point
from pycat.sprite import Sprite
from random import shuffle
from typing import List

from pyglet.media import player


img_list = 4*['media/1.png', 'media/2.png', 'media/3.png', 'media/4.png']
shuffle(img_list)

w=Window(background_image='media/forest_04.png' , draw_sprite_rects=True)
card_list: List['Card']=[]
loop = AudioLoop('media/LoopLivi.wav')
hit_sound = Player("media/hit.wav")
laugh_sound = Player("media/laugh.wav")
point_sound = Player("media/point.wav")
loop.play()
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
                c0.is_matched = True
                c1.is_matched = True
                point_sound.play()
            else:
                c0.is_visible=False
                c1.is_visible=False
                laugh_sound.play()
            card_list.clear()
        if Card.n == 0:
            w.close()
            



class Card(Sprite):
    n = 0
    def on_create(self):
        self.image='media/1.png'
        self.is_visible=False
        self.add_tag("card")
        self.is_matched = False
        Card.n += 1
    
    def on_left_click(self):
        
        if len(card_list)<2:
            if self not in card_list:
                card_list.append(self)
                hit_sound.play()
                self.is_visible=True
    
    def on_update(self, dt):
        if self.is_matched:
            self.rotation += 5
            self.scale -= 0.05
            if self.scale <= 0:
                self.delete()
                Card.n -= 1
                if Card.n == 0:
                    w.create_sprite(Win)
                    w.draw_sprite_rects = False
                    cb.delete()

class Win(Sprite):

    def on_create(self):
        self.image="media/win.png"
        self.position = w.center

    def on_update(self, dt):
        self.rotation += 5



cb = w.create_sprite(Checkbutton)
for i in range(4):
    for j in range(4):
        s = w.create_sprite(Card, x=100 + j*100, y=500 - i*100)
        s.image = img_list.pop()
w.run()