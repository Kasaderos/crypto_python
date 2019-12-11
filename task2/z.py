
def gen():
    n = 4
    j = n - 2
    while j != -1 and L[j] >= L[j+1]:
        j -= 1
    if j == -1:
        return []
    k = n - 1
    while L[j] >= L[k]:
        k -= 1
    L[k], L[j] = L[j], L[k]
    l = j + 1
    r = n - 1
    while l < r:
        L[l], L[r] = L[r], L[l]
        l += 1
        r -= 1
    return L
    
L = [i for i in range(4)]
while True:
    l = gen()
    if l != []:
        print(l)
    else:
        break

