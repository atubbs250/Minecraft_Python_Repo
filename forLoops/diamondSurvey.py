from mcpi.minecraft import Minecraft
mc = Minecraft.create()

pos = mc.player.getTilePos()
x = pos.x
y = pos.y
z = pos.z

depth = 50

for under in range(depth):
    block = mc.getBlock(x, y - under, z)
    if block == 56:
        mc.postToChat("A diamond is " + str(under) + " blocks below you.")
        break
else:
    mc.postToChat("There are no diamonds below you.")
