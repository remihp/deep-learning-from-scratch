# coding: utf-8

# 単純なレイヤの実装
class MulLayer: # 乗算レイヤ
    def __init__(self): # 初期化
        self.x = None
        self.y = None

    def forward(self, x, y): # 順伝播
        self.x = x
        self.y = y                
        out = x * y

        return out

    def backward(self, dout): # 逆伝播(乗算ではひっくり返した値を乗算する)
        dx = dout * self.y
        dy = dout * self.x

        return dx, dy


class AddLayer: # 加算レイヤ
    def __init__(self):
        pass # 何もしない

    def forward(self, x, y): # 順伝播
        out = x + y

        return out

    def backward(self, dout): # 逆伝播(加算では入力をそのまま流す)
        dx = dout * 1
        dy = dout * 1

        return dx, dy
