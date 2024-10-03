import csv

e2k = { }
k2e = { }
with open('우선순위 영단어.csv', 'r') as f :
    data = csv.reader(f)

    for word in data :
        e2k[word[0]] = word[1]


eng = list(e2k.keys())
kor = list(e2k.values())

f = open("우선순위 영단어.txt", "a",encoding = "utf-8")
for i in range(0,1000) :
    a = "%s//%s\n" % (eng[i], kor[i])
    f.write(a)


f.close()
    
