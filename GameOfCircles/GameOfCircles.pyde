import platform
import SpriteManager
from Bullet import Bullet
from Enemy import Enemy
from Player import Player
from Drops import Drop
from Jiggle_Bot import Jiggle
from ScreenSaverBot import Saver
from Shooter import Shooter
from Zombie import Zombie
from Zombie_Spawner import Zombie_Spawner

def setup():
    print "Built with Processing Python version " + platform.python_version()
    
    global player, sprites
    size(500, 500)
    playerTeam = 1
    enemyTeam = 2
    player = Player(width/2, height/2, playerTeam)
    #SpriteManager.spawn(Shooter(200, 50, 2))
    SpriteManager.spawn(Zombie_Spawner(250, 0, 2))
    SpriteManager.spawn(Zombie(250, 50, 2))
    SpriteManager.setPlayer(player)
                           
def draw():
    background(255)    
    SpriteManager.animate()
    
def keyPressed():
    SpriteManager.player.keyDown()    
        
def keyReleased():
    SpriteManager.player.keyUp()
