# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 16:48:26 2020

@author: 冉雄
"""
#冒泡排序
def bubble_sort(nums):
    for i in range(0,len(nums) - 1):
        for j in range(0,len(nums) - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j],nums[j + 1] = nums[j + 1],nums[j]
    return nums

#快速排序(二分)
def quick_sort(nums):
    if len(nums) >= 2:
        mid = nums[len(nums)//2]# 一般取中间值，也可以选取第一个或最后一个元素        
        left = []
        right = []
        nums.remove(mid)
        for item in nums:
            if item >= mid:
                right.append(item)
            else:
                left.append(item)
        return quick_sort(left) + [mid] + quick_sort(right)
    return nums
#归并排序
def MergeSort(lists):
    if len(lists) <= 1:
        return lists
    num = int( len(lists) / 2 )
    left = MergeSort(lists[:num])
    right = MergeSort(lists[num:])
    return Merge(left, right)
def Merge(left,right):
    r, l=0, 0
    result=[]
    while l<len(left) and r<len(right):
        if left[l] <= right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1
    result += list(left[l:])
    result += list(right[r:])
    return result

#print(MergeSort([1, 2, 32, 14, 58, 16, 7, 90, 21, 23, 45]))
#选择排序
def selection_sort(nums):
    for i in range(0,len(nums)):#0...i已经排好序了
        min_j = i #当前最小值索引
        for j in range(i+1,len(nums)):
            if nums[j] < nums[min_j]:
                min_j = j #如果找到最小值就更新min_j
        nums[i],nums[min_j] = nums[min_j],nums[i] 
    return nums
#print(selection_sort1([1, 2, 32, 14, 58, 16, 7, 90, 21, 23, 45]))
def insertion_sort(nums):
    for i in range(1,len(nums)):
       for j in range(0,i-1):
           if nums[i] > nums[j]:
               nums[i],nums[j] = nums[j],nums[i]
#print(insertion_sort([1, 2, 32, 14, 58, 16, 7, 90, 21, 23, 45]))

#插入排序#堆排序

def big_endian(arr,start,end):    
    root=start    
    child=root*2+1 #表示左孩子    
    while child<=end:
    #孩子比最后一个节点还大，也就意味着最后一个叶子节点了，就得跳出去一次循环，已经调整完毕     
        if child+1<=end and arr[child]<arr[child+1]:
        #为了始终让其跟子元素的较大值比较，如果右边大就左换右，左边大的话就默认           
            child+=1            
        if arr[root]<arr[child]:
        #父节点小于子节点直接交换位置，同时坐标也得换，这样下次循环可以准确判断：是否为最底层，
        #是不是调整完毕                
            arr[root],arr[child]=arr[child],arr[root]                
            root=child                
            child=root*2+1            
        else:               
            break
         
def heap_sort(arr): #无序区大根堆排序    
    first=len(arr)//2 - 1    
    for start in range(first,-1,-1):
    #从下到上，从左到右对每个节点进行调整，循环得到非叶子节点        
        big_endian(arr,start,len(arr)-1) #去调整所有的节点    
    for end in range(len(arr)-1,0,-1):        
        arr[0],arr[end]=arr[end],arr[0] #顶部尾部互换位置        
        big_endian(arr,0,end-1) #重新调整子节点的顺序，从顶开始调整    
    return arr
     
































