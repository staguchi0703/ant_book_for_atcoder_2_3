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
def my_recursion(res):
    if len(res) >= len(S):
        return ''

    my_recursion(res + '0')
    my_recursion(res + '+')
    if len(res) == len(S)-1:
        res_list.append(res)

    return res_list
# print(my_recursion(''))
# print(len(my_recursion('')))
res_list = my_recursion('')

temp_S_list = []

for item in res_list:
    temp_S = ''
    for i, j in enumerate(item):
        temp_S += S[i]+j
    temp_S += S[-1]
    S_done_eval = eval(temp_S.replace('0', ''))
    temp_S_list.append(S_done_eval)

print(sum(temp_S_list))