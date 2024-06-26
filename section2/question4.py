# # 최솟값 구하기
# num = [5, 2, 7, 8, 3, 12]
# count = len(num)
#
# # # 방법 1) question2 오름 차순 활용
# # # 오름 차순 정렬
# # for i in range(0, count):
# #     for j in range(i+1, count):
# #         if num[i] > num[j]:
# #             tmp = num[i]
# #             num[i] = num[j]
# #             num[j] = tmp
# # print(f"최소값: {num[0]}")
#
# # 방법 2) 변수 활용
# # float('inf') : Python 가장 큰 값
# min_value = float('inf')
#
# for i in range(count):
#     if min_value > num[i]:
#         min_value = num[i]
# print(f"최소값: {min_value}")

# 나의 풀이
import sys
sys.stdin = open("input.txt", "rt")

N = int(input())
score = list(map(int, input().split()))

# # 리스트 각 원소 번호 부여
# numbered_score = list(enumerate(score, start=1))
# for number, score in numbered_score:
#     print(f"번호 {number}: 점수 {score}")

score_sum = 0
count = len(score)

for i in range(N):
    score_sum += score[i]

# # round( ,1) : 소수 첫째 자리 반올림, round_half_even 방식
# score_avg = round(score_sum/N, 0)
score_avg = int(score_sum/N + 0.5)

min_value = float('inf')
min_index = 0
min_score = 0

# enumerate : 각 요소 인덱스 값 함께 반환
for idx, x in enumerate(score):
    tmp = abs(x - score_avg)
    if min_value > tmp:
        min_value = tmp
        min_index = idx
        min_score = x
    elif min_value == tmp and min_score < x:
        min_index = idx
        min_score = x

print(f"{score_avg} {min_index + 1}")

# # Chat GPT
# # 평균과 가장 가까운 수 찾기
# closest_score_min = min(score, key=lambda x: abs(x - score_avg))
# closest_score_max = min(score, key=lambda x: (abs(x - score_avg), -x))

# # 인덱스 찾기
# closest_index = score.index(closest_score_max)

# print(f"{score_avg} {closest_index + 1}")
