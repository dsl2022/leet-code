def threeSum(arr):
    answer = []
    arr = sorted(arr)
    if len(arr) < 3:    
        return []
    for i in range(len(arr)-2):        
        current = arr[i]
        target = 0 - current
        left = i+1
        right = len(arr)-1
        while left < right:
            if arr[left]+arr[right]==target:
                
                answer.append([current,arr[left],arr[right]])  
                break
            elif arr[left]+arr[right]<target:
                left+=1
            else:
                right-=1
    return answer


print(threeSum([-1,0,1,2,-1,-4]))