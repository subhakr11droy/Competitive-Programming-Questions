def calculate_sum(arr):
    sum=0
    for i in range(len(arr)):
        sum+=arr[i]
    return sum



ar = list(map(int, input().rstrip().split()))
print(calculate_sum(ar))