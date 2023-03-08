input()
s = input()

ord = {"J":0, "O":1, "I":2}
print("".join(sorted(s, key = lambda x: ord[x])))
