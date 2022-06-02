# coding: utf-8
class Man:
    """サンプルクラス"""

    def __init__(self, name): # コンストラクタ(インスタンスが作成される際に一度だけ呼ばれる)
        self.name = name
        print("Initilized!")

    def hello(self):
        print("Hello " + self.name + "!")

    def goodbye(self):
        print("Good-bye " + self.name + "!")

m = Man("David") # インスタンス
m.hello()
m.goodbye()