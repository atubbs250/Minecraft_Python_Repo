from mcpi.minecraft import Minecraft
mc = Minecraft.create()

air = 0
water = 9

while air == 0:
    pos = mc.player.getTilePos()
    blockBelow = mc.getBlock(pos.x, pos.y - 1, pos.z)
    print("Working")
    if blockBelow != 0 and 9:
        mc.setBlock(pos.x, pos.y - 1, pos.z, 41)
        print("yay")
