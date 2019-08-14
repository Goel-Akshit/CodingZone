t = int(input())
while(t != 0):
    n = int(input())
    score = input().split()
    score = [int(i) for i in score]

    foul = input().split()
    foul = [int(i) for i in foul]

    result = 0

    for i in range(n):
        result = max((score[i] * 20) - (foul[i] * 10),result)

    print(result)
    t -= 1
