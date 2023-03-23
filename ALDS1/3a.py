lst_input = input().split()
t_lst = []

def operand(i, t_lst):
	if i == "+":
		a = t_lst[-2]
		b = t_lst[-1]
		del t_lst[-2]
		del t_lst[-1]
		t_lst.append(a+b)
	elif i == "-":
		a = t_lst[-2]
		b = t_lst[-1]
		del t_lst[-2]
		del t_lst[-1]
		t_lst.append(a-b)
	elif i == "*":
		a = t_lst[-2]
		b = t_lst[-1]
		del t_lst[-2]
		del t_lst[-1]
		t_lst.append(a*b)
	else:
		t_lst.append(int(i))

for i in lst_input:
	operand(i, t_lst)
#	print(t_lst)

print(t_lst[0])
