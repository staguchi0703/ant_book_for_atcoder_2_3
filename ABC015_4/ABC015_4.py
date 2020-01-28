# %%
# VScodeで入力をテキストから読み込んで標準入力に渡す
import sys
import os
f=open(r'.\ABC015_4\input.txt', 'r', encoding="utf-8")
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
W = int(input())
N, K = [int(item) for item in input().split()]
ss_list = [[int(item) for item in input().split()] for _ in range(N)]

dp = [[[0 for _ in range(N+1)] for _ in range(K+1)] for _ in range(W+1)]

for i in range(W+1):
    for j in range(K):
        for k in range(N):
            if i + ss_list[k][0] < W:
                dp[i][j][k] = max(dp[i - ss_list[k-1][0]][j-1][k-1] + ss_list[k-1][1], dp[i][j][k-1])
            else:
                dp[i][j][k] = dp[i][j][k-1]
print(dp)
