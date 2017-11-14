from mcpi.minecraft import Minecraft
mc = Minecraft.create()

pos = mc.player.getPos()
x = pos.x
y = pos.y
z = pos.z

blockType = mc.getBlock(x, y, z)
mc.postToChat(blockType == 2)

underwater = blockType == y - 1
drowning = blockType == y - 2

mc.postToChat("The player is drowning: " + str(drowning))
mc.postToChat("The player is standing in water: " + str(underwater))


