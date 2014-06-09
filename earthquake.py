# D. R. Y. "Don't repeat yourself."
# Once your code repeats itself several times, try to find a way to condense things.
# W.E.T. "Write everything twice" is what you don't want to do

# Function goes at the top of the program.
# def is defining a function, meaning you can use it
# When you run with just the three lines below, nothing happens
def greeting():
	name = raw_input("What is your name? ")
	print "Hello, " + name
# Adding this line makes it work. If you leave a string in, error
# Because the error message says no function is given.
#greeting()

# need to pass argment for name
# The function definition, and where you call the function
# end up mirroring each other
def hello(name):
	print "Hello, " + name
# New definition for adding
def add(a, b):
	# return sends arguments to add, "send in on back"
	return a + b
hello("Sonya")

print add(2, 3) + add(4, 5)
