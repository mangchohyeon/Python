def noc_plus(a,n,alln) :                          #state는  plus 또는 마이너스, alln은 입력할 원소의 개수
                                                                      #입력한 것들중 n개씩 더해서 a가 되는 경우의 수를 찾아주는 함수

    import itertools

    flag = int(0)
    t = list()

    for i in range(0,alln) :
        a = int(input())
        t.append(a)
        
    data = list(combinations_with_replacement(t, n))
    for i in data :
        s = sum(i)
        if s == a :
            print(i)
            flag = int(1)

    if flag == int(0)  :
        print("None")





        
            
        
