import os
import glob
import run_mw
import re


directory = "C:/Users/jo_ki/OneDrive/Dokumente/My Games/Minecraft/BTE ATCHLI/Renders/auto_exporter"


dirContent = glob.glob(directory + "/schematics/*.schematic")

try:
    os.mkdir(directory + "/model")
except:
    print("Directory already exists")



inputPaths = []
outputPaths = []

for item in dirContent:
    pattern = r"(?<=[\\/])[^\\/]*(?=\.schematic)"
    schematicName = re.findall(pattern, item)[0]


    inputPaths.append(item)


    outputPaths.append(directory + "/model/" + schematicName + ".obj")



run_mw.SaveScript(run_mw.CreateLaunchScript(inputPaths, outputPaths))

run_mw.LaunchMineways("C:/Users/jo_ki/OneDrive/Dokumente/My Games/Minecraft/BTE ATCHLI/Renders/auto_exporter/program/minewaysInstructions.mwscript")