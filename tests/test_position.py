import pytest

from src.core.position import Position


class TestPosition:
    def test_initial_position(self):
        pos = Position(2, 3)
        assert pos.get_position() == (2, 3)

    def test_set_position(self):
        pos = Position(0, 0)
        pos.set_position(5, 7)
        assert pos.get_position() == (5, 7)

    def test_set_position_negative_values(self):
        pos = Position(1, 1)
        pos.set_position(-1, -2)
        assert pos.get_position() == (-1, -2)

    def test_set_position_same_values(self):
        pos = Position(4, 4)
        pos.set_position(4, 4)
        assert pos.get_position() == (4, 4)
