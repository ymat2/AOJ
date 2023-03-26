"""
class vlist:

	def __init__(self):
		self.l = []

	def tpush(self, d, x):
		if d == '0':
			self.l = [int(x)] + self.l
		else:
			self.l = self.l + [int(x)]

	def trand(self, p):
		return self.l[int(p)]

	def tpop(self, d):
		if d == '0':
			del self.l[0]
		else:
			del self.l[-1]
""" #deque is faster than list

from collections import deque

class vlist:
	def __init__(self):
		self.d = deque()

	def tpush(self, d, x):
		if d == '0':
			self.d.appendleft(int(x))
		else:
			self.d.append(int(x))

	def trand(self, p):
		return self.d[int(p)]

	def tpop(self, d):
		if d == '0':
			self.d.popleft()
		else:
			self.d.pop()

tlist = vlist()

for i in range(int(input())):
	q = input().split()
	if q[0] == '0':
		tlist.tpush(q[1], q[2])
	elif q[0] == '1':
		print(tlist.trand(q[1]))
	else:
		tlist.tpop(q[1])

