mark = 0
wait = 1000
go = True
from Bullet import Bullet
from Sprite import Sprite
from Player import Player
import SpriteManager
from Enemy import Enemy

class Shooter(Sprite):
    
    speed = 4
    xspeed = 4
    #yspeed = 2
    diameter = 50
    c = color(0, 0, 255)
    
    def _init_(self, x, y, team):
        self.x = x
        self.y = y
        self.team = team
        
    def move(self):
        self.x += self.speed
        #self.y += self.yspeed
        
        vector = self.aim(SpriteManager.getPlayer())
        self.fire(vector)
        
        self.x += self.speed
        if self.x < 0 or self.x > width:
            self.speed *= -1
            
    def display(self):
        fill(self.c)
        ellipse(self.x, self.y, self.diameter, self.diameter)
            
    def animate(self):
        self.move()
        self.display()
            
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
            SpriteManager.spawn(Bullet(self.x, self.y, vector, self.team))
