class Solution: 
    def selectionSort(self, arr):
        for i in range(len(arr)):
            m=i
            for j in range(i,len(arr)):
                if arr[j]<arr[m]:
                     m=j
            temp=arr[i]
            arr[i]=arr[m]
            arr[m]=temp
        return arr
