# Standard-algorithms-in-python

## 1. Binary Search
 Binary Search is used to search for a key in a sorted array. It is a Divide and conquer algorithm. 
 ###### Input : Sorted list of numbers, key
 ###### Output : index of key in list
 #### Steps
 1. Find mid point of given list.
 2. Check if number at mid is equal to key. If equal then return mid.
 3. If not equal then it will search for key in one half of the list based on these condition - 
    1. If number at mid of list is greater than key then search in first half of the list.
    2. If number at mid of list is smaller than key then search in second half of the list.
 
 #### Time Complexity
 	Best case - O(1)
 	Worst and Average case - O(log n) here n is size of list of numbers.


 ## 2. Partition
 Partition algorithm separates a list of numbers based on a pivot such that numbers less than and equal to pivot are on the left side of the pivot and numbers greater than the pivot are on right side of the pivot. After partiton, pivot is the element which is present on its actual location in sorted array.

 ###### Choice of pivot : first element or randomly selected element

 ###### Input : list of numbers
 ###### Output : index of pivot element

 #### Steps
 1. Select pivot element.
 2. Take two variables i = 0 and j = -1.
 3. Variable j tells that all the element at index less than or equal to j are less than or equal to pivot and all the element to the right of index j till index i are greater than pivot eement.
 4. Scan the list once using "i" and whenever an element less than or equal to pivot occurs swap it element at index j+1(element which is greater than pivot).
 5. After scanning swap first element of list with element at index j, so that pivot is present at index j.
 6. Return j which is index of pivot.


 #### Time Complexity
 	Every Case - O(n) here n is size of list of numbers.

 ## 3. K-th Smallest Number in an array
 K-th smallest number can be found using partition algorithm. If the pivot index "m" returned by partition is equal to k then element at mth index is k-th smallest number. If pivot index returned by partiton is greater then k then apply partition on left part and if pivot index is less than k then apply partition on right part


 ## 4. K-th Largest Number in an array
 Finding K-th largest number is same as finding "n - k + 1" th smallest element, here n is the length of array.



 ## Merge-sort
 Merge sort is a divide and conquer algorithm
















 

