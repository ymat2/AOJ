int(input())
cells = map(int, input().split())

faces = [1]
tface = 1
prev = 0

for i in cells:
    if prev == 0 and i == 1:
        prev = 1
        tface += 1
    elif prev == 1 and i==1:
        tface += 1
    elif prev == 1 and i == 0:
        faces.append(tface)
        tface = 1
    else:
        continue
    faces.append(tface)

print(max(faces))