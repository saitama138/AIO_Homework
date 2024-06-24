def word_count(file_path) :
	f = open("P1_data.txt", 'r')
	a = {}
	for line in f :
		word = line.split()
		for words in word :
			if words in a :
				a[words]+= 1
			else :
				a[words] = 1

	f.close()
	return a

if __name__ == '__main__' :
	file_path = 'P1_data.txt'
	print(word_count(file_path))


