try:
    num = int(input('number: '))
    result = 100/num
except (ValueError, ZeroDivisionError):
    print('无效的输入')
    exit(60)
except (KeyboardInterrupt, EOFError):
    print('\nBye')
    exit(65)
else:
    print(result)
finally:
    print('Done')

print('正常结束')
