from mcpi.minecraft import Minecraft
mc = Minecraft.create()

x = -6.6
y = 0.0
z = -59.1
TreeStart = mc.getBlock(x+1, y, z)

def growTree():
    tree = 6
    mc.setBlock(x+1, y, z, 6)
    print("tree!")
    x += 1
def growForest():
    x = x + 1
    y = pos.y
    z = pos.z
    for i in range(5):
        tree = 6
        x = x + 1
        mc.setBlock(x, y, z, 6)
        print("tree!")

growTree()
growTree()
growTree()

    


