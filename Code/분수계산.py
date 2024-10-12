def gcd(a,b): 
    x = a%b
    while x >0:
        a = b
        b = x
        x = a % b
    return b


def calfrac(a,b) :
    
    i = a.index("/")
    A = int(a[0:i])
    B = int(a[i+1:-1] + a[-1])

    i = b.index("/")
    C = int(b[0:i])
    D = int(b[i+1:-1] + b[-1])

    s = A*D + B*C
    m = B*D
    
    x = gcd(s,m)
    
    if x != 1 :
        s = s/x
        m = m /x
    r = str(s) +"/" +str(m)
    return r


x = calfrac("2/7","3/5")
print(x)

    
    
        














    
    
