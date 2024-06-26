import sys
sys.stdin = open("input.txt", "rt")

N, M = map(int, input().split())

N_list = []
M_list = []

for n in range(1, N+1):
    N_list.append(n)

for m in range(1, M+1):
    M_list.append(m)

# # 방법 1)
# tmp = 0
# sum_list = []
# for i in N_list:
#     for j in M_list:
#         tmp = i + j
#         sum_list.append(tmp)
#
# tmp_duplicate = 0
# max_duplicate = 0
# max_duplicate_values = set()
#
# # 리스트.count : 리스트 중복 원소 개수
# for v in sum_list:
#     tmp_duplicate = sum_list.count(v)
#     if max_duplicate < tmp_duplicate:
#         max_duplicate = tmp_duplicate
#     elif max_duplicate == tmp_duplicate:
#         max_duplicate_values.add(v)
#
# max_duplicate_values = list(max_duplicate_values)
# print(f"{max_duplicate_values}")

# 방법 2)
# max_value = max(N_list) + max(M_list)
# duplicate_value = [0] * (max_value + 1)
duplicate_value = [0] * (N + M + 2)

for i in N_list:
    for j in M_list:
        duplicate_value[i+j] += 1

# max_duplicate = max(duplicate_value)
max_duplicate = 0
for du in duplicate_value:
    if du > max_duplicate:
        max_duplicate = du

for idx, x in enumerate(duplicate_value):
    if x == max_duplicate:
        # end = ' ' : 한 칸 띄고 출력
        print(idx, end = ' ')