from mcpi.minecraft import Minecraft
import math
import time
import random
mc = Minecraft.create()

destX = random.randint(-127, 127)
destZ = random.randint(-127, 127)
destY = mc.getHeight(destX, destZ)

def treasureBlock():
    
    block = 57
    mc.setBlock(destX, destY, destZ, block)
    mc.postToChat("Block set")

    while True:
        pos = mc.player.getPos()
        distance = math.sqrt((pos.x - destX) ** 2 + (pos.z - destZ) ** 2)

        if distance > 100:
            mc.postToChat("On Fire!")
        elif distance > 50:
            mc.postToChat("Boiling")
        elif distance > 25:
            mc.postToChat("Warm")
        elif distance > 12:
            mc.postToChat("cold")
        elif distance > 6:
            mc.postToChat("Freezing")
        elif distance == 0:
            mc.postToChat("Found it!")
            #post to twitter
            break

def spiderBlockLocations(blockType, repeats):
    count = 0
    while count < repeats:
        x = random.randint(-127, 127)
        z = random.randint(-127, 127)
        y = mc.getHeight(x, z)
        mc.setBlock(x, y, z, blockType)
        count += 1
    while True:
        


hits = mc.events.pollBlockHits()
block = 103

for hit in hits:
    x, y, z = hit.pos.x, hit.pos.y, hit.pos.z
    mc.setBlock(x, y, z, block)


    
    blockHits = mc.events.pollBlockHits()



spiderBlockLocations(57, 5)
