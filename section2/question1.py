# # 나의 풀이
# n = int(input("number : "))
# k = int(input("count : "))
# divisor = []
#
# for i in range(1, n+1):
#     if n % i == 0:
#         divisor.append(i)
#
# if k > len(divisor):
#     print(-1)
# else:
#     print(f"{k}번째로 작은 약수 : {divisor[k-1]}")

# 강의 풀이
import sys
sys.stdin = open("input.txt", "rt")

n, k = map(int, input().split())
cnt = 0

for i in range(1, n+1):
    if n % i == 0:
        cnt += 1
    if cnt == k:
        print(i)
        break
else:
    print(-1)
