def oddNumbers(l, r):
    i = l
    l = []
    while i <= r:
        if(i%2) == 0:
            l.append(i)
    return l

print(oddNumbers(2,4))