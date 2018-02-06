from mcpi.minecraft import Minecraft
mc = Minecraft.create()

import time

pos = mc.player.getTilePos()
x = pos.x
y = pos.y
z = pos.z

class Building(object):
    def __init__(self, x, y, z, width, height, depth):
        self.x = x
        self.y = y
        self.z = z

        self.width = width
        self.height = height
        self.depth = depth

    def build(self):
        mc.setBlocks(self.x, self.y, self.z,
                    self.x + self.width, self.y + self.height,
                    self.z + self.depth, 4)

        mc.setBlocks(self.x + 1, self.y + 1, self.z + 1,
                     self.x + self.width - 1, self.y + self.height - 1,
                     self.z + self.depth - 1, 0)

        self.buildWindows()
        self.buildDoor()

    def clear(self):
        mc.setBlocks(self.x, self.y, self.z,
                     self.x + self.width, self.y + self.height,
                     self.z + self.depth, 0)
        
    def buildWindows(self):
        mc.setBlocks(self.x + (self.width / 4 * 3), self.y + 2, self.z, 0)
        mc.setBlocks(self.x + (self.width / 4), self.y + 2, self.z, 0)

    def buildDoor(self):
        mc.setBlocks(self.x + (self.width / 2), self.y + 1, self.z,
                     self.x + (self.width / 2), self.y + 2, self.z, 0)

class Tree(object):
    def __init__(self, name):
        self.name = name
        
    def growTree(x, y, z):
        wood = 17
        leaves = 18

        mc.setBlocks(x, y, z, x, y + 5, z, wood)
        
        mc.setBlocks(x - 2, y + 6, z - 2, x + 2, y + 6, z + 2, leaves)
        mc.setBlocks(x - 1, y + 7, z - 1, x + 1, y + 7, z + 1, leaves)

    def clear(self):
        wood = 0
        leaves = 0

        mc.setBlocks(x, y, z, x, y + 5, z, wood)
        
        mc.setBlocks(x - 2, y + 6, z - 2, x + 2, y + 6, z + 2, leaves)
        mc.setBlocks(x - 1, y + 7, z - 1, x + 1, y + 7, z + 1, leaves)

pos = mc.player.getTilePos()
x = pos.x
y = pos.y
z = pos.z

ghostTree = Tree("ghostTree")
ghostTree.growTree(x, y, z)

time.sleep(10)

ghostTree.clear()
