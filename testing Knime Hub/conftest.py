import pytest
import selenium

def pytest_runtest_setup(item):
    print("\n this is step one")

def pytest_runtest_call(item):
    print("\n this is step two")


def pytest_runtest_teardown(item):
    print("\n this is step three")