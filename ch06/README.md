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

$$

$$