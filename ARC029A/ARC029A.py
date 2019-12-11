# %%
# VScodeで入力をテキストから読み込んで標準入力に渡す
import sys
import os
f=open(r'.\ARC029A\input.txt', 'r', encoding="utf-8")
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
N = int(input())

meat_list = [int(input()) for _ in range(N)]
print(meat_list)


pattern_list = []

for i in range(2**N):
    first_grill = []
    second_grill = []
    for j in range(N):
        if ((i >> j) & 1 == 1):
            first_grill.append(meat_list[j])
        else:
            second_grill.append(meat_list[j])

    if first_grill != []:
        sum_first_grill = sum(first_grill)
    else:
        sum_first_grill = 0

    if second_grill != []:
        sum_second_grill = sum(second_grill)
    else:
        sum_second_grill = 0

    
    pattern_list.append([sum_first_grill, sum_second_grill])

res = min([max(item) for item in pattern_list])

print(res)