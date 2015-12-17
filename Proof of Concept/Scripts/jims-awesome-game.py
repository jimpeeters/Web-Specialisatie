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

mc.postToChat("Have fun (or pretend to)")

pos = mc.player.getTilePos()

mc.setBlock(pos.x - 2 , pos.y , pos.z +2 , block.STONE.id)
mc.setBlock(pos.x - 1 , pos.y , pos.z +2 , block.STONE.id)
mc.setBlock(pos.x, pos.y , pos.z +2 , block.STONE.id)
mc.setBlock(pos.x + 1 , pos.y , pos.z +2 , block.STONE.id)

time.sleep(1)
mc.postToChat("Now is the time to get ready......")
time.sleep(1)
mc.postToChat("3")
time.sleep(1)
mc.postToChat("2")
time.sleep(1)                       
mc.postToChat("1")
time.sleep(1)
mc.postToChat("GO")
time.sleep(1)

blocksLit = 0
points = 0


while blocksLit < 4:
        try:
            blocksLit = blocksLit +1
            lightCreated = False
            while not lightCreated:
                randomPos = random.randint(-2, 1)
                if mc.getBlock(pos.x + randomPos, pos.y , pos.z +2) == block.STONE.id:
                    mc.setBlock(pos.x + randomPos, pos.y , pos.z +2, block.GLOWSTONE_BLOCK.id)
                    time.sleep(0.5)
                    lightCreated = True

        except if GPIO.input(11) == 1 and GPIO.input(13) == 0 and GPIO.input(7) == 0 and GPIO.input(15) == 0:
                if mc.getBlock(pos.x + 1 , pos.y , pos.z +2 ) == block.GLOWSTONE_BLOCK.id:
                    mc.setBlock(pos.x + 1 , pos.y , pos.z +2, block.STONE.id)
                    blocksLit = blocksLit - 1
                    points = points + 1
                    mc.postToChat("points = " + str(points))
                    time.sleep(0.5)
        except if GPIO.input(13) == 1 and GPIO.input(11) == 0 and GPIO.input(7) == 0 and GPIO.input(15) == 0:
                if mc.getBlock(pos.x - 1 , pos.y , pos.z +2 ) == block.GLOWSTONE_BLOCK.id:
                    mc.setBlock(pos.x - 1 , pos.y , pos.z +2, block.STONE.id)
                    blocksLit = blocksLit - 1
                    points = points + 1
                    mc.postToChat("points = " + str(points))
                    time.sleep(0.5)
        except if GPIO.input(7) == 1 and GPIO.input(13) == 0 and GPIO.input(11) == 0 and GPIO.input(15) == 0:
                if mc.getBlock(pos.x , pos.y , pos.z +2 ) == block.GLOWSTONE_BLOCK.id:
                    mc.setBlock(pos.x  , pos.y , pos.z +2, block.STONE.id)
                    blocksLit = blocksLit - 1
                    points = points + 1
                    mc.postToChat("points = " + str(points))
                    time.sleep(0.5)
        except if GPIO.input(15) == 1 and GPIO.input(13) == 0 and GPIO.input(7) == 0 and GPIO.input(11) == 0:
                 if mc.getBlock(pos.x - 2 , pos.y , pos.z +2 ) == block.GLOWSTONE_BLOCK.id:
                    mc.setBlock(pos.x - 2 , pos.y , pos.z +2, block.STONE.id)
                    blocksLit = blocksLit - 1
                    points = points + 1
                    mc.postToChat("points = " + str(points))
                    time.sleep(0.5)
        

mc.postToChat("Game over - points = " + str(points))

