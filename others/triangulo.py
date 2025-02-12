class LadoInvalido(Exception):
    pass

class Triangulo:
    def __init__(self, a:float, b:float, c:float):
        Triangulo.validar(a, b, c)
        self._a = a
        self._b = b
        self._c = c
    
    @staticmethod
    def validar(a:float, b:float, c:float):
        if not (a + b > c and a + c > b and c + b > a):
            raise LadoInvalido("Lados não formam um triângulo")

    @property
    def a(self):
        return self._a

    @a.setter
    def a(self, valor:float):
        Triangulo.validar(valor, self._b, self._c)
        self._a = valor
    
    @property
    def b(self):
        return self._b

    @b.setter
    def b(self, valor:float):
        Triangulo.validar(self._a, valor, self._c)
        self._b = valor

    @property
    def c(self):
        return self._c

    @c.setter
    def c(self, valor:float):
        Triangulo.validar(self._a, self._b, valor)
        self._c = valor



t1 = Triangulo(3, 2, 4)
t1.a = 4
