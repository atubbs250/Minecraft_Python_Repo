from mcpi.minecraft import Minecraft
mc = Minecraft.create()

buildX = 2.0
buildY = 0.0
buildZ = -8.0
width = 11
height = 6
length = 7

pos = mc.player.getTilePos()
x = pos.x
y = pos.y
z = pos.z

inside = buildX < x < buildX + width and buildY < y < buildY + height and buildZ < z < buildZ + length
mc.postToChat("The player is home: " + str(inside))

