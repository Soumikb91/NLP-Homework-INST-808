import numpy as np


class DimensionError(Exception):
    """Base class for exceptions in this module."""
    def __init__(self, condition):
        print(condition)
        
    


def matrix_multiply(left, right):
    """Multiply two 2D matrices, raise DimensionError if the dimensions don't match."""
    
    # Checking the inner dimension are matching or not
    if (left.shape[1] != right.shape[0]):
        raise DimensionError('dimension are not matching')
    
    # Creating the result matrix
    result = [[0 for i in range(right.shape[1])] for j in range(left.shape[0])]
    
    # Actual matrix product calculation
    for row in range(left.shape[0]):
        for col in range(right.shape[1]):
            for k in range(left.shape[1]):
                result[row][col] += left[row][k] * right[k][col]

    return result


def user_input_matrix():
    R = int(input("Enter the number of rows:\t"))
    C = int(input("Enter the number of columns:\t"))

    assert (R > 0), "Number of rows must be positive"
    assert (C > 0), "Number of columns must be positive"

    # Initialize matrix 
    matrix = []
    print("Enter the entries rowwise:")

    # For user input 
    for i in range(R):  # A for loop for row entries
        a = []
        for j in range(C):  # A for loop for column entries
            a.append(int(input("Row %i, Column %i:\t" % (i, j))))
        matrix.append(a)

    return np.array(matrix)


if __name__ == "__main__":
    print("Left matrix")
    print("=====================")
    left = user_input_matrix()
    print("Right matrix")
    print("=====================")
    right = user_input_matrix()

    print("Product")
    print("=====================")
    print(matrix_multiply(left, right))
