"""Stub unit test file."""

import project_name


def test_sum_as_string(benchmark):
    """Test the sum_as_string function."""
    assert benchmark(project_name.sum_as_string, 2, 2) == "4"
