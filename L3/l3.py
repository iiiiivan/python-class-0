from pycat.core import Window, KeyCode
from pycat.sprite import Sprite
window = Window()
# x =input("enter x")
# y =input("enter y")

class Owl(Sprite):
    
    def on_create(self):
        self.image="owl.gif"
        self.y=350
    
    def on_update(self, dt):
        if window.is_key_pressed(KeyCode.RIGHT):
            self.x += 6         
        if self.x>window.width:
            window.close()


class Fireball(Sprite):
    
    def on_create(self):
        self.image="fireball.gif"
        self.y=400

    def on_update(self, dt):
        self.x += 5
        if self.x>window.width:
            window.close()

for i in range(10):
    window.create_sprite(Owl)
    window.create_sprite(Fireball)


# sprite= window.create_sprite()
# sprite.image ='elephant.png'
# sprite.x =float(x)
# sprite.y =float(y)

# message=('my sprite has image ' + sprite.image 
#         +', x=' + str(sprite.x) 
#         + ', y=' + str(sprite.y))

# print(message)

window.run()