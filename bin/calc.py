def add(x,y):
	z = x + y
	return z

def substract(x,y):
	z = x-y
	return z

a = float(input("Input your first number = "))
b = float(input("Input your second number = "))

print ("The result of addition of {} and {} = {}".format(a,b,add(a,b)))
print ("\nThe result of substraction of {} and {} = {}".format(a,b,substract(a,b)))