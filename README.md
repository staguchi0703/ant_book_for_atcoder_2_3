# [やってみた（途中）]　AtCoder 版！蟻本 (初級編) [2-3 値を覚えて再利用 "動的計画法"]

## はじめに

筆者はAtCoderを取り組み始めたアラフォー・Unコーダである。

[AtCoder 版！蟻本 (初級編)](https://qiita.com/drken/items/e77685614f3c6bf86f44)に蟻本記載例題の類似問題が記載されている。

[AtCoder](https://atcoder.jp/?lang=ja)を利用してジャッジできるアルゴリズムの良問が選別されているので、初学者にうってつけである。

上記記事著者である、けんちょん (Otsuki)@drken氏に感謝。

筆者は[AtCoder 版！蟻本 (初級編)](https://qiita.com/drken/items/e77685614f3c6bf86f44)を頼りにスキルアップを図っている途中である。
* [1 いざチャレンジ！でもその前に --- 準備編に取り組んだ過去記事](https://qiita.com/tagtagtag/items/eaa0655d26cdcbd5202e)


## 目的

* 筆者の競技プログラミング成績向上を図るため、動的計画法を習得する。
* [AtCoder 版！蟻本 (初級編)](https://qiita.com/drken/items/e77685614f3c6bf86f44)に記載の問題を解説しながら記述することで、アルゴリズムの基礎を身に着ける。
* コードと解説を掲載し、諸兄（姉）からの指摘を受けることで見落としていた課題を補完する。

## 解答

問題のタイトルは、けんちょん (Otsuki)@drken氏の記事を借用致します。

### 例題 2-3-1　01ナップサック問題

#### [AOJ Course 0-1ナップザック問題](http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DPL_1_B&lang=jp)

* 方針
  * 数字の間に＋を入れよう。
  * 入れらる
* 実装
  * 二次元リストを`some_list[a][b]= number`と言った具合にスライスで代入しようとすると、`some_list[a] = [, , number, , ] * b`といった具合になり狙った座標だけ書き換える事が出来なかった。
  * 新規記事を起こして検証をする
   

```python

```

### [TDPC A コンテスト](https://atcoder.jp/contests/tdpc/tasks/tdpc_contest)

* 方針
  * 数字の間に＋を入れよう。
  * 入れらる
* 実装
  * 二次

```python

```


### [TDPC D コンテスト](https://atcoder.jp/contests/tdpc/tasks/tdpc_dice)

* 方針
  * さいころの目の積の倍数
    * さいころの目で割り切れなければ解なし
    * さいころの目の因数は`[2,3,5]`
  * dpの考え方
    * N個通り
    * 因数の種類で次元を作って、それぞれの使う数
    * 上記を鑑みてdpテーブルを作る
      * `dp[N][2の因数の数][3の因数の数][5の因数の数]`
      * 値はその組み合わせが発生する確率
      * `dp[0][0][0][0]=1を初期条件`
      * 漸化式は`dp[n+1][factor2 + m][factor3 + l][factor5 +k] = dp[n][factor2][factor3][factor5]　+ その組み合わせになる確率`
        * ここでm,l,kはn+1回目のさいころの目の因数の数
  * 算出する確率はDの倍数だから、因数の数はDの素因数の数を超えてもよい。
* 実装
  * n,m,l,kの組み合わせはいろいろあり、ルートが様々
    * `dp[n+1][factor2 + m][factor3 + l][factor5 +k] += dp[n][factor2][factor3][factor5]*1/6`としておけば、その状態にたどり着く確率の和となる。
  * 素因数の数はDの素因数の数以上であれば良いので、各因数の数は`min(factor + 1(もしくは2), Dの因数)`として上限超えたら頭打ちにしてやれば良い
  * 4はn+1で2の数を+2する
  * 1はn+1で因数の操作をしない

```python

```