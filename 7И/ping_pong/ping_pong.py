import arcade

WIDTH = 600
HEIGHT = 500
TITLE = 'Ping-Pong'
BALL_SPEED_X = 5
BALL_SPEED_Y = 3
PAD_SPEED = 5

class GameWindow(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.ball = Ball('7И/ping_pong/ball.png', 0.15)
        self.pad = Pad('7И/ping_pong/paddle.png', 0.15)
        self.ball.center_x = WIDTH/2
        self.ball.center_y = HEIGHT/2
        self.ball.change_x = BALL_SPEED_X
        self.ball.change_y = BALL_SPEED_Y
        self.pad.center_x = WIDTH/2
        self.pad.center_y = HEIGHT/4
        
        

    def on_draw(self):
        arcade.start_render()
        arcade.set_background_color((143,237,127))
        self.ball.draw()
        self.pad.draw()
    
    def on_update(self, delta_time: float):
        self.ball.update()
        self.pad.update()
        if arcade.check_for_collision(self.ball, self.pad):
            self.ball.change_y = -self.ball.change_y
            
        
    def on_key_press(self, key, modifiers):
        if key == arcade.key.LEFT:
            self.pad.change_x = -PAD_SPEED
        if key == arcade.key.RIGHT:
            self.pad.change_x = PAD_SPEED
            
    def on_key_release(self, key, modifiers):
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.pad.change_x = 0

class Ball(arcade.Sprite):
    def update(self):
        self.center_x+=self.change_x
        if self.right > WIDTH or self.left < 0:
            self.change_x*=-1
            
        self.center_y+=self.change_y
        if self.top > HEIGHT or self.bottom < 0:
            self.change_y*=-1
        
class Pad(arcade.Sprite):
    def update(self):
        self.center_x+=self.change_x
        if self.right > WIDTH:
            self.right = WIDTH
        if self.left < 0:
            self.left = 0

window = GameWindow(WIDTH, HEIGHT, TITLE)


arcade.run()
