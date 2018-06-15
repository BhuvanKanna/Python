def bubblesort(x):
	length = len(x) - 1
	sorted = False
	while not sorted:
		sorted = True
		for i in range(length):
			if x[i] > x[i + 1]:
				sorted = False
				x[i], x[i + 1] = x[i + 1], x[i]
	return x
a=input("Put in a number:")
a=int(a)
b=input("Put in a number:")
b=int(b)
c=input("Put in a number:")
c=int(c)
d=input("Put in a number:")
d=int(d)
e=input("Put in a number:")
e=int(e)
f=input("Put in a number:")
f=int(f)
g=input("Put in a number:")
g=int(g)
print (bubblesort([a ,b, c, d, d, f, g]))
