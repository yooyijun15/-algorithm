import sys
sys.stdin = open("input.txt", "rt")

N = int(input())
number = list(map(int, input().split()))

score = 0
tmp = 0

for i in number:
    if i == 1:
        tmp += 1
        score += tmp

    else:
        tmp = 0
        
print(score)
