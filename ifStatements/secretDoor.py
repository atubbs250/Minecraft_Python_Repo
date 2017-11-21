from mcpi.minecraft import Minecraft
mc = Minecraft.create()

x = 68.7
y = 8.0
z = -32.3

gift = mc.getBlock(x, y, z)
if gift == 57:
    confirm = input("Do you want to enter: ")
    if confirm == "yes":
        mc.setBlock(x = 65.3, y = 5.9, z = -29.5, 0)
else:
    mc.postToChat("Place an offering on the pedestal.")
