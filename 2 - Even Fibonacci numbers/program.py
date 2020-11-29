def fib():
    a, b = 1, 2
    while True:
        yield a
        a, b = b, a + b

def even(seq):
    for number in seq:
        if not number % 2:
            yield number

def under_million(seq):
    for number in seq:
        if number > 4000000:
            break
        yield number

print(sum(under_million(even(fib()))))
