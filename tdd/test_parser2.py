from parser2 import parse

# testing

def setup_function(function):
    """ setup any state tied to the execution of the given function.
    Invoked for every test function in the module.
    """
    print("setup")

def teardown_function(function):
    """ teardown any state that was previously setup with a setup_function
    call.
    """
    print("teardown")

def test_digit():
    print("test_digit")
    for i in range(0,10):
        assert parse(str(i)) == i

def test_integer():
    print("test_integer")
    for i in range(0,1000):
        assert parse(str(i)) == i

def test_negative_integer():
    for i in range(0,1000):
        assert parse("-" + str(i)) == -i

def test_float():
    for i in range(0,1000):
        f = i / 100.0
        assert f - 0.0000001 <= parse(str(f)) <= f + 0.0000001

def test_negative_float():
    for i in range(0,1000):
        f = -1 * (i / 100.0)
        assert f - 0.0000001 <= parse(str(f)) <= f + 0.0000001

if __name__ == "__main__":
    test_negative_integer()
