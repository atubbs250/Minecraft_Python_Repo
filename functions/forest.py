from mcpi.minecraft import Minecraft
mc = Minecraft.create()

def growTree(x, y, z):


pos = mc.player.getTilePos()
x = pos.x
y = pos.y
z = pos.z

growTree(x + 1, y, z)
