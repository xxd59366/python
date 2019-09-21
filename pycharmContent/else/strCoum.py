# 快速输出，变量拼接
# str类型相关字段
astr = 'hello world 2018!' 
str2 = astr.capitalize()
str3 = astr.title()
str4 = astr.center(50)
str5=astr.center(50, '-')
str6=astr.count('w')
str7=astr.count('l', 3, 12)
str8=astr.endswith('!')
str9=astr.endswith('o', 3, 12)
str10=astr.startswith('e', 1, 10)
str11=astr.islower()
######################
str12=astr.isdigit()
str13=astr.isalnum()
######################
str14=astr.upper()
str15=astr.strip()
str16=astr.lstrip()
str17=astr.rstrip()
str18=astr.upper()
str19=astr.lower() 
str20="192.168.1.1".split('.')
str21='-'.join(['hello', 'world', '2018'])


for i in range(2,22):
    b=eval('str%s' % i)
    print('%s %s' % (i ,b))
