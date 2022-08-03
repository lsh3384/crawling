class test:
    att1 = 0
    att2 = 0
    def __init__(self, v1, v2):
        self.att1 = v1
        self.att2 = v2

    def meth(self):
        print(self.att1)


a = test(1, 2)

print(vars(a))