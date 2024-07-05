import sys
sys.stdin = open("input.txt", "rt")

a = int(input())
a_list = list(map(int, input().split()))

b = int(input())
b_list = list(map(int, input().split()))


# # 방법 1)
# # + : 리스트 합치기
# new_list = a_list + b_list
# # list(set()) : 리스트 중복 없애기 및 정렬
# set_list = list(set(new_list))
# # sort() : 리스트 정렬
# set_list.sort()
#
# print(set_list)


# # 방법 2)
# # 두 리스트 합치기 - 중복 제거
# new_list = []
# for i in a_list:
#     new_list.append(i)
# for j in b_list:
#     if j not in a_list:
#         new_list.append(j)
# print(new_list)
#
# # 오름 차순
# cnt = len(new_list)
# for k in range(cnt):
#     for g in range(k+1, cnt):
#         tmp = 0
#         if new_list[k] > new_list[g]:
#             tmp = new_list[k]
#             new_list[k] = new_list[g]
#             new_list[g] = tmp
#
# print(new_list)


# 방법 3)
# id() : 메모리 주소
p1 = p2 = 0
new_list = []

while p1 < a and p2 < b:
    if a_list[p1] <= b_list[p2]:
        new_list.append(a_list[p1])
        p1 += 1
    else:
        new_list.append(b_list[p2])
        p2 += 1
if p1 < a:
    new_list = new_list + a_list[p1:]
if p2 < b:
    new_list = new_list + b_list[p2:]

print(new_list)