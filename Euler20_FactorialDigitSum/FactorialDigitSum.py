def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n - 1)
    
def sumDig(n):
    if n < 10:
        return n
    else:
        return n % 10 + sumDig(n // 10)

print(sumDig(fact(100)))
