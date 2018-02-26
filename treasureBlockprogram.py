from mcpi.minecraft import Minecraft
import math
import time
import random
import threading
from threading import Thread
mc = Minecraft.create()


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

treasureBlock()
