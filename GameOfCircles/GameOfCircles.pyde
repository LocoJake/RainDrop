import platform
import SpriteManager
from Bullet import Bullet
from Enemy import Enemy
from Player import Player
from SpriteManager import sprites
from Drops import Drop
from Jiggle_Bot import Jiggle
from ScreenSaverBot import Saver
from Shooter import Shooter

def setup():
    print "Built with Processing Python version " + platform.python_version()
    
    global player, sprites
    size(500, 500)
    playerTeam = 1
    enemyTeam = 2
    player = Player(width/2, height/2, playerTeam)
    SpriteManager.spawn(Shooter(200, 50, 2))
    SpriteManager.setPlayer(player)
                           
def draw():
    global player, sprites
    background(255)    
    
    for sprite in sprites:
        sprite.animate()
        
    checkCollisions()
    
def checkCollisions():
    global sprites
    for a in sprites:
        for b in sprites:
            if a.team != b.team:
                d = (pow(a.x - b.x, 2) + pow(a.y - b.y, 2))**(0.5)
                r1 = a.diameter / 2
                r2 = b.diameter / 2
                if(r1 + r2 > d):
                    sprites.remove(a)
                    sprites.remove(b)
    
def keyPressed():
    global player
    player.keyDown()    
        
def keyReleased():
    global player
    player.keyUp()
