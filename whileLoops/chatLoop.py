from mcpi.minecraft import Minecraft
mc = Minecraft.create()

userName = input("Enter your username:")
while userName == "Amanda":
    message = input("Enter your message:")
    mc.postToChat(userName + ": " + message)
    if message == "exit":
        break
    print("working")



