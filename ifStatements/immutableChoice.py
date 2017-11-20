from mcpi.minecraft import Minecraft
mc = Minecraft.create()

Yes = "Y"
attempt = input("Do you want blocks to be immutable? Y/N: ")
if attempt == Yes:
    print("immutable")
    mc.setting("world_immutable", True)
    mc.postToChat("World is immutable")
else:
    print("nothing happened")
    mc.setting("world_immutable", False)
    mc.postToChat("World is mutable")
