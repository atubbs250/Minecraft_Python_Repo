from mcpi.minecraft import Minecraft
mc = Minecraft.create()

block = 35
state = 6
mc.setBlock(10, 3, -4, block, state)
mc.setBlocks(11, 3, -4, 20, 6, -8, block, state)

def getWoolState(color):
    if color == "pink":
        blockState = 6
    elif color == "green":
        blockState = 13
    elif color == "blue":
        blockState = 11
    elif color == "purple":
        blockState = 10
    elif color == "red":
        blockState = 14
    elif color == "white":
        blockState = 35
colorString = input("Enter a block color: ")
state = getWoolState(colorString)

pos = mc.player.getTilePos()
mc.setBlock(pos.x, pos.y, pos.z, 35, state)
