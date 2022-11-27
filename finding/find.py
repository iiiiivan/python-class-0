from pycat.core import Window, Sprite, Point, Color, KeyCode
import random
from breath_first_search import BreathFirstSearch
from pycat.base.event.mouse_event import MouseButton

w=Window()

startcell=None
endcell=None


class Boss(Sprite):
    def on_update(self, dt):
        if w.is_key_down(KeyCode.G):
            bfs=BreathFirstSearch()
            path=bfs.solve(startcell, endcell)
            for cell in path:
                if cell!=startcell and cell!=endcell:
                    cell.color=Color.BLACK



class Cell(Sprite):
    def on_create(self):
        self.image=random.choice(['ground.png', 'block.png'])
        


    def on_update(self, dt):
        pass

    def get_empty_neighbors(self):
        neighbors=[]
        points=[Point(64, 0), Point(-64, 0), Point(0, 64), Point(0, -64)]

        for point in points:
            cell=get_cell(self.position+point)
            if cell and self.image=='ground.png':
                neighbors.append(cell)

        return neighbors

    def on_click(self, mouse_event):
        global startcell, endcell
        if mouse_event.button==MouseButton.LEFT:
            if startcell!=None:
                startcell.color=Color.WHITE
            if self.image!='block.png':
                startcell=self
                startcell.color=Color.GREEN

        if mouse_event.button==MouseButton.RIGHT:
            if endcell!=None:
                endcell.color=Color.WHITE
            if self.image!='block.png':
                endcell=self
                endcell.color=Color.RED

def get_cell(position):
    for s in w.get_all_sprites():
        if s.distance_to(position)<2:
            return s
    return None

    
for i in range(10): 
    for j in range(10):
        w.create_sprite(Cell, x=64+i*64, y=64+j*64)






w.create_sprite(Boss)

w.run()