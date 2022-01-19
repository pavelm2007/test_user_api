import pytest

from main.testing.factory import FixtureFactory


@pytest.fixture()
def factory():
    return FixtureFactory()
