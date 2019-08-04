n = int(input())
holesArray = input().split()
holesArray = [int(i) for i in holesArray]
counter = [0] * len(holesArray)
m = int(input())
diameterOfBalls = input().split()
diameterOfBalls = [int(i) for i in diameterOfBalls]

result = [0] * len(diameterOfBalls)
start = len(holesArray) - 1

for i in range(len(diameterOfBalls)):
	for j in range(start, -1, -1):
		if(diameterOfBalls[i] <= holesArray[j] and counter[j] < j+1):
			result[i] = j+1
			counter[j] += 1
			break

s = "-"
result = [str(i) for i in result]
print(s.join(result))
