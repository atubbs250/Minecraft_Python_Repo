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

        time.sleep(10)

    block = 51
    mc.setBlocks(pos.x, pos.y, pos.z, block)
    mc.postToChat("You lose! Good day sir!")
    quit(treasureBlock)

def treasureBlock():
    from mcpi.minecraft import Minecraft
    import math
    import time
    import random
    import threading
    from threading import Thread
    import sys
    mc = Minecraft.create()

    pos = mc.player.getTilePos()
    x, y, z = pos.x, pos.y, pos.z
    
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
            mc.postToChat("Think differently!")
        elif distance > 50:
            mc.postToChat("Boiling!")
            mc.postToChat("Think differently!")
        elif distance > 25:
            mc.postToChat("Warm")
        elif distance > 12:
            mc.postToChat("cold")
        elif distance > 6:
            mc.postToChat("Freezing!")
            mc.postToChat("closer!")
        elif distance < 3:
            mc.postToChat("Found it!")
            finalPos = mc.player.getTilePos()
            mc.setBlocks(finalPos.x - 5, finalPos.y + 10, finalPos.z - 5, finalPos.x + 5, finalPos.y + 10, finalPos.z + 5, 38)
            time.sleep(5)
            quit(progressBar)
            break


def spiderBlockLocations():
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

    block = 57
    mc.setBlock(destX, destY, destZ, block)
    mc.postToChat("SBlock set")

    while True:
        pos = mc.player.getPos()
        distance = math.sqrt((pos.x - destX) ** 2 + (pos.z - destZ) ** 2)
        block = 30
        if distance < 3:
            mc.setBlock(destX, destY, destZ, block)
            mc.postToChat("Whahahahahahahahahahaha")
            mc.setBlocks(pos.x, pos.y, pos.z, block)

def lavaBlockLocations():
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

    block = 57
    mc.setBlock(destX, destY, destZ, block)
    mc.postToChat("LBlock set")

    while True:
        pos = mc.player.getPos()
        distance = math.sqrt((pos.x - destX) ** 2 + (pos.z - destZ) ** 2)
        block = 10
        if distance < 3:
            mc.setBlock(destX, destY, destZ, block)
            mc.postToChat("Whahahahahahahahahahaha")



def TNTLocations():
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

    block = 57
    mc.setBlock(destX, destY, destZ, block)
    mc.postToChat("PBlock set")

    while True:
        pos = mc.player.getPos()
        distance = math.sqrt((pos.x - destX) ** 2 + (pos.z - destZ) ** 2)
        TNT = 46
        state = 1
        if distance < 3:
            mc.setBlock(destX, destY, destZ, 46)
            mc.setBlocks(destX + 3, destY + 3, destZ + 3, destX - 3, destY - 3, destZ - 3, 0)
            mc.postToChat("Whahahahahahahahahahaha")


if __name__ == '__main__':
    Thread(target = treasureBlock).start()
    Thread(target = progressBar).start()
    Thread(target = spiderBlockLocations).start()
    Thread(target = spiderBlockLocations).start()
    Thread(target = spiderBlockLocations).start()
    Thread(target = spiderBlockLocations).start()
    Thread(target = spiderBlockLocations).start()
    Thread(target = lavaBlockLocations).start()
    Thread(target = lavaBlockLocations).start()
    Thread(target = lavaBlockLocations).start()
    Thread(target = lavaBlockLocations).start()
    Thread(target = lavaBlockLocations).start()
    Thread(target = TNTLocations).start()
    Thread(target = TNTLocations).start()
    Thread(target = TNTLocations).start()
    Thread(target = TNTLocations).start()
    Thread(target = TNTLocations).start()
    
    


