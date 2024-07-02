import sys
sys.stdin = open("input.txt", "rt")

N = int(input())

# # 나의 풀이
# for i in range(N):
#     verb = input()
#     verb = verb.lower()
#     count = len(verb)
#     tmp_asc = []
#     tmp_desc = []
#     for j in range(0, count, 1):
#         tmp_asc.append(verb[j])
#     for k in range(count-1, -1, -1):
#         tmp_desc.append(verb[k])
#     palindrome_value = tmp_asc == tmp_desc
#     if palindrome_value:
#         print(f"#{i+1} YES")
#     else:
#         print(f"#{i+1} NO")

# # 강의 풀이
# # 방법 1)
# for i in range(N):
#     verb = input()
#     verb = verb.lower()
#     count = len(verb)
#     for j in range(count // 2):
#         # python 인덱스 : (앞) 0, 1, 2, ... / (뒤) -1, -2, -3, ...
#         # -j-1 = -1-j
#         if verb[j] != verb[-j-1]:
#             print(f"#{i + 1} NO")
#             break
#     else:
#         print(f"#{i + 1} YES")

# 방법 2)
for i in range(N):
    verb = input()
    verb = verb.lower()
    count = len(verb)
    # verb[::-1] : 문자열 거꾸로
    if verb == verb[::-1]:
        print(f"#{i + 1} YES")
    else:
        print(f"#{i + 1} NO")


