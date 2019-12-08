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



comp_prob_list = []

bit_list = []

for i in range(2**D):
    comp_prob = []
    total_prob_n = 0
    total_point = 0
    bit_flag = ''
    for j in range(D):
        if ((i >> j) & 1 == 1):
            total_prob_n += comp_bounas_list[j][0]
            total_point += comp_bounas_list[j][0]*(j+1)*100 + comp_bounas_list[j][1]
            bit_flag +='1'
        else:
            comp_prob.append([0, 0])
            bit_flag +='0'

    comp_prob_list.append([total_prob_n, total_point])
    bit_list.append(bit_flag)

print(comp_prob_list)
print(bit_list)

# どのbitが立ってるときターゲット以上になるか？
# 一段少ないとこをとったとき、上より少ない数でターゲットをとれるか？



