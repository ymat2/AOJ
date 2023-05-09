def cmd(_input_, lst):
	if _input_ == "deleteFirst":
		del lst[0]
	elif _input_ == "deleteLast":
		del lst[-1]
	else:
		_input_ = _input_.split()
		if _input_[0] == "insert":
			lst.insert(0, int(_input_[1]))
		elif _input_[0] == "delete":
			try:
				lst.remove(int(_input_[1]))
			except ValueError:
				pass

n = int(input())
lst = []
for i in range(n):
	cmd(input(), lst)
print(" ".join(list(map(str, lst))))

# まだTLE
