def countBits(n):
    ans = [0] * (n + 1)
    x = 0
    b = 1
    while b <= n:
        print (b, n)
        while x < b and x + b <= n:
            ans[x + b] = ans[x] + 1
            x += 1
            x = 0  # reset x
            b <<= 1  # b = 2b
    return ans

i = 0
j = 1
while i < 10:
    while j < 11:
        print(i, j)
        j+=1
    i+=1

print(countBits(10))
