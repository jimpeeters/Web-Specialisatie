from mcpi.minecraft import Minecraft
from time import sleep

mc = Minecraft.create()
tnt = 46
while True:
        x, y, z = mc.player.getPos()
        mc.setBlock(x,y,z,tnt,1)
        sleep(0.1)

        
