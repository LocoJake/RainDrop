mark = 0
wait = 2000
go = True
from Zombie import Zombie
from Sprite import Sprite
from Player import Player
import SpriteManager

class Zombie_Spawner(Sprite):
    
    speed = 0
    c = color(155, 200, 40)
    diameter = 100
    
    def __init__(self, x, y, team):
        
        self.x = x
        self.y = y
        self.team = team
        
    def move(self):
        
        vector = self.aim(SpriteManager.getPlayer())
        self.fire(vector)
        
    def aim(self, target):
        
        xDist = self.x - target.x
        yDist = self.y - target.y
        d = ((self.x - target.x)**2 + (self.y - target.y)**2)**.5
        xVec = -xDist / 2 * .01
        yVec = -yDist / 2 * .01
        return PVector(xVec, yVec)
        return PVector(0, 10)
        
    def fire(self, vector):
        global go, mark, wait
        if (millis() - mark > wait):
            go = not go
            mark = millis()
        if(go):
            go = False
            SpriteManager.spawn(Zombie(self.x, self.y, self.team))
            
    def handleCollision(self):
        pass
