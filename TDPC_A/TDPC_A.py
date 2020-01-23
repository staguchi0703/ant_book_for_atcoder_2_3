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
sum_max = sum(line)

dp = [[0 for k in range(sum_max +1)] for i in range(N+1)]
dp[0] = [1] + [0 for _ in range(sum_max)]
# print(dp)


for i in range(N):
    for j in range(sum_max +1):
        if dp[i][j] == 1 and j - line[i] <= sum_max:
            dp[i+1][j+line[i]] = 1
            print('encount')

print(dp)
