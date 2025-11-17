def caching_fibonacci():
    cache = {}
    def fibonacci(n) -> int:
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        elif n > 1:
            return fibonacci(n-1) + fibonacci(n-2)
        else:
            if n in cache:
                cache[n] = fibonacci(n-1) + fibonacci(n-2) 
                return cache[n]
            else:
                print('Value n not in cache')
    return fibonacci



fib = caching_fibonacci()

print(fib(10))
print(fib(15))



