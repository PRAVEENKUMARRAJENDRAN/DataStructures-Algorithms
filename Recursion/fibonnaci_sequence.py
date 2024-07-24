def fib(n):
    if n <= 1:
        return n
    
    return fib(n-1) + fib(n-2)


n = 5
fib_squence = []
for i in range(5):
    fib_squence.append(fib(i))

print(fib_squence)
