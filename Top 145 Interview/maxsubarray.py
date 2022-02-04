# kadanes algo
def maxsubarray(arr):
    csum = arr[0]
    osum = arr[0]
    for i in range(1,len(arr)):
        if csum >= 0:
            csum+=arr[i]
        else:
            csum = arr[i]
        if csum > osum:
            osum = csum
    return osum

def maxSubarray(arr):
    maxsum = arr[0]
    currmax = 0
    for i in arr:
        if currmax < 0:
            currmax= 0
        currmax+=i
        maxsum = max(maxsum,currmax)
    return maxsum

arr = [int(ele) for ele in input().split()]
osum = maxsubarray(arr)
print(osum)