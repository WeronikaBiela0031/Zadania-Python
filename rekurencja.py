def factorial(n):
    i = 1
    silnia = 1
    if n == 0:
        return silnia
    else:
        while i < n + 1:
            silnia = silnia * i
            i += 1
        return silnia


# print(factorial(N))

def fibonacci(n):
    F = [0, 1]
    i = 2
    fibonacci = 1
    if n == 0 or n == 1:
        return n

    else:
        while i < n + 1:
            f = sum(F)
            F[0] = F[1]
            F[1] = f
            i += 1
        return F[1]

# print(fibonacci(N))
