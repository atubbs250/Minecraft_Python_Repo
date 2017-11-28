from mcpi.minecraft import Minecraft
mc = Minecraft.create()
pos = mc.player.getPos()

x = pos.x
y = pos.y
z = pos.z

width = 11
height = 6
length = 7

cobblestone = 1
air = 0

mc.setBlocks(x, y, z, x+length, y+height, z+width, cobblestone)
