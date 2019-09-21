print('-' * 20 + '请输入考试成绩' + '-' * 20)
grade = int(input())
if grade >= 0 and grade <= 100:
    if grade >= 90:
        print('优秀')
    elif grade >= 80:
        print('好')
    elif grade >= 70:
        print('良好')
    elif grade >= 60:
        print('及格')
    else:
        print('你要努力了！')
else:
    print('错误，输入不合法！请输入0-100！')