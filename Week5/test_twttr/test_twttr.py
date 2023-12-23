from twttr import shorten


def test_upper():
    assert shorten("HELLO WORLD") == "HLL WRLD"


def test_lower():
    assert shorten("hello world") == "hll wrld"


def test_mix():
    assert shorten("hElLo WoRlD") == "hlL WRlD"


def test_special():
    assert shorten("h3lL0 WoRld!@") == "h3lL0 WRld!@"
