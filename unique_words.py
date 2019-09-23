def unique_words():
	item= open(" https://www.gutenberg.org/files/2600/2600-0.txt",'r')
		x=input ('Enter your sentence :')
		y=x.split()
		y.sort()
		for y in sorted(y):
print (y)
unique_words()
