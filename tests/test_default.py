"""Stub unit test file."""

from project_name import sum_as_string


def test_sum_as_string(benchmark):
    """Test the sum_as_string function."""
    assert benchmark(sum_as_string, 2, 2) == '4'
