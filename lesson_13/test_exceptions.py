import pytest
from exceptions_lection import get_rectangle_perimeter, NotPositiveError


class TestMyExceptions:
    @pytest.mark.parametrize("width, height, expected", [(2, 4, 8), (1, 0, 0)])
    def test_correct_cases(self, width, height, expected):
        actual = get_rectangle_perimeter(width, height)
        assert expected == actual

    @pytest.mark.parametrize("width, height", [(-2, 4), (1, -4), (-5, -9)])
    def test_bad_cases(self, width, height):
        with pytest.raises(NotPositiveError):
            get_rectangle_perimeter(width, height)
