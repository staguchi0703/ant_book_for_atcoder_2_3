# %%
# VScodeで入力をテキストから読み込んで標準入力に渡す
import sys
import os
f=open(r'.\AOJ0-1KnapsackProblem\input.txt', 'r', encoding="utf-8")
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
N, W = [int(item) for item in input().split()]
item_list = [[int(item) for item in input().split()] for _ in range(N)]
print(item_list)

dp = [[0]* (N+1)] * (W+1)


for i in range(0, N):
    for j in range(0, W+1):

        temp_w = item_list[i][1]

        if j <= temp_w:
            print('A',i, j, dp[j][i])
            dp[j][i+1] = dp[j][i]

        else:

            dp[j][i+1] = max(dp[j - temp_w][i] + item_list[i][0], dp[j][i])
            print('B',i+1, j, dp[j][i+1])  
            print(dp)

        print('x', i,j, dp[j][i])
        # print(item_list[i][0], item_list[i][1])


        """
                        重さを引いて足して結局ｊになったときの価値（i番目のものが重いとベースの価値が低くなるかも）と
                        一つ少ない個数（重くて価値のあるもので重さがｊになっているかもしれない）と比較して、価値が大きい方を選ぶ
        """
print(dp)
#########

dp = [[0]* (N+1)] * (W+1)
dp[0][3] = 8

dp[0]

print(dp, dp[0])