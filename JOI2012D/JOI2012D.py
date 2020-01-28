# %%
# VScodeで入力をテキストから読み込んで標準入力に渡す
import sys
import os
f=open(r'.\JOI2012D\input.txt', 'r', encoding="utf-8")
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
D, N = [int(item) for item in input().split()]

temp_list = [int(input()) for _ in range(D)]
cloth_list = [[int(item) for item in input().split()] for _ in range(N)]

print(temp_list)
print(cloth_list)

dp = [[0, 0] for _ in range(D+1)]

for d in range(D):
    for i in range(N):
        c_sum = dp[d][1]
        ci = cloth_list[i][2]
        if cloth_list[i][0] <= temp_list[d] <= cloth_list[i][1]:
            if c_sum + abs(ci -dp[d][1]) > dp[d+1][1]:
                dp[d+1] = [c_sum + abs(ci -dp[d][1]), cloth_list[i][2]]
            else:
                dp[d+1] = dp[d]
        else:
            dp[d+1] = dp[d]
print(dp)