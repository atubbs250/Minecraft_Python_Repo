import time
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

pos1 = mc.player.getTilePos()
x1 = -1
y1 = 8
z1 = 8.3

time.sleep(10)

pos2 = mc.player.getTilePos()
x2 = 2
y2 = 50
z2 = 7

xDistance = x2 - x1
yDistance = y2 - y1
zDistance = z2 - z1

mc.postToChat("Yay")
