from mcpi.minecraft import Minecraft
mc = Minecraft.create()

tree = 6
def growTree(x, y, z):
    x = -2.9
    y = 8.0
    z = -2.9
    mc.setBlocks(x, y, z, 6)
    print("tree!")
    
pos = mc.player.getTilePos()
x = pos.x
y = pos.y
z = pos.z

growTree(x + 1, y, z)
