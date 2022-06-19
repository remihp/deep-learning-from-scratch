# ch03 ニューラルネットワーク(NN)

## 3.1 パーセプトロンからNNへ


## 3.2 活性化関数

- シグモイド関数

$$
h(x)=\frac{1}{1+\exp{(-x)}}
$$

- ステップ関数

$$
f(x) = 
\begin{cases}
1 & (x \geq 0)\\
0 & ()
\end{cases}

$$

## 3.3 3層NNの実装


## 3.5 出力層の設計


## 3.6 バッチ処理

1枚ずつpredict関数で予測するのではなく、100枚ずつまとめて関数に入れて予測していく  
→1枚当たりの処理時間を短縮できる