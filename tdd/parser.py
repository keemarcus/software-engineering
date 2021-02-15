def parse(s):
    v = 0
    sign = 1
    if s[0] == '-':
        sign = -1
        s = s[1:]
    fraction = False
    multiplier = 1.0
    for c in s:
        assert c in "0123456789.", "Syntax error"
        if c == '.':
            assert (not fraction), "Syntax error"
            fraction = True
        else:
            if fraction:
                multiplier = multiplier / 10.0
                v = v + (ord(c) - ord('0')) * multiplier
            else:
                v = v * 10 + ord(c) - ord('0')
    return v * sign


# testing

import unittest

class TestParser(unittest.TestCase):

    def setUp(self):
        print("setUp")

    def tearDown(self):
        print("tearDown")

    def test_00_digit(self):
        for i in range(0,10):
            assert parse(str(i)) == i

    def test_01_integer(self):
        for i in range(0,1000):
            assert parse(str(i)) == i

    def test_02_negative_integer(self):
        for i in range(0,1000):
            assert parse("-" + str(i)) == -i

    def test_03_float(self):
        for i in range(0,1000):
            f = i / 100.0
            assert f - 0.0000001 <= parse(str(f)) <= f + 0.0000001

    def test_04_negative_float(self):
        for i in range(0,1000):
            f = -1 * (i / 100.0)
            assert f - 0.0000001 <= parse(str(f)) <= f + 0.0000001

if __name__ == "__main__":
    unittest.main(verbosity=2)