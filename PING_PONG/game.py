import arcade

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
SCREEN_NAME = 'Ping-Pong'
SPEED_X = 2
SPEED_Y = 3

class GameWindow(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.ball = Ball('ball.png', 0.1)
        self.ball.center_x = SCREEN_WIDTH/2
        self.ball.center_y = SCREEN_HEIGHT/2
        self.ball.change_x = SPEED_X
        self.ball.change_y = SPEED_Y
    
    def on_draw(self):
        arcade.start_render()
        arcade.set_background_color((120, 150, 0))
        self.ball.draw()
        
    def on_update(self,delta_time):
        self.ball.update()

class Ball(arcade.Sprite):
    def update(self):
        self.center_x += self.change_x

    
window = GameWindow(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_NAME)
arcade.run()





