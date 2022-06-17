src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
a = []
for i in range(len(src) - 1):
    n = src[i]
    i += 1
    m = src[i]
    if m > n:
        a.append(m)
print(a)



