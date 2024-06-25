# # 나의 풀이
# num = [5, 2, 7, 8, 3, 12]
# count = len(num)
# k = int(input(f"몇 번째 수?(최대 {count}) "))
#
# # 오름 차순 정렬
# for i in range(0, count):
#     for j in range(i+1, count):
#         if num[i] > num[j]:
#             tmp = num[i]
#             num[i] = num[j]
#             num[j] = tmp
#
# print(f"{k}번째 수 = {num[k-1]}")

# 강의 풀이
import sys
sys.stdin = open("input.txt", "rt")

T = int(input())
for t in range(T):
    n, s, e, k = map(int, input().split())
    a = list(map(int, input().split()))
    a = a[s-1:e]
    # 오름 차순
    a.sort()
    print(f"#{t+1} {a[k-1]}")

