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
