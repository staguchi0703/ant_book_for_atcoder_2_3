# [やってみた]　AtCoder 版！蟻本 (初級編) [随時更新]

## はじめに

筆者はAtCoderを取り組み始めたアラフォー・ザコーダである。

[D問題をコンテスト中にACしたことがないので、特訓が必要である](https://qiita.com/tagtagtag/items/f9ae5a1a0c24d04ae923)

[AtCoder 版！蟻本 (初級編)](https://qiita.com/drken/items/e77685614f3c6bf86f44)に蟻本記載例題の類似問題が記載されている。

[AtCoder](https://atcoder.jp/?lang=ja)を利用してジャッジできるアルゴリズムの良問が選別されているので、初学者にうってつけである。

けんちょん (Otsuki)@drken氏に感謝。


## 目的

* 筆者の競技プログラミング成績向上を図る。
* [AtCoder 版！蟻本 (初級編)](https://qiita.com/drken/items/e77685614f3c6bf86f44)に記載の問題を解説しながら記述することで、アルゴリズムの基礎を身に着ける。
* コードと解説を掲載し、諸兄（姉）からの指摘を受けることで見落としていた課題を補完する。

## 今後

* 2-1 すべての基本 "全探索"に挑戦する。
* 力をつけて蟻さんをやっつける。

## 解答

問題のタイトルは、けんちょん (Otsuki)@drken氏の記事を借用致します。

### 1-1-1 (ハードルの上がった) くじびき ＜難問！！！！！＞

* AtCoder 
  * [JOI 2007 本選 C ダーツ](https://atcoder.jp/contests/joi2008ho/tasks/joi2008ho_c)
* [問題文](https://www.ioi-jp.org/joi/2007/2008-ho-prob_and_sol/2008-ho.pdf#page=6)
  * PDFの3番

* 方針
  * Max4本投げるが、投げなくてもよい。
    * 得点リストに0を加えて、投げても投げてない結果になるようにしておく。
  * 線形探索すると組み合わせが$N^4$になるので、$N=10^3$だとTLEするから工夫が必要。
    * $N^2=10^6$ぐらいなら全探索できる
    * よって、まず$10^6$を計算し、全通りの解を求める
    * 解を求めるときに、また$10^6$通り計算したら結局$10^{12}$通りになるから、ここ以降にさらなる工夫が必要。
    * 探したい値は決まっている（$M - a$）し、探索元のリストもできているので、二分探索で計算量を減らす。


* 実装
  * $N^2$づつに分ける。
  * リストのsortメソッドはinplaceするので変数に入れなくていい
  * 二分探索はbisectライブラリ
  * 探したい値以下の最大値を求めるので`index = bisect.bisect_left(list, target_val)`で、ほしい値があるリストのindexが得られる（目的の値が入っていいる要素の左端もしくは、目的の値がなければ最も近い左側のindexをとるから）。


``` python
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

```



### 例題 1-6-1　三角形
* AtCoder
  * [ARC 004 A 2点間距離の最大値](https://atcoder.jp/contests/arc004/tasks/arc004_1)

* 方針
  * 高々N=100だから全探索で長さを求めてリストに突っ込む
  * リストの最大値を検索する

```python
import math
num = int(input())
pos_list = [[int(item) for item in input().split()] for _ in range(num)]

length_list = []
for i in range(num):
    for k in range(num):
        a = pos_list[i]
        b = pos_list[k]

        length = math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)
        length_list.append(length)

print(max(length_list))
```

* AtCoder
  * [ABC051 B - Sum of Three Integers](https://atcoder.jp/contests/abc051/tasks/abc051_b)

* 方針
  * x,y,zを全て線形探索すると最悪で$N=2500^3 \fallingdotseq 1.5 \times 10^{10}$となりELT（うぉーうぉーうぉー）

  * 実はXとYが決まればZ=S-(X+Y)で一意に決まる。
  * 二重ループで済んだ。
* 実装

``` python
K, S = [int(item) for item in input().split()]

res = 0
for x in range(K+1):
    for y in range(K+1):
        z = S - (x + y)

        if 0 <= z <= K:
            res += 1

print(res)
```

* AtCoder
  * [ABC085 C - Otoshidama](https://atcoder.jp/contests/abc085/tasks/abc085_c)

* 方針
  * x,y,zを全て線形探索すると最悪で$N=2000^3 \fallingdotseq 8 \times 10^{9}$となりELT（うぉーうぉーうぉー）

  * 実は10万円札と5千円札が決まればZ=N-(X+Y)で千円札は一意に決まる。
  * 二重ループで済んだ。
  * N枚に限定しなければ割り算だけで出来る超簡単問題になるのに。。。
  * N枚以下で値段が成り立つとき、N-今の札数がXXの倍数なら成り立つ的な解法はないかしら？？
  
* 実装


``` python
N, Y = [int(item) for item in input().split()]

y = Y //1000
is_search = True

for i in range(N+1):
    for j in range(N+1):
        k = N -(i+j)
        temp_price = 10*i + 5*j + k

        if temp_price == y and 0 <= k <= N:
            print(i,j,k)
            is_search = False
            break

    if not is_search:
        break

if is_search:
    print('-1 -1 -1')
```

### 例題 1-6-2　Ants (POJ No.1852)
* AtCoder
  * [AGC 013 C Ants on a Circle](https://atcoder.jp/contests/agc013/tasks/agc013_c)

* 方針
  * むりすぎる。ギブ
    * >(蟻のオマージュにして類似の発想をする問題です...が、ものすごく難しいのでここから下の問題たちをやって実力をつけてから挑むのがよさそうです、はむこさん提供)　
    * 無謀にもトライしてみたが解説を読んでも実装の仕方が分からない。
    * 素直に現象を再現させてみたがTLEした。$N=10^9$に$N=10^9$をネストさせることになるから、そりゃ無理だ。
    * 解説を読み、ゼッケンを受け渡す様な方法を試してみた。
    * サンプルコードは通ったが何でテストケースが通らないかが分からない。
  
* 実装
  * ACできなかったNG品です
  * 冗長な感じからして正解できなさそう。。。

```python
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

```
