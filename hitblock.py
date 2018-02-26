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

    
lavaBlockLocations()
