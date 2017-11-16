from mcpi.minecraft import Minecraft
mc = Minecraft.create()

x = 37.9
y = 7.0
z = 0.6

blockType = mc.getBlock(x, y, z)

melon = blockType == 103
noMelon = not melon

mc.postToChat("You need to get some food: " + str(noMelon))
