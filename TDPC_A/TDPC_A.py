# %%
# VScodeで入力をテキストから読み込んで標準入力に渡す
import sys
import os
f=open(r'.\TDPC_A\input.txt', 'r', encoding="utf-8")
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
line = [int(item) for item in input().split()]

dp = [[0 for i in range(N+1)] for _ in range(N*100 +1)]

for i in range(N):
    for j in range(N*100 +1):
        if j < line[i]:
            dp[j][i+1] = 0
        else:
            dp[j][i+1] = max(dp[j][i], dp[j - line[i]][i] + 1)

print(dp)
