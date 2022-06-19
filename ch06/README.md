# ch06 学習に関するテクニック

## 6.1 パラメータの更新

これまで行った最適化手法(= 確率的勾配降下法(SGD))

$$
W \ \leftarrow \ W-\eta\frac{\delta L}{\delta W}
$$

【SGDの欠点】  
関数の形状が等方的でない(伸びた形の関数)だと、非効率な経路で探索することになる  

【SGDに代わる手法】  
- Momentum
- AdaGrad
- Adam

**Momentum**  
$v$ :物理での"速度" 
$$
v \ \leftarrow \ \alpha v -\eta\frac{\delta L}{\delta W}
$$

$$
W \ \leftarrow \ W+v
$$

**AdaGrad**  
学習係数の減衰(learning rate decay) : 学習が進むにつれて学習係数を小さくする  
AdaGradはパラメータの要素ごとに適応的に学習係数を調整しながら学習する

$$
h \ \leftarrow \ h+\frac{\delta L}{\delta W}\odot\frac{\delta L}{\delta W}
$$

$$
W \ \leftarrow \ W-\eta \frac{1}{\sqrt{h}}\frac{\delta L}{\delta W}
$$

- $\odot$は要素ごとの積
- $\frac{1}{\sqrt{h}}$で学習のスケールを調整

**AdaGrad**  
MomentumとAdaGradを融合させたような手法  
【論文読み】[Adam: A Method for Stochastic Optimization](https://github.com/remihp/paper-reading/blob/main/Adam:%20A%20Method%20for%20Stochastic%20Optimization.md)  


※適切な更新手法はとくべき問題によって異なる

## 6.2 重みの初期値

weight decay : 重みパラメータの値が小さくなるように学習する(重みの値を小さくすることで過学習が起きにくくなる)  

※重みを全て0にするのはNG   

**Xavierの初期値**  
前層のノードの個数を$n$とした場合標準偏差$\frac{1}{\sqrt{n}}$を持つ分布を使う  
→前層のノードの数が多いほど、初期値の重みのスケールは小さくなる  
※活性化関数が線形であることを前提(sigmoid, tanh)

**Heの初期値**  
前層のノードの個数を$n$とした場合標準偏差$\frac{2}{\sqrt{n}}$を持つ分布を使う(ReLU特化の初期値)  

## 6.3 Batch Normalization
各層で適度な広がりを持つように’強制的に’アクティベーションの調整をする

【Batch Normilizationのメリット】  
- 学習を早く進行させることができる（学習係数を大きくできる）
- 初期値にそれほど依存しない
- 過学習を抑制する

データ(MNIST) --> Affine --> **Batch Norm** --> ReLU   
----> Affine --> **Batch Norm** --> ReLU   
----> Affine --> Softmax -->  

ミニバッチごとに正規化を行う(データの分布が平均0,分散1になるように)  
$B=\{ x_1,x_2, \ldots, x_m \}$(ミニバッチ)

$$
\mu_B \ \leftarrow \  \frac{1}{m} \sum_{i=1}^m x_i
$$

$$
\sigma_B^2 \  \leftarrow \  \frac{1}{m} \sum_{i=1}^m (x_i-\mu_B)^2
$$

$$
\hat x_i \  \leftarrow \ \frac{x_i-\mu_B}{\sqrt{\sigma_B^2 + \epsilon}}
$$

さらに固有のスケールとシフトで変換

$$
y_i \  \leftarrow \ \gamma\hat x_i + \beta
$$

※$\gamma=1,\beta=0$からスタート   
◎活性化関数の前か後か？　→論文を参照
- [Batch Normalization: Accelerating Deep Network Training by Reducing Internal Covariate Shift](https://arxiv.org/abs/1502.03167)
- [All you need is a good init](https://arxiv.org/abs/1511.06422)

Batch Normを使用することで学習の進行を促進でき、重みの初期値にロバストになる（初期値にそれほど依存しない）

## 6.4 正則化

【過学習の原因】
- パラメータを大量に持ち、表現力の高いモデル
- 訓練データが少ない

**Weight decay**  
：大きな重みを持つことに対してペナルティを課して過学習を抑制  
重みを$W$としてL2ノルムのweight decayは$\frac{1}{2}\lambda W^2$となり、これを損失関数に加算する。ここで$\lambda$は正則化をコントロールするパラメータ。  

**Dropout**  
：ニューロンをランダムに消去しながら学習する  

訓練：データが流れるたび消去するニューロンをランダムに選択  
テスト：全てのニューロンの信号を伝達するが、各ニューロンの出力に対して、訓練時に消去した割合を乗算して出力

## 6.5 ハイパーパラメータの検証

ハイパーパラメータ：各層のニューロン数、バッチサイズ、学習係数、weight decayなど   

**検証データ**：ハイパーパラメータの調整用のデータ  
（訓練データ：重みやバイアスの学習に利用する）

【ハイパーパラメータの最適化のアプローチ】  

0. ハイパーパラメータの範囲を設定する
1. 設定されたハイパーパラメータの範囲から、ランダムにサンプリングする
2. 1でサンプリングされたハイパーパラメータの値を利用して学習を行い、検証データで認識精度を評価（ただしエポックは小さく設定）
3. 1,2をある回数(100回など)繰り返し、それらの認識精度の結果から、ハイパーパラメータの範囲を狭める

上記を繰り返し行い、ハイパーパラメータの範囲を絞り込んでいき、ある程度絞り込んだ段階で、その絞り込んだ範囲からハイパーパラメータの値を一つ選び出す。
