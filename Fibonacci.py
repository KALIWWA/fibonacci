

def calculate():
    i = 0
    j = 1
    k = 0
    fib = 0
    how_many = int(input('How many Fibonacci numbers do You want to see?: '))
    while i < int(how_many):
        fib = j + k
        j = k
        k = fib
        i += 1
        print(i, fib)


calculate()
