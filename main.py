import functools as fct


def prt(n) :
    print(n)

prt_1 = fct.partial(prt, 1)
prt_1()