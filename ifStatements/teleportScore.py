from mcpi.minecraft import Minecraft
mc = Minecraft.create()

points = int(input("Enter your points: "))
if points <= 2:
    mc.player.setPos(-37.6, 32.0, 58.3)
elif points < 6:
    mc.player.setPos(9.4, 31.0, 16.3)
elif points <= 20:
    mc.player.setPos(8.1, 36.0, -47.5)
elif points < 100:
    mc.player.setPos(-3.3, 14.0, -16.3)
else:
    mc.postToChat("I don't know what to do with that information.")
