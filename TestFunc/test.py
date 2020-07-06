def fib(n):
    start, next = 0, 1
    while start < n:
        print(start,end=' ')
        start, next = next, start+next
    print()

def fib2(n):
    result = []
    a,b = 0, 1
    while a < n:
        result.append(a);
        a, b = b, a+b
    return result
print('Ok')
f100=fib2(100)
f100
fib(100)

