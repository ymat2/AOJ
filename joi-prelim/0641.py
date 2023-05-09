n,a,b,c,d = map(int, input().split())

def count_set(n,i,j):
    nset = 0
    nnum = 0
    while nnum < n:
        nset += 1
        nnum += i
    return j * nset

total_x = count_set(n, a, b)
total_y = count_set(n, c, d)

print(min(total_x, total_y))
