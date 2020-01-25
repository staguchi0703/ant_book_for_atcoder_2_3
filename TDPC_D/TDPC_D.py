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

factor = [0, 0, 0]

while D % 2 == 0:
    D //= 2
    factor[0] += 1

while D % 3 == 0:
    D //= 3
    factor[1] += 1

while D % 5 == 0:
    D //= 5
    factor[2] += 1

if D != 1:
    print(0)
else:
    dp = [[[[0.] * (factor[2]+1)
            for j in range(factor[1]+1)]
            for k in range(factor[0]+1)] 
            for l in range(N+1)]
    # 確率を値に持ったdp

    dp[0][0][0][0] = 1 # 0回振って2,3,5の倍数になる確率は1（0だから）として初期化

    for i in range(N):
        for j in range(factor[0]+1):
            for k in range(factor[1]+1):
                for l in range(factor[2]+1):
                    # i+1回目の確率
                    # Dの倍数だから各素因数の数はDの因数の個数を超えてもよい。
                    dp[i+1][j][k][l] += dp[i][j][k][l] * 1/6 #目が1
                    dp[i+1][min(factor[0], j+1)][k][l] += dp[i][j][k][l] * 1/6#目が2
                    dp[i+1][j][min(k+1,factor[1])][l] += dp[i][j][k][l] * 1/6#目が3
                    dp[i+1][min(j+2,factor[0])][k][l] += dp[i][j][k][l] *  1/6#目が4
                    dp[i+1][j][k][min(l+1,factor[2])] += dp[i][j][k][l] * 1/6#目が5
                    dp[i+1][min(j+1,factor[0])][min(k+1,factor[1])][l] += dp[i][j][k][l] * 1/6#目が6
    print(dp[N][factor[0]][factor[1]][factor[2]])