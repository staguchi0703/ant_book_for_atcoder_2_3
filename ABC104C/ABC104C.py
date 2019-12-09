# %%
# VScodeで入力をテキストから読み込んで標準入力に渡す
import sys
import os
f=open(r'.\ABC104C\input.txt', 'r', encoding="utf-8")
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
D, G = [int(item) for item in input().split()]

comp_bounas_list = [[int(item) for item in input().split()] for _ in range(D)]

comp_all = []

for i in range(2**D):
    temp = []
    for j in range(D):
        if ((i >> j) & 1) == 1:
            temp.append(1)
        else:
            temp.append(0)
    comp_all.append(temp)

# print(comp_bounas_list)
# print(comp_all)

full_num_list = [item[0] for item in comp_bounas_list]

each_comp_point = []
for i, item in enumerate(comp_bounas_list):
    each_comp_point.append((i+1)*100*item[0]+item[1])

# print(full_num_list)
# print(each_comp_point)


temp_point_list = []

for each_pattern in comp_all:
    temp_num = 0
    temp_point = 0
    for j, item in enumerate(each_pattern):
            if item:
                temp_num += full_num_list[j]
                temp_point += each_comp_point[j]

    temp_point_list.append([temp_num, temp_point, each_pattern]) 

temp_point_list.sort(key= lambda x:x[1])

# print(temp_point_list)

# justの物を解候補にリスト化する
over_combo = min([item for item in temp_point_list if item[1] >= G], key= lambda x:x[1])
# underのものを解候補にリスト化する
under_combo = [item for item in temp_point_list if item[1] < G]

# print(over_combo)
# print(under_combo)


temp_res_list = []
is_search = True

for temp_combo in under_combo:
    temp_bit_list = temp_combo[2]
    temp_res_point = temp_combo[1]
    temp_res_num = temp_combo[0]
    # print(temp_combo)

    # print(temp_bit_list)
    for j, item in reversed(list(enumerate(temp_bit_list))):
        for _ in range(1, comp_bounas_list[j][0]):
            if item==0:
                temp_res_point += (j+1)*100
                temp_res_num += 1

            if temp_res_point >= G:
                temp_res_list.append([temp_res_num, temp_res_point])
                break

# print(temp_res_list)

res_candi = min(temp_res_list, key=lambda x:x[0])


if over_combo[0] <= res_candi[0]:
    print(over_combo[0])
else:
    print( res_candi[0])
