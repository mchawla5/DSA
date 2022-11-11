'''
MERGE SORT
Uses divide and conquer to create subarrays, then they are sorted and merged back again
'''

def merge(nums1, nums2):
    new_arr = []
    i=j=0
    while i < len(nums1) and j < len(nums2):
        if nums1[i] <= nums2[j]:
            new_arr.append(nums1[i])
            i += 1
        else:
            new_arr.append(nums2[j])
            j += 1
    return new_arr + nums1[i:] + nums2[j:]

def mergeSort(arr):
    if len(arr)<2:
        return arr
    mid = len(arr)//2
    l_arr = mergeSort(arr[:mid])
    r_arr = mergeSort(arr[mid:])
    result = merge(l_arr, r_arr)
    return result


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
        print("TESTCASE "+str(i+1)+": "+str(mergeSort(**test['input']) == test['output']))