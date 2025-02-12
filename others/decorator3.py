def convert_result(tipo):
    def decorator(func):
        def wrapper(*args, **kwargs):
            # fazendo o cast do retorno da func
            return (tipo)(func(*args, **kwargs))
        return wrapper
    return decorator


@convert_result(float)
def soma(a: int, b: int) -> int:
    return a + b

result = soma(5, 5)
print(result)
