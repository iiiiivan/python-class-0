from re import S
from pycat.core import Window, Sprite, KeyCode
from pycat.base import NumpyImage as Image
window = Window()
original_image = Image.get_array_from_file("baboon.jpeg")
s=window.create_sprite()
rows,cols,_ = original_image.shape
for i in range(rows):
    for j in range(cols):
        r,g,b,a=original_image[i][j]
        r=255-r
        g=255-g
        b=255-b
        original_image[i][j]=[r,g,b,a]
s.texture=Image.get_texture_from_array(original_image)        
s.position=window.center
window.run()