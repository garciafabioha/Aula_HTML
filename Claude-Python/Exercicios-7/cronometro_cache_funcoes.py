import time
import functools

# -------------------------------------------------
# DECORATOR 1 - CRONÔMETRO
# -------------------------------------------------

def cronometro(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):

        inicio = time.perf_counter()

        resultado = func(*args, **kwargs)

        fim = time.perf_counter()

        tempo = fim - inicio

        print(
            f"{func.__name__} levou "
            f"{tempo:.6f} segundos."
        )

        return resultado

    return wrapper

# -------------------------------------------------
# DECORATOR 2 - CACHE SIMPLES
# -------------------------------------------------

def cache_simples(func):
    cache = {}
    @functools.wraps(func)
    def wrapper(*args, **kwargs):

        chave = (args, tuple(sorted(kwargs.items())))

        if chave in cache:
            return cache[chave]

        resultado = func(*args, **kwargs)

        cache[chave] = resultado

        return resultado

    return wrapper

# -------------------------------------------------
# FIBONACCI SEM CACHE
# -------------------------------------------------

@cronometro
def fibonacci_sem_cache(n):

    if n <= 1:
        return n

    return (
        fibonacci_puro(n - 1)
        + fibonacci_puro(n - 2)
    )


def fibonacci_puro(n):

    if n <= 1:
        return n

    return (
        fibonacci_puro(n - 1)
        + fibonacci_puro(n - 2)
    )

# -------------------------------------------------
# FIBONACCI COM CACHE
# -------------------------------------------------

@cronometro
@cache_simples
def fibonacci_com_cache(n):

    if n <= 1:
        return n

    return (
        fibonacci_com_cache_interno(n - 1)
        + fibonacci_com_cache_interno(n - 2)
    )

@cache_simples
def fibonacci_com_cache_interno(n):

    if n <= 1:
        return n

    return (
        fibonacci_com_cache_interno(n - 1)
        + fibonacci_com_cache_interno(n - 2)
    )

# -------------------------------------------------
# TESTE
# -------------------------------------------------

numero = 35

print("SEM CACHE")
resultado = fibonacci_sem_cache(numero)
print(f"Fibonacci de {numero}: {resultado}")

print()

print("COM CACHE")
resultado = fibonacci_com_cache(numero)
print(f"Fibonacci de {numero}: {resultado}")