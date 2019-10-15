def set_age(name, age):
    if not 0 < age < 120:
        raise Exception('年龄超出范围(1-120)')
    print('%s is %s years old.' % (name, age))


def set_age2(name, age):
    assert 0 < age < 120, '年龄超出范围(1-120)'
    print('%s is %s years old.' % (name, age))


if __name__ == '__main__':
    set_age('yyl', 26)
    set_age2('sb', 255)
