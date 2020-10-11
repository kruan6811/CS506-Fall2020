import pytest

from cs506 import determinant

def test_euclidean():
    # sanity checks
    try:
        determinant.determinant([])
    except ValueError as e:
        assert str(e) == "size of matrix must be at least 1x1"
    try:
        determinant.determinant([[]])
    except ValueError as e:
        assert str(e) == "must be a square matrix"
    try:
        determinant.determinant([[1,2],[1]])
    except ValueError as e:
        assert str(e) == "must be a square matrix"
    
    assert determinant.determinant([[1]]) == 1
    assert determinant.determinant([[1,2],[3,4]]) == -2
    assert determinant.determinant([[1,2,3],[4,5,6],[7,8,9]]) == 0
    assert determinant.determinant([[1,3,5,9],[1,3,1,7],[4,3,9,7],[5,2,0,9]]) == -376
