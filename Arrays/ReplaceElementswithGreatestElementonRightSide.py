class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        maxele = arr[n-1]
        arr[n-1] = -1
        for i in range(n-2, -1, -1):
            temp = arr[i]
            arr[i] = maxele
            if temp > maxele:
                maxele = temp
        return arr
 """
 Problem Statement:

Given an array arr, replace every element in that array with the greatest element among the elements to its right, and replace the last element with -1.

After doing so, return the array.

Example 1:

Input: arr = [17,18,5,4,6,1]

Output: [18,6,6,6,1,-1]

Constraints:


    1 <= arr.length <= 10^4

    1 <= arr[i] <= 10^5
 """
