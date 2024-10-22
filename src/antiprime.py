## ADD WHATEVER ARGUMENTS ARE NECESSARY TO THE MAIN FUNCTION
## IN THE SAME ORDER AS THE ARGUMENTS ARE TAKEN FROM THE
## COMMAND LINE SPECIFIED BELOW
import sys

def main(x) :
	## YOU CODE SHOULD START HERE AST THE SAME
	## IDENTATION AS THIS COMMENT
	d = 0                              
	n = 1	
	while n <= x:
		if x % n == 0:
			d = d+ 1 
		n = n + 1 
	l = x - 1
	b = 0

	while l >= 1:
		a = 1
		t = 0 
		while a <= l:
			if l % a == 0:
				t = t + 1   
			a = a + 1
		if t > b:
			b = t
		l = l - 1  

	## THE LAST LINES OF YOUR CODE SHOULD EITHER
	## RETURN THE VALUE "anti-prime" or "not anti-prime"
	## REPLACE THE FOLLOWING LINE BY WHATEVER LINES
	## OF CODE ALLOW THIS FUNCTION TO RETURN THE VALUE
	## "anti-prime" or "not anti-prime"
	if d > b:
		return "anti-prime"
	else:
		return "not anti-prime"
	
## DO NOT REMOVE THIS LINE BELOW
if __name__ == "__main__" :
	x = int(sys.argv[1])

	## MODIFY THE LINE BELOW AND ADD BEFORE WHATEVER LINES ARE NECESSARY
	## TO RUN THIS PROGRAM AS, FOR INSTANCE:
	## $ python antiprime.py 6
	## WHERE THE FIRST ARGUMENT IS A POSITIVE INTEGER NUMBER FOR WHICH
	## YOU WANT TO FIGURE OUT WHETHER IS ANTI-PRIME OR NOT
	print(main(x))

