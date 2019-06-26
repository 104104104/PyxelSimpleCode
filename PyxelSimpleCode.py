import pyxel

class App:
    def __init__(self):
        pyxel.init(160, 120)
        self.x = 10
        self.y = 10
        pyxel.run(self.update, self.draw)

    def update(self):
        self.x = self.x
        self.y = self.y

    def draw(self):
        pyxel.cls(0)
        pyxel.rect(self.x, self.y, self.x+60, self.y+60, 9)

App()
