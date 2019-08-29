for _ in range(int(input())):
	s = input()
	f = 0
	for i in range(len(s) - 2):
		if (s[i] == '0' and s[i + 1] == '1' and s[i + 2] == '0') or (s[i] == '1' and s[i + 1] == '0' and s[i + 2] == '1'):
			f = 1
			break
	if f == 1:
		print("Good")
	else:
		print("Bad")
