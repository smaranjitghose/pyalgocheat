def bubble_sort(arr,order='asc'):
    n = len(arr)
    for i in range(n-1):
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
    if order =='asc':
        return arr
    elif order =='desc':
        return arr[::-1]
    
def partition(arr,low,high):
    i = low-1
    pivot = arr[high]
    for j in range(low,high):
        if arr[j]<=pivot:
            i=i+1
            arr[i],arr[j] = arr[j],arr[i]
    arr[i+1],arr[high] = arr[high],arr[i+1]
    return (i+1)

def quick_sort(arr,low,high): 
    if low < high: 
        partition_index = partition(arr,low,high) 
        quick_sort(arr, low, partition_index-1) 
        quick_sort(arr, partition_index+1, high)


def merge(arr, l, m, r): 
    n1 = m - l + 1
    n2 = r- m 
  
    L = [0] * (n1) 
    R = [0] * (n2) 
    
    for i in range(0 , n1): 
        L[i] = arr[l + i] 
  
    for j in range(0 , n2): 
        R[j] = arr[m + 1 + j] 
  
    i,j,k = 0,0,l      
    while i < n1 and j < n2 : 
        if L[i] <= R[j]: 
            arr[k] = L[i] 
            i += 1
        else: 
            arr[k] = R[j] 
            j += 1
        k += 1
    while i < n1: 
        arr[k] = L[i] 
        i += 1
        k += 1
    while j < n2: 
        arr[k] = R[j] 
        j += 1
        k += 1
  
def merge_sort(arr,l,r): 
    if l < r: 
        m = (l+(r-1))//2
        merge_sort(arr, l, m) 
        merge_sort(arr, m+1, r) 
        merge(arr, l, m, r)

def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1,len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i],arr[min_idx] = arr[min_idx],arr[i]
    return arr

        