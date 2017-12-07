from mcpi.minecraft import Minecraft
mc = Minecraft.create()

def melon():
    return 103
def water():
    return 9
def wool():
    return 35
def lava():
    return 11
def TNT():
    return 46
def Flower():
    return 38
def Diamond():
    return 57

block = melon()
pos = mc.player.getTilePos()
mc.setBlock(pos.x, pos.y, pos.x, block)
