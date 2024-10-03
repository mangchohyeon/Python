def millionprimelist(a) :
    import copy

    global prime
    number = list(range(480000,a+1))
    f = open("hundthousprime.txt",'r')
    a = (f.read()).split()
    prime = list()
    for i in a :
        prime.append(int(i))
    pcount = int(1)


    for i in number :
        if (i % 2) == 0 :
            continue
        else :
            p0 = copy.deepcopy(prime)
            for k in p0 :
                if (i % k) == 0 :
                    pcount= int(0)
                    break
            if pcount == 0 :
                pcount = int(1)
                continue
            else :
                pcount = int(1)
                prime.append(i)
    f.close()
    return prime

prime = millionprimelist(500000)
f = open("hundthousprime.txt",'a')
for i in prime :
    if i >= 480000 :
        f.write("%d\n"%i)
    
f.close()


