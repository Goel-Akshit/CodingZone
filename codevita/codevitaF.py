import math
t = int(input())


while(t != 0):
	n, k = input().split()
	n, k = int(n), int(k)

	tickets = input().split()
	tickets = [int(i) for i in tickets]
	flag = False

	for i in range(0, n-1):
		if(tickets[i] > tickets[i+1]):
			avg = 0
			count = 0
			for j in range(i, n):
				avg += tickets[j]
				count += 1

			avg = math.ceil(avg/count)
			flag = True
			break

	if(flag):
		shifter = tickets[i] - avg
		for m in range(i, n-1):
			if(k - shifter >= 0):
				tickets[m] -= shifter
				shifter2 = min(tickets[m+1] + shifter - avg, tickets[m+1])
				tickets[m+1] += shifter
				k -= shifter
				shifter = shifter2
				
	print(max(tickets))
	t -= 1