from mcpi.minecraft import Minecraft
mc = Minecraft.create()

pos = mc.player.getPos()
x = pos.x
y = pos.y 
z = pos.z

blockType = mc.getBlock(x, y-1, z)
mc.postToChat(blockType)

leaves = blockType == 17
wood = blockType == 11

mc.postToChat("The player is in a tree: " + str(leaves or wood))
