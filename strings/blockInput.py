from mcpi.minecraft import Minecraft
mc = Minecraft.create()
blockType = 1
pos = mc.player.getTilePos()
x = pos.x
y = pos.y
z = pos.z
mc.setBlock(x, y, z, blockType)
blockType = int(input("Enter a block type: "))


