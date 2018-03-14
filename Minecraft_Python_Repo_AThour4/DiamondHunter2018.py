
''' In this program, you will have to find a diamond within a certain
amount of time. Fake diamonds will be places to throw off the player as well as
opposite wording in order to find the winning diamond.
This project was created by David Eubank, Karam Qaoud, and Amanda Tubbs on
03/14/18.'''

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


'''lets the player know that the game is beginning and to find a diamond
within a 100 sec time limit'''

def beginning():
    mc.postToChat("Welcome! Try to find the diamond before 100 sec go by!")


'''This is the code for the progress bar. It is a 100 sec timer and will tell
the player that they lost and quit the program if time runs out. It displays
time by changing glass blocks to blue blocks from the top to bottom every
ten seconds'''

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
    mc.setBlock(pos.x, pos.y, pos.z, block)
    mc.postToChat("Time ran out!")
    quit(treasureBlock)


'''This code is for the winning diamond. In order to find it, the player will
have to get colder instead of warmer, but they have to figure that out
themselves. When the diamond is found within the aloted time they will be
prompted to write their name in the shell. They will be posted to the
projects twitter (@PythonTreasureHunt), saying that they won the game.'''

def treasureBlock():
    from mcpi.minecraft import Minecraft
    import math
    import time
    import random
    import threading
    from threading import Thread
    import sys
    from twython import Twython

    from auth import (
        consumer_key,
        consumer_secret,
        access_token,
        access_token_secret
    )

    twitter = Twython(
        consumer_key,
        consumer_secret,
        access_token,
        access_token_secret
    )


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
            mc.postToChat("Enter your name in the shell")
            finalPos = mc.player.getPos()
            mc.setBlocks(finalPos.x - 5, finalPos.y + 10, finalPos.z - 5, finalPos.x + 5, finalPos.y + 10, finalPos.z + 5, 38)
            name = input("What is your name?: ")
            message = "Woo Hoo! " + str(name) + " won David, Karam, and Amanda's python game!"
            twitter.update_status(status=message)
            print("Tweeted: %s" % message)
            quit(progressBar)
            break


''' This program will be used to trick the player by placing 5
disguised diamond blocks in random locations, that if the player
is within a three block radius they will be stuck in spider webs. They will
also be caught in the air whenever they fly over them. '''

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

    while True:
        pos = mc.player.getPos()
        distance = math.sqrt((pos.x - destX) ** 2 + (pos.z - destZ) ** 2)
        block = 30
        if distance < 2:
            mc.setBlock(destX, destY, destZ, block)
            mc.postToChat("Whahahahahahahahahahaha")
            mc.setBlock(pos.x, pos.y, pos.z, block)


'''This program places 5 fake diamonds in the world
which turns into a hug pile of lava to get you stuck if you get close within
a 3 block radius to them.'''

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

    while True:
        pos = mc.player.getPos()
        distance = math.sqrt((pos.x - destX) ** 2 + (pos.z - destZ) ** 2)
        block = 10
        if distance < 3:
            mc.setBlock(destX, destY, destZ, block)
            mc.setBlocks(destX + 1, destY + 1, destZ + 1, destX - 1, destY - 1, destZ - 1, block)
            mc.postToChat("Whahahahahahahahahahaha")


'''This program creates a hole that the player will fall into if they walk
up to the diamond. This hole is very large and will require flight to get
out. There will be 5 of these placed randomly.'''

def holeLocations():
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

    while True:
        pos = mc.player.getPos()
        distance = math.sqrt((pos.x - destX) ** 2 + (pos.z - destZ) ** 2)
        air = 0
        if distance < 3:
            mc.setBlock(destX, destY, destZ, 0)
            mc.setBlocks(destX + 1, destY + 50, destZ + 1, destX - 1, destY - 50, destZ - 3, 0)
            


beginning()
time.sleep(3)
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
    Thread(target = holeLocations).start()
    Thread(target = holeLocations).start()
    Thread(target = holeLocations).start()
    Thread(target = holeLocations).start()
    Thread(target = holeLocations).start()    


