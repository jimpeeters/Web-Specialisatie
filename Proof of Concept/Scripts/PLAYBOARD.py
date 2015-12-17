#! /usr/bin/python
"""import mcpi.minecraft as minecraft"""
from mcpi.minecraft import Minecraft
import mcpi.block as block
import random
import RPi.GPIO as GPIO
import time


mc = Minecraft.create()

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(15, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def drawBuilding( locx, locy, locz, floors, width, depth, floorheight, wallmaterial, floormaterial ):
    topx = locx+width
    topy = locy+((floorheight+1)*floors)
    topz = locz+depth
    #draw building shell
    mc.setBlocks( locx, locy, locz, topx, topy, topz, wallmaterial )
    mc.setBlocks( locx+1, locy+1, locz+1, topx-1, topy-1, topz-1, block.AIR )
    #draw floors
    if( floors > 1 ):
        for i in range( floors -1 ):
            floorYloc = locy+( (floorheight+1)*(i+1) )
            mc.setBlocks( locx+1, floorYloc, locz+1, topx-1, floorYloc, topz-1, floormaterial )
    #draw door
    doorloc = random.randint( 1, width-2 )
    mc.setBlock( locx, locy+1, locz+doorloc, block.AIR )
    mc.setBlock( locx, locy+2, locz+doorloc, block.AIR )
    #draw front windows
    if( floors > 1 ):
        for i in range( floors-1 ):
            windowYloc = locy+2+( (floorheight+1)*(i+1) )
            for j in range( floorheight-1 ):
                mc.setBlocks( locx, windowYloc+j , locz+1, locx, windowYloc+j, locz+(width-1), block.GLASS_PANE )
    #draw back windows
    if( floors > 1 ):
        for i in range( floors-1 ):
            windowYloc = locy+2+( (floorheight+1)*(i+1) )
            for j in range( floorheight-1 ):
                mc.setBlocks( locx+depth, windowYloc+j , locz+1, locx+depth, windowYloc+j, locz+(width-1), block.GLASS_PANE )


def drawTree(xpos, ypos, zpos):
    wood = 17
    leave = 18
    mc.setBlock(xpos+2, ypos, zpos, wood)
    time.sleep(0.5)
    mc.setBlock(xpos+2, ypos+1, zpos, wood)
    time.sleep(0.5)
    mc.setBlock(xpos+2, ypos+2, zpos, wood)
    time.sleep(0.5)
    mc.setBlock(xpos+2, ypos+3, zpos, wood)
    time.sleep(0.5)
    mc.setBlock(xpos+2, ypos+4, zpos, wood)
    time.sleep(0.5)
    mc.setBlock(xpos+2, ypos+5, zpos, wood)
    time.sleep(0.5)
    for x in range(5, 8):
        mc.setBlock(xpos+3, ypos+x, zpos, leave)
        time.sleep(0.1)
        mc.setBlock(xpos+3, ypos+x, zpos+1, leave)
        time.sleep(0.1)
        mc.setBlock(xpos+3, ypos+x, zpos-1, leave)
        time.sleep(0.1)
        mc.setBlock(xpos+2, ypos+x, zpos+1, leave)
        time.sleep(0.1)
        mc.setBlock(xpos+1, ypos+x, zpos+1, leave)
        time.sleep(0.1)
        mc.setBlock(xpos+1, ypos+x, zpos-1, leave)
        time.sleep(0.1)
        mc.setBlock(xpos+1, ypos+x, zpos, leave)
        time.sleep(0.1)
        mc.setBlock(xpos+2, ypos+x, zpos-1, leave)
        time.sleep(0.1)
        mc.setBlock(xpos+2, ypos+x, zpos, leave)
        time.sleep(0.1)


def drawStairs(xpos, ypos, zpos):
    for x in range(0, 100):
        mc.setBlock(xpos+x, ypos+x, zpos, 57)
        time.sleep(0.1)
        mc.setBlock(xpos+x, ypos+x, zpos+1, 57)
        time.sleep(0.1)
        mc.setBlock(xpos+x, ypos+x, zpos-1, 57)
        time.sleep(0.1)

    

  
try:
    while True:
        if(GPIO.input(11) == 1):
            print('Spawn house')
            x, y, z = mc.player.getPos()
            drawBuilding( x+10, y, z, 5, 5, 5, 3, block.STONE, block.WOOD_PLANKS )
            time.sleep(0.2)
        elif(GPIO.input(13) == 1):
            print('Generate tree')
            x, y, z = mc.player.getPos()
            drawTree(x+8,y,z)
            time.sleep(0.2)
        elif(GPIO.input(7) == 1):
            print('Generate stair')
            x, y, z = mc.player.getPos()
            drawStairs(x+8,y,z)
            time.sleep(0.2)

                

except KeyboardInterrupt:
    GPIO.cleanup()

