def func(x):
    fx = x ** 3 - x**2 + x - 1
    return fx

def solve(a,b):
    a = a
    b = b
    fa = func(a)
    fb = func(b)

    if fa * fb > 0:
        print("该区间不存在根")

    else:
        while abs(a - b) > 0.0001:
            xmid = (a + b)/2
            fx = func(xmid)

            if fa * fx < 0:
                b = xmid
                fb = fx
                print(f"区间:[{a},{b}],零点近似值:{b}")
            elif fb * fx < 0:
                a = xmid
                fa = fx
                print(f"区间:[{a},{b}],零点近似值:{a}")

solve(-1,2)
