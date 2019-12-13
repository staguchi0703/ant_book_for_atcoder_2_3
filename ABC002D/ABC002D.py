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

for i in range(2**N):
    bit_ex = print(format(i, 'b').zfill(N))

    temp_combo_list = []
    # 各人について関係がある人をリスト化していく
    # まだできていない
    for k in range(N):
        temp_combo = []
        for j in range(k,N):
            if ((i >> j) & 1) == 1 and ((i >> k) & 1) == 1:
                temp_combo.append([k+1, j+1])
        if temp_combo != []:
            print(temp_combo[1:])
            temp_combo_list += temp_combo[1:]
    combo_list.append(temp_combo_list)
print('ans check -------------------------------')

print(combo_list[7])

if relation_list in temp_combo_list:
    print(relation_list)
else:
    print('no way!')