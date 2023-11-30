import arcade
#######################
WIDTH = 600
HEIGHT = 600
TITLE = 'RACE'
R,G,B = 100,0,255
#######################

class GameWindow(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)

    def setup(self):
        pass
    
    def on_draw(self):
        arcade.start_render()
        arcade.set_background_color((R,G,B))

    def on_update(self, delta_time):
        pass


window = GameWindow(WIDTH, HEIGHT, TITLE)
arcade.run()