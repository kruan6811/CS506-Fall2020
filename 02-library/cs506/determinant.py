def determinant(matrix):
    """
    Given `matrix`, which is an array of arrays,
    return the determinant
    """
    if ((matrix == None) or (len(matrix) == 0)):
        raise ValueError("size of matrix must be at least 1x1")

    for row in range(len(matrix)):
        if (len(matrix) != len(matrix[row])):
            raise ValueError("must be a square matrix")

    # base case
    if (len(matrix) == 1):
        return matrix[0][0]

    # recursive case
    ret_determinant, sign  = 0, 1
    for col in range(len(matrix)):
        smaller_matrix = get_smaller_matrix(matrix, col)
        to_add = matrix[0][col] * determinant(smaller_matrix)
        ret_determinant += (to_add*sign)
        sign *= -1

    return ret_determinant

def get_smaller_matrix(matrix, col_to_exclude):
    """
    Helper function for determinant

    Given a n x n matrix, return a smaller matrix
    that exclues `col_to_exclude` from matrix
    """
    size = len(matrix)-1
    ret = [[] * size for i in range(size)]

    for row in range(1, len(matrix)):
        for col in range(len(matrix)):
            if col == col_to_exclude:
                continue

            ret[row-1].append(matrix[row][col])
    
    return ret
