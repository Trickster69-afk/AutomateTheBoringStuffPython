import pytest
from rookCapture import white_rook_can_capture

def test_white_rook_can_capture():
    assert white_rook_can_capture('d3', {'d7': 'bQ', 'd2': 'wB', 'f3': 'bP', 'a3': 'bN'}) == ['d7', 'f3', 'a3']
    assert white_rook_can_capture('e4', {'a1': 'wP', 'b2': 'wN', 'c3': 'wB'}) == []
    assert white_rook_can_capture('c5', {'c1': 'bR', 'c8': 'bK', 'a5': 'wQ', 'h5': 'wP'}) == ['c1', 'c8']
    assert white_rook_can_capture('f6', {'a6': 'bP', 'd6': 'bN', 'h6': 'bQ', 'f1': 'wB'}) == ['a6', 'd6', 'h6']
    assert white_rook_can_capture('b2', {'b8': 'bQ', 'b5': 'wP', 'b1': 'bR', 'a2': 'bN', 'h2': 'wB', 'c2': 'bP'}) == ['b8', 'b1', 'a2', 'c2']
    assert white_rook_can_capture('a1', {'a8': 'bK', 'h1': 'bQ', 'a2': 'bP', 'b1': 'wN'}) == ['a8', 'h1', 'a2']
    assert white_rook_can_capture('e5', {'e8': 'bK', 'e1': 'bP', 'a5': 'bN', 'h5': 'bB', 'e3': 'wQ', 'c5': 'bR'}) == ['e8', 'e1', 'a5', 'h5', 'c5']

    