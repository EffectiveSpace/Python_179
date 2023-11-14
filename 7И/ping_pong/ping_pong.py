import arcade

WIDTH = 600
HEIGHT = 500
TITLE = 'Ping-Pong'
BALL_SPEED_X = 5
BALL_SPEED_Y = 3

class GameWindow(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.ball = Ball('ball.png', 0.15)
        self.ball.center_x = WIDTH/2
        self.ball.center_y = HEIGHT/2
        self.ball.change_x = BALL_SPEED_X
        self.ball.change_y = BALL_SPEED_Y
        
        

    def on_draw(self):
        arcade.start_render()
        arcade.set_background_color((143,237,127))
        self.ball.draw()
    
    def on_update(self, delta_time: float):
        self.ball.update()

class Ball(arcade.Sprite):
    def update(self):
        self.center_x+=self.change_x
        if self.right > WIDTH or self.left < 0:
            self.change_x*=-1
            
        self.center_y+=self.change_y
        if self.top > HEIGHT or self.bottom < 0:
            self.change_y*=-1
        
        

window = GameWindow(WIDTH, HEIGHT, TITLE)


arcade.run()
