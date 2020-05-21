class Att:
    def __init__(self, No):
        self.No = No
        self.listd = []
    def f(self, d):
        self.listd.append(d)

if __name__ == '__main__':
    x = Att("No1")
    y = Att("No2")
    x.f(100)
    y.f(200)
    print(x.No, x.listd)
    print(y.No, y.listd)