t = int(input())

while(t != 0):

    n = int(input())

    c_array = input().split(" ")
    c_array = [int(i) for i in c_array]

    h_array = input().split(" ")
    h_array = [int(k) for k in h_array]
    min_temp = 0
    max_temp = 999999999999999999999999
    master_array = [0] * n
    for j in range(n):
        min_temp = max(0, j-c_array[j]+1)
        max_temp = min(n, j+c_array[j]+1)

    master_array.sort()
    h_array.sort()
    # print(master_array)
    # print(h_array)
    if(master_array == h_array):
        print("YES")

    else:
        print("NO")

    t -= 1
