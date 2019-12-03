# %%
# VScodeで入力をテキストから読み込んで標準入力に渡す
import sys
import os
f=open(r'.\ant_1-6-2_AGC013C\AGC013_input.txt', 'r', encoding="utf-8")
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
N, L, T = [int(item) for item in input().split()]
pos_list = [[int(item) for item in input().split()] for _ in range(N)]

first_ant = pos_list[0]
# N 匹の蟻がいて、それぞれの蟻は 1 から N まで番号の書かれたゼッケンをつけている。
# 二つの蟻が同じ場所についた瞬間、その二つの蟻はゼッケンを交換し、そのまますれ違って同じ方向に歩き続ける。
# 上記問題の言い換えに生息するfirst ant さんの操作後の位置とゼッケンを求める
if first_ant[1] == 1: #一番の子が1向きの場合

    last_pos_of_first_ant = (first_ant[0] + T ) % L
    num_of_reverse_ant = [item[1] for item in pos_list].count(2)

    cnt = 0
    reverse_ant_pos = [item[0] for item in pos_list if item[1] == 2]
    cnt += T//L * len(reverse_ant_pos)

    for i in reverse_ant_pos:
        if (i - first_ant[0])//2 +1 <= (T % L):
            cnt += 1
    
    last_num_of_first_ant = (1 + cnt) % N
    if last_num_of_first_ant == 0:
        last_num_of_first_ant += N

else:
    last_pos_of_first_ant = (first_ant[0] - T ) % L
    num_of_reverse_ant = [item[1] for item in pos_list].count(1)

    cnt = 0
    reverse_ant_pos = [item[0] for item in pos_list if item[1] == 1]

    cnt += T//L * len(reverse_ant_pos)

    for i in reverse_ant_pos:
        if ((first_ant[0] -(i-L))//2 + 1) <= (T % L):
            cnt += 1
            # print(T % L)
            # print(i, first_ant[0] -(i-L),(first_ant[0] -(i-L))//2 + 1) 
            # print('cnt', cnt)
    
    last_num_of_first_ant = (1 - cnt) % N
    if last_num_of_first_ant <= 0:
        last_num_of_first_ant += N

# アリの位置を求める
last_ant_pos = []

for ant_pos, direction  in pos_list:
    if direction == 1:
        last_ant_pos.append((ant_pos + T)%L)
    else:
        ant_pos = (ant_pos - T)%L
        if ant_pos < 0:
            ant_pos += L
        last_ant_pos.append(ant_pos)

# first ant さんは位置Xにいるので、アリの位置リストからどれがfirst antさんか特定する。
# 特定したらその位置にゼッケンを設定する。
# 1方向のfirst antさんは、その他のゼッケンは時計回りに+1する（他のアリを1減らしながら回っているから）
# 2方向のfirst antさんは、その他のゼッケンを時計回りに-1する（他のアリを1増やしながら回っているから。逆回りに・・・で考えたほうが分かりよいか？）
# 2方向の場合はできたリストを逆順に出力する    
res = []
if first_ant[1] == 1:
    for i, pos in enumerate(last_ant_pos):
            temp_num = (last_num_of_first_ant+i)%N
            if temp_num == 0:
                temp_num = N
            res.append([pos, temp_num])

    res.sort(key=lambda x:x[1])
else:
    for i, pos in enumerate(last_ant_pos):
        temp_num = (last_num_of_first_ant-i)%N
        if temp_num == 0:
            temp_num = N
        res.append([pos, temp_num])

    res.sort(key=lambda x:x[1], reverse=True)



# print(first_ant)
# print(num_of_reverse_ant)
# print(reverse_ant_pos)
# print('collison', cnt)
# print('first ant of pos, num',last_pos_of_first_ant, last_num_of_first_ant)
# print(last_ant_pos)
# print(res)
# print('-------ans--------')
print(*[item[0] for item in res])
