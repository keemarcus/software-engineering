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
