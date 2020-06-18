'''
Input: a List of integers
Returns: a List of integers
'''
def product_of_all_other_numbers(arr):
    # Your code here

    # Create a new list to hold all numbers except the one at the specific index
    newList = []

    # Iterate through the list
    for index, item in enumerate(arr):
        # Create new list that holds all except th one at the index
        other_nums = [x for i, x in enumerate(arr) if i != index]
        product = 1

        # Iterate through the numbers and multiply them together 
        for n in other_nums:
            product = product * n
        # Append the results to the new list
        newList.append(product)
    return newList


if __name__ == '__main__':
    # Use the main function to test your implementation
    # arr = [1, 2, 3, 4, 5]
    arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
