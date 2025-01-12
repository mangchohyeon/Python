res = []
while True :
    temp = str(input())
    if(temp == "end") :
        break

    temp = temp.replace('\\', "\\\\")
    res.append(temp)

for i in res :
    print(i)