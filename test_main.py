import pytest
from main import dec2bin, bin2dec


def test_dec2bin_pos():
    assert dec2bin(33, 8) == '00100001'


def test_dec2bin_neg():
    assert dec2bin(-33, 8) == '11011111'


def test_dec2bin_zero():
    assert dec2bin(0, 10) == '0000000000'


def test_dec2bin_neg_zero():
    assert dec2bin(0, 10) == '0000000000'


def test_dec2bin_bin_dig_true():
    assert dec2bin(31, 6) == '011111'


def test_dec2bin_bin_dig_false():
    with pytest.raises(ValueError,
                       match='The specified bin_dig is less than the required'
                             ' number to represent the x'):
        dec2bin(31, 5)


def test_bin2dec_pos():
    assert bin2dec("1010", 0) == 10


def test_bin2dec_sign_pos():
    assert bin2dec("01010", 1) == 10


def test_bin2dec_sign_neg():
    assert bin2dec("10110", 1) == -10


if __name__ == '__main__':
    pytest.main()
