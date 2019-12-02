# %%
# VScodeで入力をテキストから読み込んで標準入力に渡す
import sys
import os
f=open(r'.\ant_1-1-1_JOI2007C\JOI2007C_input.txt', 'r', encoding="utf-8")
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
# 全パターンを計算すると10^12でTLE
# 半分計算して組み合わせをだしておいて、残りの半分のなかで条件を満たす最大値を探す。
# この操作を最初の半分の組み合わせ分行うこれでO(root(N^4) * 残りの操作のオーダ)
# 残りの半分からなるべく早く見つけないとTLEとなってしまう。（線形探索してしまったら全部を線形探索しているのと変わらなくなる）
# 残りの半分は(リスト事態は前半の半分と同じだけど)順序のあるリストに出来るので二分探索する（オーダ 2logN）
import bisect
N, M = [int(item) for item in input().split()]
point_list = [int(input()) for _ in range(N)]
point_list.append(0)

half_comb_list = [point_list[i]+point_list[k] for i in range(len(point_list)) for k in range(i+1) if point_list[i]+point_list[k] <= M]
half_comb_list.sort()

res_list = []
for first_val in half_comb_list:
    second_gr_index = bisect.bisect_left(half_comb_list, M - first_val)
    res = first_val + half_comb_list[second_gr_index-1]
    res_list.append(res)

print(max(res_list))

