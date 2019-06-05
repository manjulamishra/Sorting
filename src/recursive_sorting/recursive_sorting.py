# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len(arrA) + len(arrB) 
    merged_arr = [0] * elements # creates a list of zeros in the length of arrA + arrB
    # Let's layout the base case
    if arrA == []:
      return arrB
    if arrB == []:
      return arrA  
    if arrA[0] <= arrB[0]:
        # here I'm directly overwriting the elements of merged_arr
        merged_arr = [arrA[0]] + merge(arrA[1:], arrB) # the 1st element of + call the fn
        return merged_arr
    else:
      merged_arr= [arrB[0]] + merge(arrA, arrB[1:]) # if the otherwise is true
    return merged_arr
    


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
     # base case
    if len(arr) <= 1:
      return arr
    half = len(arr)//2 # let's find out the midpoint to break the list into halves
    first_half = arr[0:half] # first half of the list
    second_half = arr[half:] # second half of the list
    
    list_1 = merge_sort(first_half) # recursively sorts first half
#     print (list_1)
    list_2 = merge_sort(second_half) # recursively sorts second half
#     print(list_2)
    arr = merge(list_1, list_2) # call the merge method to merge sorted list
    return arr


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
