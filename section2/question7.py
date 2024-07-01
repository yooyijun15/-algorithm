import sys
sys.stdin = open("input.txt", "rt")

N = int(input())

# # 나의 풀이
# 방법 1) 전체 - 소수 아닌 수
# not_decimal = []
#
# # 소수 아닌 수 찾기
# # range(start, stop, step)
# for i in range(N, 0, -1):
#     for j in range(2, i, 1):
#         if i % j == 0:
#             not_decimal.append(i)
#             break
#
# decimal_count = N - len(not_decimal) - 1
# print(decimal_count)

# 방법 2-1)
decimal = [0] * N

# for i in range(2, N+1):
#     if decimal[i] != 1:
#         for j in range(i+1, N+1):
#             if j % i == 0:
#                 decimal[j] = 1

# 방법 2-2)
# i = 1, 2, ... 19
for i in range(1, N):
    if decimal[i] != 1:
        # i = 1, j = 2, 3, ... 19
        # i = 2, j = 3, 4, ... 19
        for j in range(i+1, N):
            if (j+1) % (i+1) == 0:
                decimal[j] = 1
print(decimal)

decimal_count = 0

for k in decimal:
    if k == 0:
        decimal_count += 1
print(decimal_count -1)

# 강의 풀이 - 에라토스테네스 체
ch = [0] * (N+1)
cnt = 0
# i = 2, 3, ... 20
for i in range(2, N+1):
    if ch[i] == 0:
        cnt += 1
        # i = 2, j = 2, 4, ...20
        # i = 3, j = 3, 6, ...18
        # 즉, 소수의 배수
        for j in range(i, N+1, i):
            ch[j] = 1

print(cnt)