def A(n,i):
    print(n,i)
    if n == 0:
        return i+1
    elif i == 0 and n > 0:
        return A(n-1,1)
    elif n > 0 and i > 0:
        return A(n-1, A(n, i - 1))

n = 3
sum = 0
for i in range (1, n):
    sum += A(n,i)

print(sum)