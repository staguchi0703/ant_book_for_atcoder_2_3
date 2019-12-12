# %%
# VScodeで入力をテキストから読み込んで標準入力に渡す
import sys
import os
f=open(r'.\ABC002D\input.txt', 'r', encoding="utf-8")
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
N, M = [int(item) for item in input().split()]
relation_list = [[int(item) for item in input().split()] for _ in range(M)]

print(N,M)
print(relation_list)

combo_list = []

temp_combo_list = []
for i in range(2**N):
    print(i)
    temp_combo = []

    # 各人について関係がある人をリスト化していく
    # まだできていない
    for j in range(N):
        if ((i >> j) & 1) == 1:
            temp_combo.append(j)
    print(temp_combo)
    temp_combo_list.append(temp_combo)
