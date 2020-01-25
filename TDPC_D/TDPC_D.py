# %%
# VScodeで入力をテキストから読み込んで標準入力に渡す
import sys
import os
f=open(r'.\TDPC_D\input.txt', 'r', encoding="utf-8")
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
# res1 = Dの倍数の個数
# 回答は　Dの倍数の確率なので計算して出力する
import math
N, D= [int(item) for item in input().split()]
max_num = int(math.sqrt(6**N))

dp = [[1 if m == D else 0 for m in range(max_num+1)] for _ in range(N+1)]
cnt = 0

for i in range(N):
    for j in range(max_num+1):
        for k in range(1,7):
            dp[i+1][j] = dp[i][j]
            if dp[i][j] == 1 and j*k < max_num:
                index_1  = j*k
                print(i,j,i*j, max_num)
                dp[i+1][index_1] = 1
                cnt += 1

print(cnt)
