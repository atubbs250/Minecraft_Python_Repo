from mcpi.minecraft import Minecraft
mc = Minecraft.create()

tree = 6

def growTree():
    tree = 6
    pos = mc.player.getPos()
    x = pos.x
    y = pos.y
    z = pos.z
    mc.setBlock(x+1, y, z, 6)
    print("tree!")
    
growTree()
growTree()
    


