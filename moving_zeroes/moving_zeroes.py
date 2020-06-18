'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    # Your code here
    # Create a second list
    arr1 = []
    # Count the number of zeros
    numZeros = 0

    # Iterate through the list
    for item in arr:
        # Check for zeros, add them to counter
        if item == 0:
            numZeros += 1
        # If it doesn't match append it to the second array
        else:
            arr1.append(item)
    # While the num of zeros is not zero, decrement and append to the second array,
    # then return the second array
    while numZeros != 0:
        numZeros -= 1
        arr1.append(0)
    return arr1


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")