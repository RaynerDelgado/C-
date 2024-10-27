a, b = map(int, input().split())
mas=[]
for i in range(a):
    mas.append(str(input()))
words=[]
for i in range(a):
    if "#" in mas[i]:
        buff=mas[i].split("#")
        for q in buff:
            if len(q)>1:
                words.append(q)
    else:
        words.append(mas[i])
    buff=""
for i in range(b):
    for j in range(a):
        buff += mas[j][i]
    if "#" in buff:
        buff = buff.split("#")
        for q in buff:
            if len(q)>1:
                words.append(q)
    else:
        words.append(buff)
    buff=""
words.sort()
print(words[0])
