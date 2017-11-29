import time
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

count = 0
while count <= 30:
    pos = mc.player.getPos()
    mc.setBlock(pos.x, pos.y, pos.z, 8)
    time.sleep(1)
    count += 1

