import numpy as np

arr = [int(x) for x in raw_input().split(" ")]

key = input("enter key : ")

np_arr = np.array(arr)

def binarysearch(numbers,l,h,x):

	mid = (l + h)/2
	if numbers[mid] == x :
		#print mid
		return mid
	elif numbers[mid] > x :
		#print len(numbers[-1 : mid]) 
		return binarysearch(numbers,l,mid-1,x)
	else :
		#print len(numbers[mid + 1 : -1])
		return binarysearch(numbers,mid + 1,h,x)


print binarysearch(np_arr,0,len(np_arr)-1,key)