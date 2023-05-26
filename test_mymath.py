import mymath as mm
import os


def test_add():
    assert mm.add(2, 3) == 2 + 3
    assert mm.add(5, -10.5) == 5 + (-10.5)


def test_subtract():
    assert mm.subtract(10, 5) == 10 - 5


def test_secrets():
    ovirt_pwd = os.environ.get("OVIRT_PWD", "")
    assert ovirt_pwd == "ovirtpassword"
