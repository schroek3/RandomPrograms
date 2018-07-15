#Ken Schroeder
#06.25.16
#Home, 2225 SE 35th Pl, Portland
#Sunny Morning
#A program that lists out the first N Ingham Numbers
#An Ingham number is a number whose binary representation is n 1's followed by n-1 0's
#inghamNumbers.py

'''
Background: When talking with Hannah about perfect numbers, she stumbled across the fact that the binary representation of all perfect numbers is a series of n 1's followed by n-1 0's. While all perfect numbers fit this form, not all numbers of this form are perfect numbers. They are Ingham Numbers.

Mathematics: I haven't look at the math, but it suffices to say that all numbers of the form 2^(n-1)*(2^n-1) are Ingham numbers. If n is a Mersenne prime, then the number is perfect.

Possible Program Improvements: It might be nice to allow the user to input
	multiple numbers, rather than re-run the program. This also might be fun to 
	put into a bigger program that fines primes, and perfect numbers, and
	Schroeder-Stark primes, etc.

References:
	https://en.wikipedia.org/wiki/List_of_perfect_numbers
	https://en.wikipedia.org/wiki/Mersenne_prime

'''
#******************************************************************************
# Functions
import time
start = None
speedTrials=10000

#------------------------------------------------------------------------------
# inghamNumbers(int)
# finds the base 10 representation of an Ingham number
#------------------------------------------------------------------------------
def inghamNumbers(n):
   inghamNumber = "1"
   for x in range (1, n):
   	newNum = "1" + inghamNumber + "0"
   	inghamNumber = newNum
   return int(int(inghamNumber, 2))

#------------------------------------------------------------------------------
# printInghamNumbers(void)
# prints the first n Ingham numbers, controlled by user input
# prefaces the nth Ingham number with a star if that number is perfect
#------------------------------------------------------------------------------
def printInghamNumbers():
	global start
	n = speedTrials
	start = time.time()
	for x in range (1,n+1):
		theNumber = inghamNumbers(x)
		if isPerfect(theNumber):
			print "*",
		print str(x) + ". " + str(theNumber)

#-------------------------------------------------------------------------------
# isPerfect(int)
# returns true if a number is contained in the vector of perfect numbers
#-------------------------------------------------------------------------------
def isPerfect(num):
	perfectNums = [6, 28, 496, 8128, 33550336, 8589869056, 137438691328,
	 2305843008139952128, 2658455991569831744654692615953842176, 
	 191561942608236107294793378084303638130997321548169216]
	if num in perfectNums:
		return True
	return False

#------------------------------------------------------------------------------
# howManyInghamNumbers(void)
# receives user input for how many Ingham Numbers they'd like to see
# helper function for printInghamNumbers
#------------------------------------------------------------------------------
def howManyInghamNumbers():
  return 10000
	#return raw_input("How many Ingham Numbers would you like to see?\n\t>")
#*******************************************************************************

# main()

start=time.time()
printInghamNumbers()
end = time.time()
print "Program duration: ",
print(end-start)
