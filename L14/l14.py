from pycat.core import Color, KeyCode, Sprite, Window, Scheduler
from random import randint, random

from pycat.label import Label




window = Window()
window.set_clear_color(0, 0, 153)

class Timer(Label):
    def on_create(self):
        self.time=30
        self.text='time='+str(self.time)
    def on_update(self, dt: float):
        self.time-=dt
        self.text='time='+str(round(self.time,1))
        if self.time<=20:
            Scheduler.cancel_update(spawn_enemy)
        if self.time<=0:
            window.close()
            

timer = window.create_label(Timer)

class Player(Sprite):

    def on_create(self):
        self.color = Color(51, 204, 51)
        self.x=50
        self.y=100
        self.scale = 30
        self.speed = 15
        self.health_label = window.create_label()
        self.health = 100
        self.health_label.text = "health = "+ str(self.health)
        self.health_label.font_size=11
        

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
        self.health_label.x=self.x-self.width/2
        self.health_label.y=self.y-self.height/2

    def on_left_click_anywhere(self):
        window.create_sprite(Bullet)


class Bullet(Sprite):

    def on_create(self):
        self.position=player.position   
        self.scale=15
        self.point_toward_mouse_cursor()
        self.add_tag('bullet')

    def on_update(self, dt):
        self.move_forward(7)
        if self.is_touching_window_edge():
            self.delete()

        

        
class Enemy(Sprite):
    
    def on_create(self):
        self.scale=30
        self.goto_random_position()
        self.time=0
        self.rotation=randint(0, 360)
        self.color=Color(255, 234, 0)
        self.add_tag('enemy')
        self.health = 5
        self.enemyhealth = window.create_label()
        self.enemyhealth.text = "enemy health = "+ str(self.health)
        self.enemyhealth.font_size=11
        self.enemyhealth.x=self.x-self.width/2
        self.enemyhealth.y=self.y-self.height/2

    def on_update(self, dt):
        self.move_forward(3)
        if self.is_touching_any_sprite_with_tag('barrier'):
            self.delete()
        if self.is_touching_any_sprite_with_tag('bullet'):
            self.health-=1
        if self.is_touching_window_edge():
            self.delete()
        self.time+=dt
        if self.time>0.5:
            b=window.create_sprite(EnemyBullet)
            b.position=self.position
            b.point_toward_sprite(player)
            self.time=0
        self.enemyhealth.x=self.x-self.width/2
        self.enemyhealth.y=self.y-self.height/2
        self.enemyhealth.text = "enemy health = "+ str(self.health)
        if self.health<=0:
            self.delete()

    def delete(self):
        self.enemyhealth.delete()
        return super().delete()

class EnemyBullet(Sprite):

    def on_create(self):
        self.scale=15
        self.color=Color(255, 89, 0)
        self.add_tag('enemybullet')

    def on_update(self, dt):
        self.move_forward(10)
        if self.is_touching_window_edge():
            self.delete()
        if self.is_touching_sprite(player):
            self.delete()
            player.health-=1
            player.health_label.text="health = "+str(player.health)
            print(player.health)

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




class Boss(Sprite):


    def on_create(self):
        self.scale=20
        self.goto_random_position()
        self.color=Color(255, 234, 0)
        self.rotation=randint(0, 360)
        self.x_speed=3
        self.y_speed=3
        self.time=0
        self.health = 20
        self.enemyhealth = window.create_label()
        self.enemyhealth.text = "enemy health = "+ str(self.health)
        self.enemyhealth.font_size=11
        self.enemyhealth.x=self.x-self.width/2
        self.enemyhealth.y=self.y-self.height/2


    def on_update(self, dt):
        self.x+=self.x_speed
        self.y+=self.y_speed
        if (self.x>window.width) or (self.x<0):
            self.x_speed = -self.x_speed
        if (self.y<0) or (self.y>window.height):
            self.y_speed = -self.y_speed
        if self.is_touching_any_sprite_with_tag('bullet'):
            self.health-=1
        self.time+=dt
        if self.time>0.1:
            b=window.create_sprite(EnemyBullet)
            b.position=self.position
            b.point_toward_sprite(player)
            self.time=0

        self.enemyhealth.x=self.x-self.width/2
        self.enemyhealth.y=self.y-self.height/2
        self.enemyhealth.text = "enemy health = "+ str(self.health)
        if self.health<=0 and timer.time:
            window.close()
            print('you lose')
        # if self.health<=1:
        #     print('you win')


    def delete(self):
        self.enemyhealth.delete()
        return super().delete()
window.create_sprite(Boss)

def spawn_enemy(dt):
    window.create_sprite(Enemy)

Scheduler.update(spawn_enemy, delay=0.5)
player = window.create_sprite(Player)
window.run()