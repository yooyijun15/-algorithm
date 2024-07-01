import sys
sys.stdin = open("input.txt", "rt")

N = int(input())

# # 나의 풀이
# reward_list = []
#
# for i in range(N):
#     number = list(map(int, input().split()))
#     if number[0] == number[1] == number[2]:
#         money = 10000 + number[0] * 1000
#     elif number[0] == number[1]:
#         money = 1000 + number[0] * 100
#     elif number[0] == number[2]:
#         money = 1000 + number[0] * 100
#     elif number[1] == number[2]:
#         money = 1000 + number[1] * 100
#     else:
#         max_num = max(number)
#         money = max_num * 100
#     reward_list.append(money)
#
# max_reward = max(reward_list)
# print(max_reward)

# 강의 풀이
res = 0
for i in range(N):
    tmp = input().split()
    # 정렬
    tmp.sort()
    a, b, c = map(int, tmp)
    if a == b and b == c:
        money = 10000 + a * 1000
    # 3개 중 2개 같은 식 표현
    elif a == b or b == c:
        money = 1000 + a * 100
    elif b == c:
        money = 1000 + b * 100
    else:
        money = c * 100
    if money > res:
        res = money
print(res)
