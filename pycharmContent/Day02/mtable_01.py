for i in range(1,10):
    for j in range(1,i+1):
        endch = '\n' if i == j else '\t'
        print('%s*%s=%s' % (i, j, i*j), end=endch)