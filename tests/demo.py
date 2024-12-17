import pytest

# @pytest.fixture()
# def before_after():
#     print("\nBefore test")
#     yield
#     print("\nAfter test")


def demo_1():
    assert 1 == 1


def demo_2(before_after):
    assert 2 == 2
