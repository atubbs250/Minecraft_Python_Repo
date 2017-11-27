from mcpi.minecraft import Minecraft
mc = Minecraft.create()
pos = mc.player.getPos()

x = -105.8
y = 7.0
z = -18.3

air = 0

gift = mc.getBlock(x, y, z)
if gift == 57:
    confirm = input("Do you want to enter: ")
    if confirm == "yes":
        mc.setBlock(-105.3, 5.0, -17.7,  air)
else:
    mc.postToChat("Place an offering on the pedestal.")
    mc.setBlock(pos.x, pos.y - 1, pos.z, 10)
