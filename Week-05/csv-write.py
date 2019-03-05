## player name, score
# Mary Please, 72
# Max Walker, 64
# Col Klomp, 78
# Belle McKay, 67

import csv
import io
import random

def r():
    return random.randint(64, 78)

players = [
    ["Amhuinn", "Alumfist", r()],
    ["Balfour", "Micabeard", r()],
    ["Belimawr", "Crystalbeard", r()],
    ["Braith", "Flamedigger", r()],
    ["Breck", "Diamondchief", r()],
    ["Bridget", "Pyritechief", r()],
    ["Bryanna", "Darkdagger", r()],
    ["Camlin", "Leadking", r()],
    ["Catriona", "Tinqueen", r()],
    ["Conal", "Spargrinder", r()],
    ["Concepta", "Redclan", r()],
    ["Conley", "Sulfurbeard", r()],
    ["Corie", "Flamespade", r()],
    ["Corri", "Slategauntlet", r()],
    ["Creiddylad", "Crystalfist", r()],
    ["Cumina", "Moltenchief", r()],
    ["Drem", "Birchminer", r()],
    ["Dwyer", "Firechief", r()],
    ["Dylis", "Harddagger", r()],
    ["Farrell", "Muddagger", r()],
    ["Finbar", "Flamedagger", r()],
    ["Gladis", "Boronaxe", r()],
    ["Glinda", "Micaclan", r()],
    ["Gwenyth", "Rubygold", r()],
    ["Gwitart", "Jewelshield", r()],
    ["Hisolda", "Jetcrusher", r()],
    ["Kam", "Leadminer", r()],
    ["Kelcie", "Silverspade", r()],
    ["Llawr", "Sulfurgold", r()],
    ["Meaghan", "Sandygold", r()],
    ["Moran", "Moltendwarf", r()],
    ["Murchadh", "Moondwarf", r()],
    ["Myma", "Sandydwarf", r()],
    ["Ronald", "Earthcrusher", r()],
    ["Ruadhagan", "Coaldwarf", r()],
    ["Shela", "Flamegauntlet", r()],
    ["Terriss", "Cindershield", r()],
    ["Tierney", "Shalecollier", r()],
    ["Tighe", "Sulfurforge", r()],
    ["Tormaigh", "Lavaforge", r()],
]




with open('Golf-000.txt', mode='w', newline='') as player_file:
    player_writer = csv.writer(player_file, delimiter=",", quotechar='"', quoting=csv.QUOTE_NONNUMERIC)
    player_writer.writerows(players)
