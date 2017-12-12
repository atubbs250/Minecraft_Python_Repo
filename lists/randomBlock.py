from mcpi.minecraft import Minecraft
mc = Minecraft.create()

import random
blocks = [3, 4, 129, 57, 56, 103]
block = random.choice(blocks)

pos = mc.player.getTilePos()
x, y, z = (pos.x), (pos.y), (pos.z)

mc.setBlock(x, y, z, block)
