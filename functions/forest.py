from mcpi.minecraft import Minecraft
mc = Minecraft.create()

x = 0.5
y = 7.0
z = 0.5
count = 1

def growTree():
    tree = 6
    mc.setBlock(x+1, y, z, 6)
    print("tree!")

while count <= 6:
    growTree()
    x += 1
    count = count + 1
