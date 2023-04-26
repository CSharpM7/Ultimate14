import fileinput
import os
import os.path
import glob
import os.path
import shutil


#characters = ["mario","donkey","link","samus","samusd","yoshi","kirby","fox","pikachu","luigi","ness","captain","purin","peach","daisy","koopa","ice_climber","sheik","zelda","mariod","pichu","falco","marth","lucina","younglink","ganon","mewtwo","roy","chrom","gamewatch","metaknight","pit","pitb","szerosuit","wario","snake","ike","pzenigame","pfushigisou","plizardon","diddy","lucas","sonic","dedede","pikmin","lucario","robot","toonlink","wolf","murabito","rockman","wiifit","rosetta","littlemac","gekkouga","miifighter","miigunner","miiswordsman","palutena","pacman","reflet","shulk","koopajr","duckhunt","ryu","ken","cloud","kamui","bayonetta","inkling","ridley","simon","richter","krool","shizue","gaogaen","packun","jack","brave","buddy","dolly","master","tantan","pickel","edge","eflame_first","demon","trail"]
characters = ["mario"]
#characters = {"pitb","eflame","pfushigisou","purin","younglink","plizardon","shulk","chrom","miifighter","gamewatch","krool","samusd","ryu","rosetta","yoshi","lucas","link","lucario","zelda","kamui","wolf","nana","tantan","koopag","ridley","gekkouga","ike","roy","rockman","peach","elight","gaogaen","falco","ness","kirby","pikachu","daisy","sheik","mariod","luigi","captain","mario","jack","palutena","dolly","pickel","wiifit","pzenigame","pichu","pit","ken","brave","richter","miiswordsman","robin","master","robot","szerosuit","ganon","wario","diddy","shizue","littlemac","pacman","edge","marth","trail","mewtwo","metaknight","toonlink","koopajr","sonic","donkey","inkling","packun","miigunner","buddy","pikmin","cloud","fox","duckhunt","lucina","murabito","bayonetta","samus","koopa","simon","popo","dedede","snake","demon"}

#for c in range(len(characters)):
#    print("#"+str(c)+":"+characters[c])
for c in characters:
    i = characters.index(c)
    buffer = "0" if i < 10 else ""
    print("#"+str(i)+":"+c)
    newfile = os.getcwd() + "\\" + buffer + str(i) + "_"+c+".md"
    shutil.copyfile('74_dolly.md', newfile)
    for line in fileinput.input(newfile, inplace=True):
        print('{}'.format(line.replace("Terry",c).replace("dolly",c)), end='')