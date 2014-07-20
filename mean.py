import sys
sum = 0
n=0

# sum input values
# modify the variable name
# adding comments just to test
for num in open('data.txt'): #open as existing file directely
	sum += float(num)
	n += 1

print sum/n
