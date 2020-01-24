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
import math
N, D= [int(item) for item in input().split()]

dp = [0 for _ in range(int(math.sqrt(D)+1))]
dp[1] = 1

for i in range(N):
    for num in range(1,7):  
        for j in range(int(math.sqrt(D)/num)+1):
            if dp[j] == 1:
                dp[j*num] = 1

print(dp)

