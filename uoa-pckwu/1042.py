def as_numbers(text):
	out_ = ""
	tabs = text.split(" ")
	for i in tabs:
		out_ += str(len(i))
	return out_

while True:
	in_ = input()
	if in_ == "END OF INPUT":
		break
	else:
		print(as_numbers(in_))
