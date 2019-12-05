# %%
# VScodeで入力をテキストから読み込んで標準入力に渡す
import sys
import os
f=open(r'.\ABC045C\input.txt', 'r', encoding="utf-8")
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
S = input()

res_list = []
def my_recursion(res, i):
    if i == len(S):
        return

    my_recursion(res + S[i] + '-', i+1)
    my_recursion(res + S[i] + '+', i+1)
    # print(res)
    if len(res) == 2*(len(S)-1):
        res_list.append(res.replace('-', '') + S[-1])

    return res_list

# print(my_recursion('', 0))
# print(len(my_recursion('', 0)))

res_list = my_recursion('', 0)
temp_S_list = [eval(item) for item in res_list]

print(sum(temp_S_list))