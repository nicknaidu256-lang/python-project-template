from template_package.utils import get_greeting


def test_get_greeting():
    assert get_greeting("Test") == "Hello, Test!"
