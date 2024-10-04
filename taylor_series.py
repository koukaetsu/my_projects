from sympy import * #感谢开源项目感谢大家的集思广益

def nth_derivative(f,n): #n阶导数0
    x = symbols('x')
    f_expr = eval(f)
    nth_derivative = diff(f_expr, x, n)
    nth_value = nth_derivative.subs(x, 0)
    return nth_value


def taylor_series_approximation(f,xv,total = 0):
    n = 1000
    for i in range(n+1):
        nth_value = nth_derivative(f,i)
        term = (nth_value/factorial(i))*(xv**i)
        total += term
    return total.evalf()


#e^x=exp(x) log(x)=ln(x) log(x,10)=log_10(x)
f = input("Function:")
xv = float(input("x="))
result = taylor_series_approximation(f, xv)
print(float(result))
