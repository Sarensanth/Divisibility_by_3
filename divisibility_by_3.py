def divisibility(array):

    s=sum(array) #divisibility rule of 3 sum of digits by 3 = 0
    if s%3==0:
        return 1
    return 0


array=list(map(int,input().split()))
print(divisibility(array))