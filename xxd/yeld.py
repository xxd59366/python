def mygen():
    yield 'hello'
    a = 10 + 20
    yield a
    yield [1,2,3]

for i in mygen():
    print(i,end='\t')
