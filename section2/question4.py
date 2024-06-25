# 나의 풀이
import sys
sys.stdin = open("input.txt", "rt")

N = int(input())
score = list(map(int, input().split()))
# 리스트 각 원소 번호 부여
numbered_score = list(enumerate(score, start=1))
score_sum = 0

# for number, score in numbered_score:
#     print(f"번호 {number}: 점수 {score}")

for i in range(N):
    score_sum += score[i]

# round( ,1) : 소수 첫째 자리 반올림
score_avg = int(round(score_sum / N, 0))

# 평균과 가장 가까운 수 찾기
closest_score_min = min(score, key=lambda x: abs(x - score_avg))
closest_score_max = min(score, key=lambda x: (abs(x - score_avg), -x))

# 인덱스 찾기
closest_index = score.index(closest_score_max)

print(f"{score_avg} {closest_index + 1}")
