from mcpi.minecraft import Minecraft
mc = Minecraft.create()

places = {"Home": ( -37.9, 25.0, -2.5)
          "Tree": (7.3, 31.0, 33.4)
          "Hole": (2.3, -59.0, 13.6)}

choice = ""
while choice != "exit":
    choice = input("Enter a location ('exit' to close): ")
    if choice in places:
        location = places[choice]
        x, y, z = location[0], location[1], location[2]
        mc.player.setTilePos(x, y, z)
        
