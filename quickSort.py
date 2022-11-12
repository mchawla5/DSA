'''
QUICK SORT
Uses divide and conquer to create subarrays by taking a pivot
The important thing is that elements in the left subarray are less than the pivot and greater than the pivot in the right subarray 

SOLUTION:
    |_ Time Complexity - O(nlogn); worst is O(n^2)
    |_ Space Complexity - O(n)
'''

def partition(arr, low, high):
    pivot = arr[high]
    i = low-1
    for j in range(low, high):
        if arr[j]<= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1

def quickSort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)
    return arr

if __name__ == "__main__":
    tests = []
    # TESTCASE 1: empty arr
    tests.append({
        'input': {
            'arr': [],
            'low': -1,
            'high': -1
        },
        'output': []
    })
    # TESTCASE 2: one element
    tests.append({
        'input': {
            'arr': [2],
            'low': 0,
            'high': 0
        },
        'output': [2]
    })
    #TESTCASE 3: Ascending array
    tests.append({
        'input': {
            'arr': [1,2,3,4,5],
            'low': 0,
            'high': 4
        },
        'output': [1,2,3,4,5]
    })
    #TESTCASE 4: Descending array
    tests.append({
        'input': {
            'arr': [5,4,3,2,1],
            'low': 0,
            'high': 4
        },
        'output': [1,2,3,4,5]
    })
    #TESTCASE 5: Repeated elements
    tests.append({
        'input': {
            'arr': [2,3,1,1,6,5,7,5],
            'low': 0,
            'high': 7
        },
        'output': [1,1,2,3,5,5,6,7]
    })

    for i in range(len(tests)):
        test = tests[i]
        print("TESTCASE "+str(i+1)+": "+str(quickSort(**test['input']) == test['output']))