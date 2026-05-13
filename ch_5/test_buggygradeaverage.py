import pytest
from buggygradeaverage import calculate_grade_average

def test_calculate_grade_average():
    assert calculate_grade_average(4, 4) == 1
    assert calculate_grade_average(5, 2) == 2
    assert calculate_grade_average(200, 2) == 100

    #ZeroDivisionError has been fixed in the original program
    #as the next continuation of this problem