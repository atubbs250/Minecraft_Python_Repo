from mcpi.minecraft import Minecraft
mc = Minecraft.create()

boom = "Y"
noBoom = "N"
attempt = raw_input("Create a crater? Y/N: ")
if attempt == boom:
    print("Boom!")
    pos = mc.player.getPos()
    mc.setBlocks(pos.x + 1, pos.y + 1, pos.z + 1, pos.x - 1, pos.y - 1, pos.z -1, 0)
    mc.postToChat("Boom!")
if attempt == noBoom:
    print("Why not?")
    

    
    
