from mcpi.minecraft import Minecraft
import math
import time
import random
import threading
from threading import Thread
mc = Minecraft.create()

destX = random.randint(-127, 127)
destZ = random.randint(-127, 127)
destY = mc.getHeight(destX, destZ)

def progressBar():
    pos = mc.player.getTilePos()
    x = pos.x + 1
    y = pos.y
    z = pos.z

    blocks = [20, 20, 20, 20, 20, 20, 20, 20, 20, 20]
    barBlock = 22

    count = 0
    while count <= len(blocks):

        mc.setBlock(x, y + 9, z, blocks[0])
        mc.setBlock(x, y + 8, z, blocks[1])
        mc.setBlock(x, y + 7, z, blocks[2])
        mc.setBlock(x, y + 6, z, blocks[3])
        mc.setBlock(x, y + 5, z, blocks[4])
        mc.setBlock(x, y + 4, z, blocks[5])
        mc.setBlock(x, y + 3, z, blocks[6])
        mc.setBlock(x, y + 2, z, blocks[7])
        mc.setBlock(x, y + 1, z, blocks[8])
        mc.setBlock(x, y, z, blocks[9])

        count += 1

        del blocks[9]
        blocks.insert(0, barBlock)
        mc.postToChat("Hurry up, you are losing time!")

        time.sleep(10)


def treasureBlock():
    
    destX = random.randint(-127, 127)
    destZ = random.randint(-127, 127)
    destY = mc.getHeight(destX, destZ)

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
            finalPos = mc.player.getTilePos()
            mc.setBlocks(finalPos.x - 5, finalPos.y + 10, finalPos.z - 5, finalPos.x + 5, finalPos.y + 10, finalPos.z + 5, 38)
            #post to twitter
            
    pos = mc.player.getTilePos()
    x = pos.x + 1
    y = pos.y
    z = pos.z

    blocks = [20, 20, 20, 20, 20, 20, 20, 20, 20, 20]
    barBlock = 22

    count = 0
    while count <= len(blocks):

        mc.setBlock(x, y + 9, z, blocks[0])
        mc.setBlock(x, y + 8, z, blocks[1])
        mc.setBlock(x, y + 7, z, blocks[2])
        mc.setBlock(x, y + 6, z, blocks[3])
        mc.setBlock(x, y + 5, z, blocks[4])
        mc.setBlock(x, y + 4, z, blocks[5])
        mc.setBlock(x, y + 3, z, blocks[6])
        mc.setBlock(x, y + 2, z, blocks[7])
        mc.setBlock(x, y + 1, z, blocks[8])
        mc.setBlock(x, y, z, blocks[9])

        count += 1

        del blocks[9]
        blocks.insert(0, barBlock)
        mc.postToChat("Hurry up, you are losing time!")

        time.sleep(10)
        

def spiderBlockLocations():

    block = 57
    count = 0
    while count < 5:
        x = random.randint(-127, 127)
        z = random.randint(-127, 127)
        y = mc.getHeight(x, z)
        mc.setBlock(destX, destY, destZ, block)
        count += 1
    
    hits = mc.events.pollBlockHits()
    block = 30

    for hit in hits:
        x, y, z = hit.pos.x, hit.pos.y, hit.pos.z
        mc.setBlock(x, y, z, block)
    

def lavaBlockLocations():

    block = 57
    count = 0
    while count < 5:
        x = random.randint(-127, 127)
        z = random.randint(-127, 127)
        y = mc.getHeight(x, z)
        mc.setBlock(destX, destY, destZ, block)
        count += 1
    
    hits = mc.events.pollBlockHits()
    block = 10

    for hit in hits:
        x, y, z = hit.pos.x, hit.pos.y, hit.pos.z
        mc.setBlock(x, y, z, block)



def sandFallLocations():

    block = 57
    count = 0
    while count < 5:
        x = random.randint(-127, 127)
        z = random.randint(-127, 127)
        y = mc.getHeight(x, z)
        mc.setBlock(destX, destY, destZ, block)
        count += 1
    
    hits = mc.events.pollBlockHits()
    block = 12

    for hit in hits:
        x, y, z = hit.pos.x, hit.pos.y + 3, hit.pos.z
        mc.setBlock(x, y, z, block)


if __name__ == '__main__':
    Thread(target = progressBar).start()
    Thread(target = treasureBlock).start()
    Thread(target = spiderBlockLocations).start()
    Thread(target = lavaBlockLocations).start()
    Thread(target = sandFallLocations).start()
    


