from re import I
from pycat.core import Window, Sprite
from pycat.label import Label
from pyglet import image

w=Window(background_image="media/forest_04.png")

img_list = [
    "media/1.jpg",
    "media/2.jpg",
    "media/3.jpg",
    "media/4.jpg",
    "media/5.jpg",
    "media/6.jpg",
    "media/7.jpg",
    "media/8.jpg",
    "media/9.jpg",
    "media/10.jpg",
]

txt_list=[
    "bus stop1",
    "bus stop2",
    "bus stop3",
    "rest place",
    "",
    "bus stop4",
    "strawberry",
    "babyshark",
    "",
    "bus stop5",
]


w.background_image = img_list[0]

class Title(Label):
    def on_create(self):
        self.x=550
        self.y=600
        self.font_size=50


label = w.create_label(Title)
label.text = txt_list[0]


class Nextbutton(Sprite):
    
    def on_create(self):
        self.image="media/button_next.png"
        self.x=600
        self.y=100
        self.scale=0.5
        self.i=0


    def on_left_click(self):
        self.i += 1
        if self.i > 9:
           self.i=0
        
        w.background_image=img_list[self.i]
        label.text=txt_list[self.i]

        
w.create_sprite(Nextbutton)
w.run()