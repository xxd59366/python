try:
    num = int(input('number: '))
    result = 100/num
except (ValueError, ZeroDivisionError):
    print('无效的输入')
except (KeyboardInterrupt, EOFError):
    print('\nBye')
else:
    print(result)

print('Done')
