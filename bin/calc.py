def add(x,y):
	z = x + y
	return z

def substract(x,y):
	z = x-y
	return z

def multiply(x,y):
	z = x*y
	return z

def div(x,y):
	z = x/y
	return z

def rem(x,y):
	z = x%y
	return z

print ("Simple Calculator")
print ("========================")
a = float(input("Input your first number = "))
b = float(input("Input your second number = "))
print ("========================")

print ("The result of addition of {} and {} = {}".format(a,b,add(a,b)))
print ("The result of substraction of {} and {} = {}".format(a,b,substract(a,b)))
print ("The result of multiplication of {} and {} = {}".format(a,b,multiply(a,b)))
print ("The result of division of {} and {} = {}".format(a,b,div(a,b)))
print ("The remaining of the division between {} and {} = {}".format(a,b,rem(a,b)))