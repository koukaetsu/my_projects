def solve():
    n = 1000000
    total = 0
    for i in range(n):
        term = (-1)**i/(2*i+1)
        total += term
    return 4*total

print(solve())
