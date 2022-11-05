'''
GIVEN A NUMBER OF CARDS WITH INTEGER VALUES IN DESCENDING ORDER, FIND THE CARD WITH A PARTICULAR VALUE.

Cards can have multiple values.
Example:
5,4,4,4,3,3,3,3,2,1
In such a case return the first index

SOLUTION: O(logn)
'''

def testLocation(cards, query, mid):
    mid_number = cards[mid]
    if mid_number == query:
        if mid-1>=0 and cards[mid-1] == query:
            return 'left'
        else:
            return 'found'
    elif mid_number < query:
        return 'left'
    else:
        return 'right'

def locateCard(cards, query):
    lo, hi = 0, len(cards)-1
    while lo <= hi:
        mid = (lo+hi)//2
        result = testLocation(cards, query, mid)
        if result == 'found':
            return mid
        elif result == 'left':
            hi = mid-1
        elif result == 'right':
            lo = mid+1
    return -1


if __name__=="__main__":
    tests = []
    # TESTCASE 1: query occurs somewhere in middle
    tests.append({
        'input': {
            'cards': [13,11,10,7,4,3,1,0],
            'query': 7
        },
        'output': 3
    })
    # TESTCASE 2: query is the first element
    tests.append({
        'input': {
            'cards': [4,2,1,-1],
            'query': 4
        },
        'output': 0
    })
    # TESTCASE 3: query is the last element
    tests.append({
        'input': {
            'cards': [3,-1,-9,-127],
            'query': -127
        },
        'output': 3
    })
    # TESTCASE 4: cards contain just one element, which is query
    tests.append({
        'input': {
            'cards': [6],
            'query': 6
        },
        'output': 0
    })
    # TESTCASE 5: cards doesn't contain query
    tests.append({
        'input': {
            'cards': [9,7,5,2,-9],
            'query': 4
        },
        'output': -1
    })
    # TESTCASE 6: cards is empty
    tests.append({
        'input': {
            'cards': [],
            'query': 7
        },
        "output": -1
    })
    # TESTCASE 7: contains repeating numbers
    tests.append({
        'input': {
            'cards': [8,8,6,6,6,6,6,3,2,2,2,0,0,0],
            'query': 3
        },
        'output': 7
    })
    # TESTCASE 8: query occurs at more than 1 position
    tests.append({
        'input': {
            'cards': [8,8,6,6,6,6,6,3,2,2,2,0,0,0],
            'query': 6
        },
        'output': 2
    })
    for i in range(len(tests)):
        test = tests[i]
        print("TESTCASE "+str(i)+": "+str(locateCard(**test['input']) == test['output']))