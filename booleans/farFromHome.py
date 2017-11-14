from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import math
homeX = 18.9
homeY = 41.0
homeZ = 27.7
pos = mc.player.getTilePos()
x = pos.x
y = pos.y
z = pos.z
distance = math.sqrt((homeX - x) ** 2 + (homeY - y) ** 2 + (homeZ -z) ** 2)
mc.postToChat(distance)
nearby = distance <= 50
mc.postToChat("The player is near their home: " + str(nearby))

