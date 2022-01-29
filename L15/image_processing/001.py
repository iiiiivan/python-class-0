from pycat.core import Window
from pycat.base import NumpyImage as Image

# 10 minutes on video
# 140 on lesson
# 10 on next semester
window = Window(is_sharp_pixel_scaling=True)
image = Image(255, 255, 3)
for i in range(255):
    for j in range(255): 
        if j<85:
            image[i][j]=[255,0,0]
        elif j<170:
            image[i][j]=[0,255,0]
        else:
            image[i][j]=[0,0,255]
sprite = window.create_sprite()
sprite.texture = image.texture
sprite.position = window.center

window.run()