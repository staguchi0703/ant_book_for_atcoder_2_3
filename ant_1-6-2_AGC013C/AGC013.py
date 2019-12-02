# %%
# VScodeで入力をテキストから読み込んで標準入力に渡す
import sys
import os
f=open(r'.\ant_1-6-2_AGC013C\AGC013_input.txt', 'r', encoding="utf-8")
# inputをフルパスで指定
# win10でファイルを作るとs-jisで保存されるため、読み込みをutf-8へエンコードする必要あり
# VScodeでinput file開くとutf8になってるんだけど中身は結局s-jisになっているらしい
sys.stdin=f

#
# 入力スニペット
# num = int(input())
# num_list = [int(item) for item in input().split()]
# num_list = [input() for _ in range(3)]
##################################
# %%
# 以下ペースト可
N, L, T = [int(item) for item in input().split()]
pos_list = [[int(item) for item in input().split()] for _ in range(N)]
print(pos_list)

# for pos, direction in pos_list:
#     if direction == 1:
#         pos = (pos + T) % L
#         res_list.append(pos)

#     else:
#         pos = (pos -T) % L
#         if pos < 0:
#             pos += 8

#         res_list.append(pos)
num = 0


next_list = []

for i, item in enumerate(pos_list):
    next_list.append([*item , i])

while T >= 0:
    pos_list, next_list = next_list, []
    print(pos_list)
    for pos, direction, num in pos_list:
        if direction == 1:
            pos = (pos + 1) % L
            next_list.append([pos, direction, num])

        else:
            pos = (pos -1) % L
            if pos < 0:
                pos += 8
            next_list.append([pos, direction, num])
        
        num += 1

    for i in range(N):
        
        is_contact = False

        if next_list[i][1] == 1:
            if next_list[i][0] == (next_list[(i+1)%N][0] + 1) % L:
                next_list[i][1], next_list[(i+1)%N][1] = next_list[(i+1)%N][1], next_list[i][1]
                # next_list[i][2], next_list[(i+1)%N][2] = next_list[(i+1)%N][2], next_list[i][2]
        else:
            if next_list[i][0] == (next_list[(i-1)%N][0] - 1) % L:
                next_list[i][1], next_list[(i-1)%N][1] = next_list[(i-1)%N][1], next_list[i][1]
                # next_list[i][2], next_list[(i-1)%N][2] = next_list[(i-1)%N][2], next_list[i][2]

    T -= 1

print(next_list)
