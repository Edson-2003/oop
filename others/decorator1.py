# Crie um decorator que repita a execução de uma função um determinado número de vezes.
# Crie um decorator chamado repeat que aceite um argumento n, indicando quantas vezes a função deve ser repetida.
# Aplique o decorator a uma função que imprime uma mensagem, para que ela seja repetida múltiplas vezes.

def repeat(n:int):
    def interna(func):
        def aninhada(*args, **kwargs):
            for i in range(n):
                func() # invocar a função n vezes
        return aninhada
    return interna

@repeat(5)
def diga_uau():
    print("Uau!")

diga_uau()
