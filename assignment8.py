class A:
    def __init__(self, a, b, c):
        self.__a = a
        self._b = b
        self.c = c
    
    def display(self):
        print("Values in class A:")
        print("a:", self.__a)
        print("b:", self._b)
        print("c:", self.c)


class B(A):
    def display(self):
        try:
            print("Values in class B:")
            print("a:", self.__a)  # Raises an exception
        except AttributeError:
            print("Cannot access private member 'a' in class B.")
        print("b:", self._b)
        print("c:", self.c)


obj_b = B(1, 2, 3)
obj_b.display()
