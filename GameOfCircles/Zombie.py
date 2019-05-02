# This will be an enemy type that follows the player and gradually speeds up over time if it doesn't touch the player.
mark = 0
wait = 500
go = True
from Sprite import Sprite
from Player import Player
import SpriteManager

class Zombie(Sprite):
    
    speed = 1
    c = color(0, 255, 0)
    
    def __init__(self, x, y, team):
        self.x = x
        self.y = y
        self.team = team
        
    def aim(self, target):
        
        target = SpriteManager.getPlayer()
        xDist = self.x - target.x
        yDist = self.y - target.y
        d = ((self.x - target.x)**2 + (self.y - target.y)**2)**.5
        xVec = -xDist / 2 * .01
        yVec = -yDist / 2 * .01
        return PVector(xVec, yVec)
        return PVector(0, 10)
    
    def move(self):
        target = SpriteManager.getPlayer()
        xDist = self.x - target.x
        yDist = self.y - target.y
        d = ((target.x - self.x)**2 + (target.y - self.y)**2)**.5
        moving = PVector((xDist / d) * 2, (yDist / d) * 2)
        self.x -= moving.x
        self.y -= moving.y
            
