lines = []

while True :
    line = str(input())
    if line == "" :
        break
    
    t = 0
    temp = line.lstrip()
    lines.append("<li>" + temp + "</li>")

print("-------------------------------------------------------------------------------------------------------------------------------------")
for i in lines :
    print(i)

