from bank import value


def test_hello():
    assert value("hello") == 0
    assert value("hello bla bla") == 0
    assert value("Hello bla bla") == 0


def test_h():
    assert value("hi") == 20
    assert value("hi bla bla") == 20
    assert value("Hi bla bla") == 20


def test_diff():
    assert value("whats'up") == 100
    assert value("whats'up sir") == 100
    assert value("Whats'up sir") == 100
