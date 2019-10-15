import random


def kp(seq):
    if len(seq) < 2:
        return seq
    middle = seq[0]
    smaller = []
    larger = []

    for num in seq[1:]:
        if num <= middle:
            smaller.append(num)
        else:
            larger.append(num)

    return kp(smaller) + [middle] + kp(larger)


if __name__ == '__main__':
    nums = [random.randint(1, 100) for i in range(10)]
    print(nums)
    result = kp(nums)
    print(result)
