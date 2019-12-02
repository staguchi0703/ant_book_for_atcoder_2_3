# %%
# VScodeで入力をテキストから読み込んで標準入力に渡す
import sys
import os
f=open(r'.\ant_1-6-1_ARC004\ARC004_input.txt', 'r', encoding="utf-8")
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
import math
num = int(input())
pos_list = [[int(item) for item in input().split()] for _ in range(num)]

length_list = []
for i in range(num):
    for k in range(num):
        a = pos_list[i]
        b = pos_list[k]

        length = math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)
        length_list.append(length)

print(max(length_list))
