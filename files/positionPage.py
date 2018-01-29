from flask import Flask
app = Flask(__name__)
from mcpi.minecraft import Minecraft
mc = Minecraft.create()
pos = mc.player.getTilePos()
x = pos.x
y = pos.y
z = pos.z

@app.route("/")
def position():
    return ("x: " + str(pos.x) + " y: " + str(pos.y) + " z: " + str(pos.z))

app.run()
