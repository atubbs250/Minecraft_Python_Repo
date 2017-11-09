from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time
x = 10.5
y = 7.1
z = 12.3
mc.player.setTilePos(x, y, z)
time.sleep(10)
x = -0.7
y = 0.0
z = -0.7
mc.player.setTilePos(x, y, z)


