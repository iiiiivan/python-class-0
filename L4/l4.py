from pycat.core import Window, Sprite, KeyCode, RotationMode
from pyglet.image import create

window = Window(background_image='img/sea.png',enforce_window_limits=False)

class Owl(Sprite):
    
    def on_create(self):

        self.image="img/owl.png"
        self.x=50
        self.y=500

    def on_update(self, dt):
        # self.move_forward(5)
        if window.is_key_pressed(KeyCode.UP):
            self.rotation=90
        if window.is_key_pressed(KeyCode.DOWN):
            self.rotation=270
        if window.is_key_pressed(KeyCode.RIGHT):
            self.rotation=0
        if window.is_key_pressed(KeyCode.LEFT):
            self.rotation=180

        if self.is_touching_any_sprite():
            print('you lose')
            # window.close()

        if self.x > 1250:
            print('you win')
            # window.close()



class Ork1(Sprite):

    def on_create(self):
        
        self.image="img/ork1.png"
        self.scale=0.2
        self.goto_random_position()
        self.layer=1
        # self.rotation_mode=RotationMode.RIGHT_LEFT
        

    def on_update(self, dt):
        
        self.rotation+=3
        self.move_forward(10)
        # if self.is_touching_window_edge():
        #     self.rotation+=270
for i in range(5):
    window.create_sprite(Ork1)
            





# window.create_sprite(image='img/beach.png', x=400, y=600)
# window.create_sprite(image='img/beach.png', x=400, y=400)
# window.create_sprite(image='img/beach.png', x=400, y=300)
# window.create_sprite(image='img/beach.png', x=1000, y=0)
# window.create_sprite(image='img/beach.png', x=1000, y=100)
# window.create_sprite(image='img/beach.png', x=1000, y=200)
# window.create_sprite(image='img/beach.png', x=1000, y=300)
# window.create_sprite(image='img/beach.png', x=1000, y=400)
window.create_sprite(Owl)
window.create_sprite(Ork1)
window.run()