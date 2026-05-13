import pytest
from coordinateDirections import get_end_coordinates_directions

def test_get_end_coordinates_directions():
    directions = [
    ["n", "s", "e", "w", "e", "n", "s"],
    ["w", "e", "n", "n", "s", "w", "e", "e"],
    ["s", "s", "w", "n", "e"],
    ["e", "w", "n", "s", "e", "w", "n"],
    ["n", "n", "e", "s", "w", "w", "e", "n", "s"],
    ["s", "e", "w", "n", "n", "e"],
    ["w", "e", "s", "n", "w", "e", "n"]
    ]
    
    assert get_end_coordinates_directions(directions[0]) == [1, 0]
    assert get_end_coordinates_directions(directions[1]) == [1, 1]
    assert get_end_coordinates_directions(directions[2]) == [0, -1]
    assert get_end_coordinates_directions(directions[3]) == [0, 1]
    assert get_end_coordinates_directions(directions[4]) == [0, 1]
    assert get_end_coordinates_directions(directions[5]) == [1, 1]
    assert get_end_coordinates_directions(directions[6]) == [0, 1]
    