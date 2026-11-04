import pytest


def pytest_collection_modifyitems(items):
    for item in items:
        if "_func_" in item.nodeid:
            item.add_marker(pytest.mark.func)
        elif "_exception_" in item.nodeid:
            item.add_marker(pytest.mark.exception)
