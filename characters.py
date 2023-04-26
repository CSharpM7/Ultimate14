import fileinput
import os
import os.path
import glob
import os.path
import shutil


characters = ["mario","donkey","link","samus","samusd","yoshi","kirby","fox","pikachu","luigi","ness","captain","purin","peach","daisy","koopa","ice_climber","sheik","zelda","mariod","pichu","falco","marth","lucina","younglink","ganon","mewtwo","roy","chrom","gamewatch","metaknight","pit","pitb","szerosuit","wario","snake","ike","ptrainer","diddy","lucas","sonic","dedede","pikmin","lucario","robot","toonlink","wolf","murabito","rockman","wiifit","rosetta","littlemac","gekkouga","miifighter","miigunner","miiswordsman","palutena","pacman","reflet","shulk","koopajr","duckhunt","ryu","ken","cloud","kamui","bayonetta","inkling","ridley","simon","richter","alucard","krool","shizue","gaogaen","packun","jack","brave","buddy","dolly","master","tantan","pickel","edge","eflame_first","demon","trail"]
names = ["Mario","Donkey Kong","Link","Samus","Dark Samus","Yoshi","Kirby","Fox","Pikachu","Luigi","Ness","Captain Falcon","Jigglypuff","Peach","Daisy","Bowser","Ice Climbers","Sheik","Zelda","Dr Mario","Pichu","Falco","Marth","Lucina","Young Link","Ganondorf","Mewtwo","Roy","Chrom","Mr Game n Watch","Meta Knight","Pit","Dark Pit","Zerosuit Samus","Wario","Snake","Ike","Pokemon Trainer","Diddy","Lucas","Sonic","King Dedede","Olimar","Lucario","ROB","Toon Link","Wolf","Villager","Megaman","Wii Fit Trainer","Rosalina","Little Mac","Greninja","Mii Brawler","Mii Gunner","Mii Swordfighter","Palutena","Pacman","Robin","Shulk","Bowser Jr","Duck Hunt","Ryu","Ken","Cloud","Corrin","Bayonetta","Inkling","Ridley","Simon","Richter","Alucard","King Krool","Isabelle","Incineroar","Piranha Plant","Joker","Hero","Banjo & Kazooie","Terry","Byleth","Min Min","Steve","Sephiroth","Aegis","Kazuya","Sora"]

#for c in range(len(characters)):
#    print("#"+str(c)+":"+characters[c])
for i in range(len(characters)):
    chara = characters[i]
    name = names[i]
    buffer = "0" if i < 10 else ""
    print("#"+str(i)+":"+chara)
    newfile = os.getcwd() + "\\_portfolio\\" + buffer + str(i) + "_"+chara+".md"
    shutil.copyfile(os.getcwd() +'\\template.md', newfile)
    for line in fileinput.input(newfile, inplace=True):
        print('{}'.format(line.replace("Terry",name).replace("dolly",chara)), end='')