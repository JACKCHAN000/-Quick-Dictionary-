import glob
import os
import zipfile
from quick_dict import d
dir = 'C:\\Users\\JACK\\Desktop\\aaaa\\abc\\'
lst_dict = [i for i in glob.glob(dir+"*.txt")]

print(lst_dict)
x = 0


def quick(txt):
    out = ""
    for i in txt:
        if i in d:
            c = d[str(i)]
            out += c
    return out


for i in lst_dict:
    x += 1
    name = str(x)
    print(name)
    data = open(i, 'r', encoding='utf8')
    output = open("dictionary.txt", 'w', encoding='utf8')
    dictzip = zipfile.ZipFile(name+".zip", 'w')
    output.writelines("# Gboard Dictionary version:1"+"\r")
    for i in data.readlines():
        c1 = i.split("\n")
        c2 = quick(c1[0])
        output.writelines(c2+"\t"+c1[0]+"\t"+"zh-HK"+"\r")
    output.close()
    dictzip.write("dictionary.txt")
    dictzip.close()
