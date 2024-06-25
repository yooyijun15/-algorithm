# # 나의 풀이
# import sys
# sys.stdin = open("input.txt", "rt")
#
# N, K = map(int, input().split())
# a = list(map(int, input().split()))
#
# result = []
# 
# for i in range(N):
#     for j in range(i+1, N):
#         for k in range(j+1, N):
#             y = a[i] + a[j] + a[k]
#             result.append(y)
#
# result.sort(reverse=True)
# print(result[K-1])

# 강의 풀이
import sys
sys.stdin = open("input.txt", "rt")

N, K = map(int, input().split())
a = list(map(int, input().split()))
# set() : 중복 제거
res = set()

result = []

for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            res.add(a[i] + a[j] + a[k])

res = list(res)
res.sort(reverse=True)
print(res[K-1])