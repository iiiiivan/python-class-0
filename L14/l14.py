from pycat.core import Color, KeyCode, Sprite, Window, Scheduler
from random import randint, random


window = Window()
health = window.create_label()

class Player(Sprite):

    def on_create(self):
        self.color = Color.AMBER
        self.x=50
        self.y=100
        self.scale = 30
        self.speed = 15
        self.health = 100
        health.text = "health = "+ str(self.health)

    def on_update(self, dt):
        if window.is_key_down(KeyCode.SPACE):
            enemy=window.get_sprites_with_tag('enemy')
            bullet=window.create_sprite(Bullet)
            min_d=1000000000
            for e in enemy:
                d=self.distance_to(e.position)
                if d<min_d:
                    min_d=d
                    bullet.point_toward_sprite(e)
        if window.is_key_pressed(KeyCode.W):
            self.y += self.speed
            if self.is_touching_any_sprite_with_tag('barrier'):
                self.y -= self.speed
        if window.is_key_pressed(KeyCode.S):
            self.y -= self.speed
            if self.is_touching_any_sprite_with_tag('barrier'):
                self.y += self.speed
        if window.is_key_pressed(KeyCode.A):
            self.x -= self.speed
            if self.is_touching_any_sprite_with_tag('barrier'):
                self.x += self.speed
        if window.is_key_pressed(KeyCode.D):
            self.x += self.speed
            if self.is_touching_any_sprite_with_tag('barrier'):
                self.x -= self.speed
        if self.health<=0:
            self.delete()
            window.close()

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
        self.add_tag('enemy')

    def on_update(self, dt):
        self.move_forward(1)
        if self.is_touching_any_sprite_with_tag('barrier'):
            self.delete()
        if self.is_touching_any_sprite_with_tag('bullet'):
            self.delete()
        if self.is_touching_window_edge():
            self.delete()
        self.time+=dt
        if self.time>5:
            b=window.create_sprite(EnemyBullet)
            b.position=self.position
            b.point_toward_sprite(player)
            self.time=0


class EnemyBullet(Sprite):

    def on_create(self):
        self.scale=15
        self.color=Color.RED
        self.add_tag('enemybullet')

    def on_update(self, dt):
        self.move_forward(2)
        if self.is_touching_window_edge():
            self.delete()
        if self.is_touching_sprite(player):
            self.delete()
            player.health-=1
            health.text="health = "+str(player.health)

class Barrier(Sprite):

    def on_create(self):
        self.width = 120
        self.height = 20
        self.color = Color.WHITE
        self.add_tag('barrier')
        self.time=10
    def on_update(self, dt):
        bullet=self.get_touching_sprites_with_tag('bullet')
        bullet+=self.get_touching_sprites_with_tag('enemybullet')
        for i in range(len(bullet)):
            bullet[i].delete() 
        self.time-=dt
        if self.time<1:
            self.delete()


b=window.create_sprite(Barrier)
b.x = 50
b.y = 150
b=window.create_sprite(Barrier)
b.x = 100
b.y = 100
b.rotation=90




def spawn_enemy():
    window.create_sprite(Enemy)


Scheduler.update(spawn_enemy, delay=0.5)

player = window.create_sprite(Player)
window.run()