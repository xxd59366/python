while True:
    num=int(input('请输入乘法表阶数，取值范围 1-9：'))
    if num in range(1,10):
        for i in range(1,num+1):
            for j in range(1,i+1):
                print('%s*%s=%s' %(j,i,i*j),end='\t')
            print()
        break
    else:
            print('输入错误，请重新输入')