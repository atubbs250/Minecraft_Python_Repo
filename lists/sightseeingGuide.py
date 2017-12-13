from mcpi.minecraft import Minecraft
mc = Minecraft.create()

places = {"Home": ( 9.8, 5.0, -26.5),
          "Tree": (74.7, 15.0, -61.7),
          "Hole": (70.3, -61.0, -46.7)}

choice = ""
while choice != "exit":
    choice = input("Enter a location ('exit' to close): ")
    if choice in places:
        location = places[choice]
        x, y, z = location[0], location[1], location[2]
        mc.player.setTilePos(x, y, z)
        
