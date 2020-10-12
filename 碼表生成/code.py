import re
from quick_dict import d
input = open("input.txt", 'r', encoding='utf-8')
output = open("output.txt", 'w', encoding='utf-8')


def special_match(strg, search=re.compile(r'[^a-z0-9.]').search):
    return not bool(search(strg))


def quick(txt):
    out = ""
    for i in txt:
        if i in d:
            c = d[str(i)]
            out += c
    return out


for line in input.readlines():
    line = line.split("\t")
    words = line[0]
    if special_match(words) == False:
        print(words+quick(words))
        output.write(words+"\t"+quick(words)+"\n")
output.close()
