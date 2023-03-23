def linsert(str_, lst_):
	lst_[str_] = True

def lfind(str_, lst_):
	if str_ in lst_:
		return "yes"
	else:
		return "no"

n = int(input())
lst = {}  # in演算は辞書型が最強
for i in range(n):
	in_ = input().split()
	if in_[0] == "insert":
		linsert(in_[1], lst)
	elif in_[0] == "find":
		print(lfind(in_[1], lst))
