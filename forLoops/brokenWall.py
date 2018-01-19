from mcpi.minecraft import Minecraft
mc = Minecraft.create()

import random

def brokenBlock():
    brokenBlocks = [48, 67, 4, 4, 4, 4]
    block = random.choice(brokenBlocks)
    return block

pos = mc.player.getTilePos()
x, y, z = pos.x, pos.y, pos.z

brokenWall = []
height, width = 5, 10

for column in range(height):
    brokenWall.append([])
    for row in range(width):
        block = brokenBlock()
        brokenWall[column].append(block)

for column in brokenWall:
    for block in column:
        mc.setBlock(x, y, z, block)
        x += 1
    y += 1
    x = pos.x
