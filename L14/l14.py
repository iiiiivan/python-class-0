from pycat.core import Color, KeyCode, Sprite, Window, Scheduler
from random import randint, random


window = Window()
health = window.create_label()

class Player(Sprite):

    def on_create(self):
        self.color = Color.AMBER
        self.scale = 30
        self.speed = 10
        self.health = 100
        health.text = "health = "+ str(self.health)

    def on_update(self, dt):
        if window.is_key_pressed(KeyCode.W):
            self.y += self.speed
        if window.is_key_pressed(KeyCode.S):
            self.y -= self.speed
        if window.is_key_pressed(KeyCode.A):
            self.x -= self.speed
        if window.is_key_pressed(KeyCode.D):
            self.x += self.speed
          
    def on_left_click_anywhere(self):
        window.create_sprite(Bullet)

class Bullet(Sprite):

    def on_create(self):
        self.position=player.position   
        self.scale=15
        self.point_toward_mouse_cursor()
        self.add_tag('bullet')

    def on_update(self, dt):
        self.move_forward(5)
        if self.is_touching_window_edge():
            self.delete()

        
class Enemy(Sprite):
    
    def on_create(self):
        self.scale=30
        self.goto_random_position()
        self.time=0
        self.rotation=randint(0, 360)
        self.color=Color.RED

    def on_update(self, dt):
        self.move_forward(5)
        if self.is_touching_any_sprite_with_tag('bullet'):
            self.delete()
        if self.is_touching_window_edge():
            self.delete()
        self.time+=dt
        if self.time>1:
            b=window.create_sprite(EnemyBullet)
            b.position=self.position
            b.point_toward_sprite(player)
            self.time=0



class EnemyBullet(Sprite):

    def on_create(self):
        self.scale=15
        self.color=Color.RED
        
    def on_update(self, dt):
        self.move_forward(7)
        if self.is_touching_window_edge():
            self.delete()
        if self.is_touching_sprite(player):
            self.delete()
            player.health-=1
            health.text="health = "+str(player.health)

class Barrier(Sprite):

    def on_create(self):
        self.width = 100
        self.height = 20
        self.color = Color.WHITE
b=window.create_sprite(Barrier)
b.x = 1000
b.y = 600


def spawn_enemy():
    window.create_sprite(Enemy)


Scheduler.update(spawn_enemy, delay=0.5)

player = window.create_sprite(Player)
window.run()