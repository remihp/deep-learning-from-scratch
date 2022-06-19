# ch03 ニューラルネットワーク(NN)

## 3.1 パーセプトロンからNNへ

<img src="https://user-images.githubusercontent.com/98373139/174490872-eff13f5e-de48-4923-afc5-7ab9e6bf5d38.png" width="800">

## 3.2 活性化関数

- シグモイド関数

$$
h(x)=\frac{1}{1+\exp{(-x)}}
$$

- ステップ関数

$$
f(x) = 
\begin{cases}
0 & (x \leq 0)\\
1 & (x > 0)
\end{cases}
$$


- ReLU関数

$$
f(x) = 
\begin{cases}
x & (x > 0)\\
0 & (x \geq 0)
\end{cases}
=max(0,x)
$$

"NNでは活性化関数に非線形関数を用いる必要がある"

## 3.3 3層NNの実装


## 3.5 出力層の設計

- 回帰問題には恒等関数$\sigma$
- 分類にはソフトマックス関数  
  →和が1になるので確率として解釈する
  
$n$は出力層の数

$$
y_{k} \ =\ \frac{\exp(a_{k})}{\sum\exp( a_{i})}
$$

ソフトマックス関数は、指数関数の値が大きくなりすぎてオーバーフローする

$$
\begin{align*}
y_k &= \frac{\exp(a_{k})}{\sum\exp( a_{i})} \\
&= \frac{C\exp(a_{k})}{C\sum\exp( a_{i})} \\
&= \frac{\exp(a_{k}+\log C)}{\sum\exp( a_{i}+\log C)} \\
&= \frac{\exp(a_{k}+C')}{\sum\exp( a_{i}+C')} \\
\end{align*}
$$

となり、オーバーフロー対策として$C'=-$入力信号の最大値として実装する


## 3.6 バッチ処理

1枚ずつpredict関数で予測するのではなく、100枚ずつまとめて関数に入れて予測していく  
→1枚当たりの処理時間を短縮できる
