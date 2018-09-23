def gcd(n, m):
    if n % m == 0:
        return m;
    else:
        return gcd(m, n % m)
    
def otheralg(n, m):
    while n != m:
        if n > m:
            n = n - m
        else:
            m = m - n
    return n
    
    
print(gcd(100,20))
print(otheralg(100, 20))