class Setbit:
    def set(self, a, b):

        if a == b:
            return 2 ** a
        else:
            return 2**a + 2**b


a = int(input())
b = int(input())
object = Setbit()
print(object.set(a, b))