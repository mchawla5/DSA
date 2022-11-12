'''
QUICK SORT
Uses divide and conquer to create subarrays by taking a pivot
The important thing is that elements in the left subarray are less than the pivot and greater than the pivot in the right subarray 

SOLUTION:
    |_ Time Complexity - O(n); worst is O(nlogn)
    |_ Space Complexity - O(1)
'''

def heapify(arr, size, index):
    root_index = index
    left_index = 2*index + 1
    right_index = 2*index +2

    if left_index < size and arr[root_index] < arr[left_index]:
        root_index = left_index
    if right_index < size and arr[root_index] < arr[right_index]:
        root_index = right_index
    if root_index != index:
        arr[root_index], arr[index] = arr[index], arr[root_index]
        heapify(arr, size, root_index)

def heapSort(arr):
    size = len(arr)
    for i in range(size//2 -1, -1, -1):
        heapify(arr, size, i)
    for i in range(size-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
    return arr

if __name__ == "__main__":
    tests = []
    # TESTCASE 1: empty arr
    tests.append({
        'input': {
            'arr': []
        },
        'output': []
    })
    # TESTCASE 2: one element
    tests.append({
        'input': {
            'arr': [2]
        },
        'output': [2]
    })
    #TESTCASE 3: Ascending array
    tests.append({
        'input': {
            'arr': [1,2,3,4,5]
        },
        'output': [1,2,3,4,5]
    })
    #TESTCASE 4: Descending array
    tests.append({
        'input': {
            'arr': [5,4,3,2,1]
        },
        'output': [1,2,3,4,5]
    })
    #TESTCASE 5: Repeated elements
    tests.append({
        'input': {
            'arr': [2,3,1,1,6,5,7,5]
        },
        'output': [1,1,2,3,5,5,6,7]
    })

    for i in range(len(tests)):
        test = tests[i]
        print("TESTCASE "+str(i+1)+": "+str(heapSort(**test['input']) == test['output']))