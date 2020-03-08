from quick_dict import d
output = ""


def qk(word):
    output = ""
    temp = ""
    for k in word:
        if k in d:
            temp = d[str(k)]
            output += (k+"["+temp+"]"+" ")
        else:
            output += (k+"[] ")
    return output


while 1:
    word = input("請輸入文字")
    print(qk(word))
