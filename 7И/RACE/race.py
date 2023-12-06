import arcade

WIDTH = 600
HEIGHT = 600
TITLE = ''
IMAGE_ROAD = '7И/RACE/road.jpg'
IMAGE_CAR = '7И/RACE/car.png'
SCALE_CAR = 0.1

class GameWindow(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.bg = arcade.load_texture(IMAGE_ROAD)
        self.car = Car(IMAGE_CAR, SCALE_CAR)
        
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

    
    

