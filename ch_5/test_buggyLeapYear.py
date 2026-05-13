import pytest
from buggyLeapYear import is_leap_year

def test_is_leap_year():
    list = [1700,1800,1900,2100,2200,2300,2500,2600,2004]
    for i in list:
        assert is_leap_year(i) == False