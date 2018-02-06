from mcpi.minecraft import Minecraft
mc = Minecraft.create()

pos = mc.player.getTilePos()
x = pos.x
y = pos.y
z = pos.z
count = 1

def growTree():
    tree = 6
    mc.setBlock(x+1, y, z, 6)
    print("tree!")

while count <= 6:
    growTree()
    x += 1
    count = count + 1
