import sys
sys.stdin = open("input.txt", "rt")

N = int(input())
number = list(map(int, input().split()))

max_sum = 0
max_idx = 0

# for i in number:
#     sum_list.append(digit_sum(i))

# # 나의 풀이
# sum_list = []
#
# for i in number:
#     count = len(str(i))
#     sum_num = 0
#     num = i
#     for j in range(count):
#         a = num % 10
#         sum_num += a
#         num = num // 10
#     sum_list.append(sum_num)
#
# for idx, x in enumerate(sum_list):
#     if x > max_sum:
#         max_sum = x
#         max_idx = idx
#
# print(number[max_idx])


# 강의 풀이
# 개념 : while, def - return
def digit_sum(x):
    sum_num = 0
    while x > 0:
        sum_num += x % 10
        x = x // 10
    return sum_num


for i in number:
    tot = digit_sum(i)
    if tot > max_sum:
        max_sum = tot
        result = i

print(result)