from random import randint


def add(*args):
    total = 0
    for val in args:
        total += val
    return total


def roll_dice(n=2):
    """摇色子"""
    total = 0
    for _ in range(n):
        total += randint(1, 6)
    return total


if __name__ == '__main__':
    print(add(1, 2, 3))
    print(add(1, 2, 3, 4))
    print(add())
    print(roll_dice(3))
    print(roll_dice(2))
