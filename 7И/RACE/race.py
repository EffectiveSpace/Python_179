import arcade, random

WIDTH = 600
HEIGHT = 600
TITLE = 'RACE'
IMAGE_ROAD = '7И/RACE/road.jpg'
IMAGE_CAR = '7И/RACE/car.png'
SCALE_CAR = 0.1
SPEED_CAR = 5
ANGLE = -90
DELTA_ANGLE = 15
IMAGE_BREAK = '7И/RACE/road_break.png'
SCALE_BREAK = 0.1
SPEED_BREAK = 5

class GameWindow(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.bg = arcade.load_texture(IMAGE_ROAD)
        self.car = Car(IMAGE_CAR, SCALE_CAR)
        self.brk = Break(IMAGE_BREAK, SCALE_BREAK)
        
    def setup(self):
        self.car.center_x = WIDTH - WIDTH/3
        self.car.center_y = HEIGHT/4
        self.car.angle = ANGLE
        self.brk.center_x = random.randint(0, WIDTH)
        self.brk.center_y = random.randint(HEIGHT+HEIGHT/4, HEIGHT+HEIGHT/2)
        self.brk.change_y = SPEED_BREAK
    
    def on_draw(self):
        arcade.start_render()
        arcade.draw_texture_rectangle(WIDTH/2, HEIGHT/2, WIDTH, HEIGHT, self.bg)
        self.car.draw()
        self.brk.draw()
    
    def on_update(self, delta_time):
        self.car.update()
        self.brk.update()

    def on_key_press(self, key, modifiers):
        if key == arcade.key.RIGHT:
            self.car.change_x = SPEED_CAR
            self.car.angle = ANGLE - DELTA_ANGLE
        if key == arcade.key.LEFT:
            self.car.change_x = -SPEED_CAR
            self.car.angle = ANGLE + DELTA_ANGLE
    
    def on_key_release(self, key, modifiers):
        if key == arcade.key.RIGHT or key == arcade.key.LEFT:
            self.car.change_x = 0
            self.car.angle = ANGLE

class Car(arcade.Sprite):
    def update(self):
        self.center_x += self.change_x
        if self.right > WIDTH:
            self.right = WIDTH
        if self.left < 0:
            self.left = 0

class Break(arcade.Sprite):
    def update(self):
        self.center_y -= self.change_y
        if self.top < 0:
            self.center_x = random.randint(0, WIDTH)
            self.center_y = random.randint(HEIGHT+HEIGHT/4, HEIGHT+HEIGHT/2)


window = GameWindow(WIDTH, HEIGHT, TITLE)
window.setup()
arcade.run()

    
    

