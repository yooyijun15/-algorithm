import sys
sys.stdin = open("input.txt", "rt")

N, M = map(int, input().split())
N_list = list(map(int, input().split()))

# 1, 2
# 2, 1
# 3
# 1, 1, 1
# 1, 2

# # 나의 풀이
# result = 0
# cnt = 0
#
# for i in range(N):
#     result += N_list[i]
#     if result == M:
#         cnt += 1
#         result = 0
#     elif result < M:
#         for j in range(i+1, N):
#             result += N_list[j]
#             if result == M:
#                 cnt += 1
#                 result = 0
#                 break
#             elif result > M:
#                 result = 0
#                 break
#     elif result > M:
#         result = 0

# 강의 풀이
# 1 2 1 3 1 1 1 2
lt = 0
rt = 1
tot = N_list[lt]
cnt = 0
# tot = 1, 3, 2, 3, 1, 2, 3, 2, 3, 0, 1, 3
# lt = 0, 1, 2, 3, 4
# rt = 1, 2, 3, 4, 5, 6, 7, 8
# cnt = 0, 1, 2, 3, 4, 5
while True:
    if tot < M:
        if rt < N:
            tot += N_list[rt]
            rt += 1
        else:
            break
    elif tot == M:
        cnt += 1
        tot -= N_list[lt]
        lt += 1
    else:
        tot -= N_list[lt]
        lt += 1

print(cnt)


