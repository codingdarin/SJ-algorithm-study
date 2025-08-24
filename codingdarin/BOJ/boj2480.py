# 주사위 세개 (브론즈 4)

# 2회차 풀이
roll = list(map(int, input().split()))

for i in range(1, 7):
    cnt = roll.count(i)
    if cnt == 3:
        ans = 10000 + i * 1000
        break
    elif cnt == 2:
        ans = 1000 + i * 100
        break
    else:
        ans = max(roll) * 100

print(ans)

# # 1회차 풀이 -----------------------------
# roll = list(map(int, input().split()))
# #3 3 6
# dice_count = [0] * 7
#
# for i in range(3):
#     for j in range(7):
#         if roll[i] == j:
#             dice_count[j] += 1
#
# max_dice = 0
# for j in range(7):
#     if dice_count[j] >= max_dice:
#         eye, max_dice = j, dice_count[j]
#
# if max_dice == 1:
#     ans = eye * 100
# elif max_dice == 2:
#     ans = 1000 + eye * 100
# else:
#     ans = 10000 + eye * 1000
#
# print(ans)
