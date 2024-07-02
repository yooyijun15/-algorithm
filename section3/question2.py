import sys
sys.stdin = open("input.txt", "rt")

text = input()

# # 나의 풀이
# num_list = []
# num = 0
# # 숫자 고르기
# for i in text:
#     try:
#         int(i)
#         value = True
#     except ValueError:
#         value = False
#     if value and i:
#         num_list.append(i)
#
# # 숫자 만들기
# cnt = len(num_list)
#
# for j in range(cnt):
#     num += int(num_list[j]) * (10 ** (cnt-(j+1)))
# print(num)
#
# # 약수 개수 구하기
# # 1, num(본인) 포함
# measure_cnt = 2
# for k in range(2, num//2 + 1):
#     if num % k == 0:
#         measure_cnt += 1
#
# print(measure_cnt)

# 강의 풀이
res = 0
for i in text:
    # isdecimal() : 숫자 판별
    if i.isdecimal():
        # 숫자 만들기
        # ex. res = 2, 20+8
        res = res * 10 + int(i)
print(res)

measure_cnt = 0
for k in range(1, res + 1):
    if res % k == 0:
        measure_cnt += 1
print(measure_cnt)
