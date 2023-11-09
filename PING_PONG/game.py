import arcade
import random

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
SCREEN_NAME = 'Ping-Pong'
SPEED_X = random.randint(5, 10)
SPEED_Y = random.randint(5, 10)
SPEED_PAD = 3

class GameWindow(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.ball = Ball('ball.png', 0.1)
        self.pad = Pad('paddle.png', 0.2)
        self.ball.center_x = SCREEN_WIDTH/2
        self.ball.center_y = SCREEN_HEIGHT/2
        self.ball.change_x = SPEED_X
        self.ball.change_y = SPEED_Y
        self.pad.center_x = SCREEN_WIDTH/2
        self.pad.center_y = SCREEN_HEIGHT/3
    
    def on_draw(self):
        arcade.start_render()
        arcade.set_background_color((180, 120, 180))
        self.ball.draw()
        self.pad.draw()
        
    def on_update(self,delta_time):
        self.ball.update()

    def on_key_press(self, key, modifiers):
        if key == arcade.key.LEFT:
            self.pad.change_x = -SPEED_PAD
        if key == arcade.key.RIGHT:
            self.pad.change_y = SPEED_PAD

class Ball(arcade.Sprite):
    def update(self):
        self.center_x += self.change_x
        if self.right > SCREEN_WIDTH or self.left < 0:
            self.change_x *=-1
        self.center_y += self.change_y
        if self.top > SCREEN_HEIGHT or self.bottom < 0:
            self.change_y*=-1

class Pad(arcade.Sprite):
    pass
    
window = GameWindow(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_NAME)
arcade.run()





