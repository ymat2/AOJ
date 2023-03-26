class vlist:

	def __init__(self):
		self.l = []

	def pushb(self, x):
		self.l.append(x)

	def ra(self, p):
		return self.l[int(p)]

	def popb(self):
		del self.l[-1]

tlist = vlist()

for i in range(int(input())):
	q = input().split()
	if q[0] == '0':
		tlist.pushb(q[1])
	elif q[0] == '1':
		print(tlist.ra(q[1]))
	else:
		tlist.popb()

