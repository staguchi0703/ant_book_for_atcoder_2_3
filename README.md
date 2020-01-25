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


### [TDPC D コンテスト](https://atcoder.jp/contests/tdpc/tasks/tdpc_contest)

* 方針
  * 数字の間に＋を入れよう。
  * 入れらる
* 実装
  * リスト内包表記を使った、3項演算子の書き方
  `some_list = [1 if m == D else 0 for i in range(n)]`

```python

```