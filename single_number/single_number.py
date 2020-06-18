'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    # Your code here

    # set() removes duplicates, it's a greedy solution

    # return 2 * sum(set(arr)) - sum(arr)

    # Create a list for the unmatched numbers
    unmatched_number = []

    # Iterate through the list
    for n in arr:
        # Set default for found
        found = False

        # Enumerate through the arr to compare
        for index, item in enumerate(unmatched_number):
            # if equals pop and set found to true
            if item == n:
                unmatched_number.pop(index)
                found = True
                break
        # if not found dupl, then append to unmatched and return
        if not found:
            unmatched_number.append(n)
    return unmatched_number[0]


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")