# [やってみた]　AtCoder 版！蟻本 (初級編) [随時更新]

## はじめに

[AtCoder 版！蟻本 (初級編)](https://qiita.com/drken/items/e77685614f3c6bf86f44)に蟻本記載例題の類似問題を[AtCoder](https://atcoder.jp/?lang=ja)XXXXXXXXXXXXXXXX]


を利用してジャッジできるアルゴリズムの良問が選別されている。

けんちょん (Otsuki)@drken氏に感謝。

## 目的

* 筆者の競技プログラミングの成績向上のため、アルゴリズムを勉強する。
* [AtCoder 版！蟻本 (初級編)](https://qiita.com/drken/items/e77685614f3c6bf86f44)に記載の問題を解説しながら記述することで、アルゴリズムの基礎を身に着ける。
* コードと解説を掲載し、諸兄（姉）からの指摘を受けることで見落としていた課題を補完する。

## 今後

* 上記記事に掲載された問題の完走を目指す。

## 解答

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
    * よってまず$10^6$を計算し、これ(a)の全通りの解を求める
    * 解を求めるときにまた、$10^6$通り計算したら結局$10^12$になるからここに工夫が必要。
    * 探したい値は決まっている（$M - a$）し、探索元のリストもできているので、二分探索

* 実装
  * $N^2$づつに分ける。
  * リストのsortメソッドはinplaceaするので変数に入れなくていい
  * 二分探索はbisectライブラリ
  * 探したい値以下の最大値を求めるので`index = bisect.bisect_left(list, target_val)`で、ほしい値があるリストのindexが得られる。


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

