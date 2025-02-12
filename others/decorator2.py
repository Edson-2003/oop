def limit_calls(n: int):
    def decorator(func):
        count = 0 # contador de execuções
        def wrapper(*args, **kwargs):
            nonlocal count # usar count de fora
            if count >= n:
                raise Exception("Limite de chamadas excedido.")
            count += 1
            return func(*args, **kwargs)
        return wrapper
    return decorator

@limit_calls(3)
def func():
    print("Chamando func")


func()
func()
func()
func() # lançar exceção
