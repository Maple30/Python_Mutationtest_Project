# Python code to demonstrate naive 
# method to compute gcd ( recursion ) 
import sys
sys.setrecursionlimit(100000)


def gcd(a,b): 
	if(b == 0): 
		return a 
	else:
		return gcd(b,a%b)

a = 48
b= 60

# prints 12 
print ("The gcd of 60 and 48 is : ",end="") 
print (gcd(a,b)) 
