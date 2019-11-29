# %%
# VScodeで入力をテキストから読み込んで標準入力に渡す
import sys
import os
f=open(r'.\JOI2007C\JOI2007C_input.txt', 'r', encoding="utf-8")
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
# index使って二分探索しようとしたけどindexの大小関係と数値の大小関係がことなるからダメだった
# 実際のあたえられた数値で二分探索したらどうなるのか？半分にした値がエリアの値で表現出来ない場合に出来る範囲の度の値に振るかが問題になりそう
N, M = [int(item) for item in input().split()]
point_list = [int(input()) for _ in range(N)]
point_list.append(0)
point_list = sorted(point_list)
print(point_list)
N += 1

high = N**4 -1
low = 0

# print('h', high)
# print('l', low)

def point_cal(point_list, my_index):

    temp_index = []
    for i in reversed(range(4)):
        temp_index.append(my_index // N**i)
        my_index = my_index % (N **i)


    temp_index = temp_index[::-1]

    print(temp_index)
    temp_score = 0
    for index in temp_index:
        temp_score += point_list[index]
    return temp_score

res_list = []

while True:
    mid = (high + low)//2

    # print('----------------roop------')
    # print('h', high)
    # print('m', mid)
    # print('l', low)

    if mid == high or mid == low:
        break

    temp_score = point_cal(point_list, mid)

    print(temp_score, mid)

    if temp_score > M:
        high = mid
    elif temp_score <= M:
        low = mid

    res_list.append(temp_score)

print(max([res for res in res_list if res <= M]))

print('point_cal', point_cal(point_list, 442))
