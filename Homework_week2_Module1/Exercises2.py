def count_chars(s) :
	a = {}
	for i in s :
		if i in a :
			a[i]+= 1
		else :
			a[i] = 1
	print(a)

