from pycat.core import Window
from pycat.sprite import Sprite
window = Window()
# x =input("enter x")
# y =input("enter y")

class Owl(Sprite):
    
    def on_create(self):
        
        self.scale=0.01
        self.image="owl.gif"
        self.goto_random_position()
class Fireball(Sprite):
    
    def on_create(self):
        
        self.scale=0.01
        self.image="fireball.gif"
        self.goto_random_position()

for i in range(5):
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