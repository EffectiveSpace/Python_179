import arcade, random
#######################
WIDTH = 600
HEIGHT = 600
TITLE = 'RACE'
R,G,B = 100,0,255
FONT = '7ИТ/RACE/font_race.jpg'
CAR = '7ИТ/RACE/car.png'
CAR_SCALE = 0.2
CAR_SPEED = 5
DELTA_ANGLE = 15
BREAK = '7ИТ/RACE/road_break.png'
SCALE_BREAK = 0.1
#######################

class GameWindow(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.bg = arcade.load_texture(FONT)
        self.car = Car(CAR, CAR_SCALE)
        self.break_road = Break(BREAK, SCALE_BREAK)

    def setup(self):
        self.car.center_x = WIDTH - WIDTH/3
        self.car.center_y = HEIGHT/4
        self.car.angle = -90
        self.break_road.center_x = random.randint(WIDTH/6, WIDTH)
        self.break_road.change_y = random.randint(3,10)
    
    def on_draw(self):
        arcade.start_render()
        arcade.draw_texture_rectangle(WIDTH/2, HEIGHT/2, WIDTH, HEIGHT, self.bg)
        self.car.draw()
        self.break_road.draw()

    def on_update(self, delta_time):
        self.car.update()
        self.break_road.update()

    def on_key_press(self, key, modifiers):
        if key == arcade.key.LEFT:
            self.car.change_x = -CAR_SPEED
            self.car.angle += DELTA_ANGLE
        if key == arcade.key.RIGHT:
            self.car.change_x = CAR_SPEED
            self.car.angle -= DELTA_ANGLE
    
    def on_key_release(self, key, modifiers):
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.car.change_x = 0
            self.car.angle = -90

class Car(arcade.Sprite):
    def update(self):
        self.center_x+=self.change_x

class Break(arcade.Sprite):
    def update(self):
        self.center_y-=self.change_y
        if self.top < 0:
            self.bottom = HEIGHT

window = GameWindow(WIDTH, HEIGHT, TITLE)
window.setup()
arcade.run()