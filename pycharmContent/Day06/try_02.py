try:
    num = int(input('number: '))
    result = 100/num
except (KeyboardInterrupt, EOFError):
    print('\nBye')
    exit(65)
except Exception as e:
    print('无效的输入: ', e)
    exit(60)
else:
    print(result)
finally:
    print('Done')

print('正常结束')
