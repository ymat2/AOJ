input()
m = input().strip().split(" ")
n = input().strip().split(" ")
print(len([i for i in m if i in n]))
