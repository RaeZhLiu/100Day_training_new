## NK1
# if __name__ == '__main__':
#     k = 1000
#     num = 0
#
#     while k > 1:
#         print(k)
#         num += 1
#         k = k / 2
#     print(num)

# # NK2   小整数池：[-5, 257)
# a = [-10, -5, 1, 2, 3, 256, 257, 2000]
# b = [-10, -5, 1, 2, 3, 256, 257, 2000]
#
# for i in range(len(a)):
#     print(id(a[i]) == id(b[i]))

# NK3
import math


def sieve(size):
    sieve1 = [True] * size
    sieve1[0] = False
    sieve1[1] = False
    for i in range(2, int(math.sqrt(size)) + 1):
        k = i * 2
        while k < size:
            sieve1[k] = False
            k += i
    return sum(1 for x in sieve1 if x)


print(sieve(10000000000))
