n = int(input())
m = n
value = 0
while(m != 0):
	value += m
	m -= 1

value = value * 2
pointer1 = 1
pointer2 = value - n

for i in range(n):
	for j in range(1):
		for k in range(i):
			print("**",end="")
		print("%d" %(pointer1),end="")

	for a in range(1, n-i):
		pointer1 += 1
		print("0%d" %(pointer1), end="")

	pointer1 += 1

	for b in range(1,n+1-i):
		pointer2 +=  1
		print("0%d" %(pointer2), end="")

	pointer2  = pointer2 - 2*(n-i-1) - 1
 
	print()

