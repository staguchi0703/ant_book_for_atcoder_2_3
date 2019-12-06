# %%
# VScodeで入力をテキストから読み込んで標準入力に渡す
import sys
import os
f=open(r'.\ABC079C\input.txt', 'r', encoding="utf-8")
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
ABCD = input()

N = len(ABCD)


for i in range(2**(N-1)):
    temp_res = ''
    for j in range(N-1):
        temp_res += ABCD[j]
        if ((i >> j) & 1):
            temp_res += '+'
        else:
            temp_res += '-'
    temp_res += ABCD[-1]

    if eval(temp_res) == 7:
        res = temp_res + '=7'
        break

print(res)
