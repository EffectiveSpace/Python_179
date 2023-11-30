import arcade
#######################
WIDTH = 600
HEIGHT = 600
TITLE = 'RACE'
R,G,B = 100,0,255
FONT = '7ИТ/RACE/font_race.jpg'
CAR = '7ИТ/RACE/car.png'
CAR_SCALE = 0.2
#######################

class GameWindow(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.bg = arcade.load_texture(FONT)
        self.car = Car(CAR, CAR_SCALE)

    def setup(self):
        self.car.center_x = WIDTH - WIDTH/3
        self.car.center_y = HEIGHT/4
        self.car.angle = -90
    
    def on_draw(self):
        arcade.start_render()
        arcade.draw_texture_rectangle(WIDTH/2, HEIGHT/2, WIDTH, HEIGHT, self.bg)
        self.car.draw()

    def on_update(self, delta_time):
        pass


class Car(arcade.Sprite):
    pass

window = GameWindow(WIDTH, HEIGHT, TITLE)
window.setup()
arcade.run()