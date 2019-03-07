class Drop:
    
    speed = 8
    diameter = 20
    c = color(0,0,255)
    
    def __init__(self, x, y, team):
        self.x = x
        self.y = y
        self.team = team
        
    def move(self):
        self.y += self.speed
        if self.y < 0 or self.y > height:
            self.speed *= -1
        if self.y > height:
            self.y = 0
