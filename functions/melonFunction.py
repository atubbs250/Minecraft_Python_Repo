from mcpi.minecraft import Minecraft
mc = Minecraft.create()

import time

def underPlayer():
    pos = mc.player.getPos()
    x = pos.x
    y = pos.y
    z = pos.z
    mc.setBlock(x, y-1, z, 103)
    print("working")
    time.sleep(10)

underPlayer()
underPlayer()
underPlayer()
