from mcpi.minecraft import Minecraft
mc = Minecraft.create()

def sortPair(val1, val2):
    if val1 > val2:
        return val2, val1
    else:
        return val1, val2

def copyStructure(x1, y1, z1, x2, y2, z2):
    x1, x2 = sortPair(x1, x2)
    y1, y2 = sortPair(y1, y2)
    z1, z2 = sortPair(z1, z2)

    width = x2 - x1
    height = y2 - y1
    length = z2 - z1

    stucture = []

    print("Please wait...")

    for column in range(height):
        structure.append([])
        for row in range(width):
            structure[column].append([])
            for depth in range(length):
                block = mc.getBlock(x1 + row, y1 + column, z1 + depth)
                structure[row][column].append(block)

    return structure

def buildStructure(x, y, z, structure):
    xStart = x
    yStart = y
    for column in structure:
        for row in column:
            for block in row:
                mc.setBlock(x, y, z, block)
                z += 1
            x += 1
            z = yStart
        y += 1
        x = xStart

input("Move to the first corner and press enter in this window")
pos = mc.player.getTilePos()
x1, y1, z1 = pos.x, pos.y, pos.z

input("Move to the opposite corner and press enter in this window")
pos = mc.player.getTilePos()
x2, y2, z2 = pos.x, pos.y, pos.z

structure = copyStructure(x1, y1, z1, x2, y2, z2)

input("Move to the position you want to create the structure and press ENTER in this window")
pos = mc.player.getTilePos()
x, y, z = pos.x, pos.y, pos.z
buildStructure(x, y, z, structure)
