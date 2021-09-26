import os

minewaysPath = "E:/Program Files/mineways/Mineways.exe"
terrainFile = "C:/Users/jo_ki/OneDrive/Dokumente/My Games/Minecraft/BTE ATCHLI/Renders/Custom Texture Sheet/TileMaker/AVPBR-1-3-TerrainMap.png"


def LaunchMineways(script):
    launchCommand = '"' + minewaysPath + '" -t "' + terrainFile + '" "' + script + '"'

    print(launchCommand)

    stream = os.popen(launchCommand)
    output = stream.read()

    print(output)


def CreateLaunchScript(inputPaths, outputPaths):
    script = ""
    script = """Set render type: Wavefront OBJ absolute indices

File type: Export full color texture patterns
Texture output RGB: no
Texture output A: no
Texture output RGBA: no

Material per family: Yes
//G3D full material: YES

Give more export memory: YES\n\n"""

    if len(inputPaths) == len(outputPaths):

        for i in range(len(inputPaths)):
            script += "Minecraft world: " + inputPaths[i] + "\n"
            script += "Selection location: all\n"
            script += "Export for rendering: " + outputPaths[i] + "\n\n"

        script += "Close"

    return script


def SaveScript(scriptContent):
    f = open("minewaysInstructions.mwscript", "w")
    f.write(scriptContent)
    f.close()
