import time
import pytest


@pytest.mark.slow
def test_slow() -> None:
    """A dummy test that takes a an hour to run."""
    time.sleep(60 * 60)
    pass


def test_quick() -> None:
    """A dummy test that takes 2 seconds to run."""
    time.sleep(2)
    pass


def test_very_fast() -> None:
    """A dummy test that takes 1 second to run."""
    time.sleep(1)
    pass


def test_func_function1():
    pass


def test_func_function2():
    pass


def test_exception_keyerror():
    with pytest.raises(KeyError):
        {"a": 0, "b": 1}["not a key"]


def test_exception_indexerror():
    with pytest.raises(IndexError):
        [0, 1, 2][3]
