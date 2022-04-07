class Baz():
    def __init__(self, num):
        self.a = num
        print(self.a)

def foo(num):
    obj = Baz(num)