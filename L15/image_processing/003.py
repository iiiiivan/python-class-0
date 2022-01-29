from re import S
from pycat.core import Window, Sprite, KeyCode
from pycat.base import NumpyImage as Image
window = Window()
original_image = Image.get_array_from_file("baboon.jpeg")
s=window.create_sprite()
rows,cols,_ = original_image.shape
s.texture=Image.get_texture_from_array(original_image)        
s.position=window.center
s.x=150
left_eye_image=original_image[190:207, 65:90, :]
left_eye=window.create_sprite()
left_eye.position=(600, 490)
left_eye.texture=Image.get_texture_from_array(left_eye_image)
left_eye.scale=4

right_eye_image=original_image[190:207, 135:160, :]
right_eye=window.create_sprite()
right_eye.position=(700, 490)
right_eye.texture=Image.get_texture_from_array(right_eye_image)
right_eye.scale=4

noth_image=original_image[155:190, 90:130, :]
noth_eye=window.create_sprite()
noth_eye.position=(650, 300)
noth_eye.texture=Image.get_texture_from_array(noth_image)
noth_eye.scale=4
window.run()