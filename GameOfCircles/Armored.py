import SpriteManager
from Sprite import Sprite

class Armored(Sprite):
    armor = 10
    c = color(0)
    
    def display(self):
        #stroke(100)
        strokeWeight(armor)
        ellipse(self.x, self.y, self.diameter, self.diameter)
        noStroke()
        
def handleCollision(self):
    self.armor -= 1
    if self.armor < 1:
        SpriteManager.destroy(self)
