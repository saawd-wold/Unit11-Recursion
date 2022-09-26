from src.binary import bin2den, den2bin

def test_den2bin():
    assert den2bin(0) == "0", "Wrong representation of 0!"
    assert den2bin(1) == "1", "Wrong representation of 1!"
    assert den2bin(10) == "1010", "Wrong representation of 10!"
    assert den2bin(123456789) == bin(123456789)[2:], "Wrong representation of 123456789!"
    assert den2bin(1<<420 + 1) == bin(1<<240 + 1)[2:], "Wrong representation of 2^420+1!"

def test_bin2den():
    assert bin2den("0") == 0, "Wrong interpretation of 0!"
    assert bin2den("1") == 1, "Wrong interpretation of 1!"
    assert bin2den("10101010101") == 0b10101010101, "Wrong interpretation of 10101010101!"