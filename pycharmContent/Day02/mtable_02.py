num = int(input('XX乘法表?\n'))
for i in range(1,num+1):
    for j in range(1,i+1):
        endch = '\n' if i == j else '\t'
        print('%s*%s=%s' % (j, i, i*j), end=endch)