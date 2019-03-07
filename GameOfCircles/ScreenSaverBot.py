class Saver:
    speed = 8
    xspeed = 8
    yspeed = 2
    diameter = 50
    c = color(255,0,255)
    
    def __init__(self, x, y, team):
        self.x = x
        self.y = y
        self.team = team
        self.speed = 8
        
    def move(self):
        self.x += self.xspeed
        self.y += self.yspeed
        
        if self.y < 0 or self.y > height:
            self.yspeed *= -1
        if self.x < 0 or self.x > width:
            self.xspeed *= -1
