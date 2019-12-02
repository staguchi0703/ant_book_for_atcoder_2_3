# %%
# VScodeで入力をテキストから読み込んで標準入力に渡す
import sys
import os
f=open(r'.\ant_1-6-1_ABC085\ABC085_input.txt', 'r', encoding="utf-8")
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
N, Y = [int(item) for item in input().split()]

y = Y //1000
is_search = True

for i in range(N+1):
    for j in range(N+1):
        k = N -(i+j)
        temp_price = 10*i + 5*j + k

        if temp_price == y and 0 <= k <= N:
            print(i,j,k)
            is_search = False
            break

    if not is_search:
        break

if is_search:
    print('-1 -1 -1')
