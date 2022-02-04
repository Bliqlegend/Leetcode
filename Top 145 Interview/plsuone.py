def TRASH(arr):
    if arr[0] == 9:
        o = []
        o.append(1)
        for i in range(len(arr)):
            o.append(0)
        return o

    if arr[-1] < 9:
        arr[-1]+=1
        return arr
    else:
        for i in range(len(arr)-1,-1,-1):
            if arr[i] == 9:
                arr[i] = 0
                continue
            arr[i]+=1
            break
    return arr
    
def plusone(arr):
    idx = 1
    n = 0
    for i in range(len(arr)-1,-1,-1):
        n+=(arr[i]*idx)
        idx*=10
    n+=1
    o = []
    while n!=0:
        ele = int(n % 10)
        n = int(n/10)
        o.append(ele)
    start = 0
    end = len(o)-1
    while start < end:
        o[start],o[end] = o[end],o[start]
        start+=1
        end-=1
    return o
    

    


arr = [int(ele) for ele in input().split()]
print(plusone(arr))
