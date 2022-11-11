'''
BUBBLE SORT
Increment through the array to compare the current element with the next element
If larger then swap them

SOLUTION - O(n^2)
'''

def bubbleSort(arr):
    new_arr = list(arr)
    for _ in range(len(new_arr)-1):
        for i in range(len(new_arr)-1):
            if new_arr[i] > new_arr[i+1]:
                new_arr[i], new_arr[i+1] = new_arr[i+1], new_arr[i]
    return new_arr

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
        print("TESTCASE "+str(i+1)+": "+str(bubbleSort(**test['input']) == test['output']))