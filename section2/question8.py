import sys
sys.stdin = open("input.txt", "rt")

N = int(input())
number = list(map(int, input().split()))

# 나의 풀이
# def reverse(origin):
#     desc_list = []
#     for num in origin:
#         str_num = str(num)
#         count = len(str_num)
#         desc_num = 0
#         for i in range(count-1, -1, -1):
#             int_num = int(str_num[i])
#             if int_num != 0:
#                 desc_num += int_num * (10 ** i)
#         desc_list.append(desc_num)
#     return desc_list

# def isPrime(origin):
#     decimal_list = origin[:]
#     for num in origin:
#         decimal_value = True
#         i = 2
#         while decimal_value and i < num:
#             if num % i == 0:
#                 decimal_list.remove(num)
#                 decimal_value = False
#             else:
#                 i += 1
#     return decimal_list

# reverse_list = reverse(number)
# result_list = isPrime(reverse_list)
#
# print(result_list)

# # 숫자 뒤집기 - 첫자리 0 제거
# desc_list = []
#
# for num in number:
#     str_num = str(num)
#     count = len(str_num)
#     desc_num = 0
#     for i in range(count-1, -1, -1):
#         int_num = int(str_num[i])
#         if int_num != 0:
#             desc_num += int_num * (10 ** i)
#     desc_list.append(desc_num)
# print(desc_list)

# # 소수 판별
# # [:] : 리스트 복사본 생성
# decimal_list = desc_list[:]
#
# for num in desc_list:
#     decimal_value = True
#     i = 2
#     while decimal_value and i < num:
#         if num % i == 0:
#             decimal_list.remove(num)
#             decimal_value = False
#         else:
#             i += 1
#
# print(decimal_list)


# 강의 풀이
# ex 1. 23
# ex 2. 7300
def reverse(x):
    res = 0
    while x > 0:
        # ex 1. t = 3, 2
        # ex 2. t = 0, 0, 3, 7
        t = x % 10
        # ex 1. res = 3, 32
        # ex 2. res = 0, 0, 3, 37
        res = res * 10 + t
        # ex 1. x = 2, 0
        # ex 2. x = 730, 73, 7, 0
        x = x // 10
    # ex 1. res = 32
    # ex 2. res = 37
    return res

# ex 1. 32
# ex 2. 37
def isPrime(x):
    if x == 1:
        return False
    # ex 1. i = 2
    # ex 2. i = 2, 3, 4, 5, 6, ... 18
    for i in range(2, x//2+1):
        if x%i == 0:
            # ex 1. False
            return False
    else:
        # ex 2. True
        return True


for x in number:
    tmp = reverse(x)
    if isPrime(tmp):
        print(tmp, end=' ')
