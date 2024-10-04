def solve(n,k,total = 1):
    if k >100:
        return total
    n = n * k # 计算阶乘 n!
    total += 1/n # 累加 1/n!
    k = k + 1
    return solve(n,k,total)


print(solve(1,1))
