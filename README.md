# [やってみた（苦戦中！）]　AtCoder 版！蟻本 (初級編) [2-1 すべての基本 "全探索"]

## はじめに

筆者はAtCoderを取り組み始めたアラフォー・Unコーダである。

[AtCoder 版！蟻本 (初級編)](https://qiita.com/drken/items/e77685614f3c6bf86f44)に蟻本記載例題の類似問題が記載されている。

[AtCoder](https://atcoder.jp/?lang=ja)を利用してジャッジできるアルゴリズムの良問が選別されているので、初学者にうってつけである。

上記記事著者である、けんちょん (Otsuki)@drken氏に感謝。

筆者は[AtCoder 版！蟻本 (初級編)](https://qiita.com/drken/items/e77685614f3c6bf86f44)を頼りにスキルアップを図っている途中である。
* [1 いざチャレンジ！でもその前に --- 準備編に取り組んだ過去記事](https://qiita.com/tagtagtag/items/eaa0655d26cdcbd5202e)


## 目的

* 筆者の競技プログラミング成績向上を図る。
* [AtCoder 版！蟻本 (初級編)](https://qiita.com/drken/items/e77685614f3c6bf86f44)に記載の問題を解説しながら記述することで、アルゴリズムの基礎を身に着ける。
* コードと解説を掲載し、諸兄（姉）からの指摘を受けることで見落としていた課題を補完する。

## 今後

* 2-1 の残り問題をこの記事に追加する
* 2-2 猪突猛進！ "貪欲法"に挑戦する。


## 解答

問題のタイトルは、けんちょん (Otsuki)@drken氏の記事を借用致します。

### 例題 2-1-1　部分和問題

#### [ABC 045 C - たくさんの数式](https://atcoder.jp/contests/arc061/tasks/arc061_a)

* 方針
  * 数字の間に＋を入れよう。
  * 入れらる位置が文字数-1個あり、それぞれの場所で入れるか入れないかの二択だから、$2^{N-1}$通りの数式が出来上がる。
  * 入れる入れない・・・を考えると二分木の末端を拾って行けばよい。
  * 再帰関数を使えば入れる（+）、入れない（0）として簡単に組み合わせを表現できる。
  * 数式の計算は`eval()`を使えば、文字列から直で計算できるので簡単。
  * えっ！bit全探索？？？？？？
    * `if ((i >> j) & 1):`あ～これね、うっかりJavaでも参照しちゃったかな。てへぺろ・・・
    * ええええ、pythonでもこんな書き方あるの？！？！
    * `(i >> j)`←の意味は、整数iを2bitに変換して（0b0100111みたいな）、下j桁を切り捨てる。
    * `((i >> j) & 1)` ←の意味は、2bitで&の左側と右側を比較し（右の桁数に合わせるのでこの場合は左の下一桁と右の一桁1）、お互いに1なら、1を返す（ビット演算子＆[理論積]）。
    * 再帰関数使わなくても楽に求まるのね。。。
    * [Python ビット演算 超入門を参考にさせていただきました](https://qiita.com/7shi/items/41d262ca11ea16d85abc)

 

* 実装
  * 再帰関数版
    * 再帰関数で数字の間に+をいれるか（+）、入れないか（0）の組み合わせをリストUPする。ただしこの方法は、全ての文字を使っていない場合も含まれてしまう。
    * 今回の問題では全ての数字を使った式なので、組み合わせの要素数は数字の文字数-1で、組み合わせの数は$2^{数字の文字数-1}$個である。
    * よって、組み合わせの要素数でフィルタリングする。
    * あとはfor文でも回して間に⁺入れて文字列を作る。
    * 文字列は`eval()`評価する。
    * 合計とって出力


```python
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
```

  * bit演算子版
    * 与えられた数字の桁数をnとすると
    * $2^{n-1}$通り組み合わせがある。これをbit表現するとどの隙間に+が入るを表すことができる
      * 例0b01010111と表現できると1の位置に+が入る
    * 2^{n-1}$通り組み合わせの全探索`for i in range(2**(n-1))`を行う
    * bit演算でどの桁に₊を入れるか条件分けを行う。`if ((i >> j) & 1)`
      * jで全桁なめている
    * めっちゃさっぱりなコード！

``` python
S = input()

res_list = []

for i in range(2**(len(S)-1)):
    temp_s = ''
    for j in range(len(S)):
        temp_s += S[j]
        if ((i >> j) & 1):
            temp_s += '+'
    # print(temp_s)
    res_list.append(temp_s)

temp_S_list = [eval(item) for item in res_list]

print(sum(temp_S_list))
```


#### [ABC 079 C - Train Ticket](https://atcoder.jp/contests/abc079/tasks/abc079_c)

* 方針
  * 数字の間に＋か-を入れよう。
  * 上記ABC045Cと同じくbit全探索する

 

* 実装
  * 再帰関数版
    * 再帰関数で数字の間に+をいれるか、-を入れるかの組み合わせをリストUP
    * eval()で計算した結果と7を比較して見つかったら回答する


```python
ABCD = input()

N = len(ABCD)


for i in range(2**(N-1)):
    temp_res = ''
    for j in range(N-1):
        temp_res += ABCD[j]
        if ((i >> j) & 1):
            temp_res += '+'
        else:
            temp_res += '-'
    temp_res += ABCD[-1]

    if eval(temp_res) == 7:
        res = temp_res + '=7'
        break

print(res)
```

