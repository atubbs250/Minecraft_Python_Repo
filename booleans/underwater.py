from mcpi.minecraft import Minecraft
mc = Minecraft.create()

pos = mc.player.getPos()
x = pos.x
y = pos.y
z = pos.z

blockType = mc.getBlock(x, y, z)
blockType2 = mc.getBlock(x, y+1, z)
mc.postToChat(blockType == 9)

underwater = blockType == 9
drowning = blockType2 == 9

mc.postToChat("The player is drowning: " + str(drowning))
mc.postToChat("The player is standing in water: " + str(underwater))


