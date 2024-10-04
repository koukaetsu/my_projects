a = int(input('a='))
x = int(input('x='))

b = -a ** 2 + x

def solve(a,b): 
    try:
        return a + b/(a+solve(a,b))
    except RecursionError:
        return 0

print(solve(a,b))
