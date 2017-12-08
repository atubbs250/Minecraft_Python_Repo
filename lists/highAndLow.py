from mcpi.minecraft import Minecraft
mc = Minecraft.create()

import time

heights = [100, 0]
count = 0

while count < 60:
    pos = mc.player.getTilePos()

    if pos.y < heights[0]:

    elif pos.y > heights[1]:

    count += 1
    time.sleep(1)

mc.postToChat("Lowest: ")
mc.postToChat("Highest: ")
